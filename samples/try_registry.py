import sys
sys.path.append(r'..')

from marketsim import (strategy, orderbook, trader, order, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def Complete(graph, world, books):
    
    book_A = books['Asset A']

    price_graph = graph("Price")
    eff_graph = graph("efficiency")
    amount_graph = graph("amount")
     
    def trader_ts():
        thisTrader = trader.SASM_Proxy()
        return { observable.VolumeTraded(thisTrader) : amount_graph, 
                 observable.Efficiency(thisTrader)   : eff_graph }
    
    def orderbook_ts():
        thisBook = orderbook.Proxy()
        askPrice = observable.AskPrice(thisBook)
        bidPrice = observable.BidPrice(thisBook)
        assetPrice = observable.Price(thisBook)
        avg = observable.avg
        return [timeserie.ToRecord(askPrice, price_graph),
                timeserie.ToRecord(bidPrice, price_graph),
                timeserie.ToRecord(assetPrice, price_graph), 
                timeserie.ToRecord(avg(assetPrice, alpha=0.15), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.65), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.015), price_graph)]
       
    book_A.timeseries = orderbook_ts()
     
    t_A = trader.SASM(book_A, 
                      strategy.LiquidityProvider(
                            volumeDistr=const(70.), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))), 
                      "liquidity", 
                       timeseries = trader_ts())
    
    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))
    
    trader_200 = trader.SASM(book_A, fv_200_12, "t200", 
                             timeseries = trader_ts())
    
    fv_200 = fv_200_12.With(volumeDistr=const(1.))
     
    trader_200_1 = trader.SASM(book_A, fv_200, "t200_1", 
                               timeseries = trader_ts())
        
    trader_200_2 = trader.SASM(book_A, fv_200.With(), "t200_2", 
                               timeseries = trader_ts())
    
    trader_150 = trader.SASM(book_A,
                             strategy.FundamentalValue(fundamentalValue=const(150.),
                                                            volumeDistr=const(1.)),
                             "t150", 
                             timeseries = trader_ts())
    
    meanreversion = trader.SASM(book_A,
                                strategy.MeanReversion(volumeDistr=const(1.)),
                                "mr_0_15", 
                                timeseries = trader_ts())
    
    avg_plus = trader.SASM(book_A,
                           strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                average2=mathutils.ewma(0.015),
                                                volumeDistr=const(1.)),
                           label="avg+", 
                           timeseries = trader_ts())

    avg_minus = trader.SASM(book_A,
                           strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                average2=mathutils.ewma(0.15),
                                                volumeDistr=const(1.)),
                           label="avg-", 
                           timeseries = trader_ts())
    
    v_fv200 = trader.SASM(book_A,
                          strategy.TradeIfProfitable(fv_200),
                          "v_fv200", 
                          timeseries = trader_ts())
    def s_fv(fv):
        return strategy.TradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))

    def fv_virtual(fv):
        return trader.SASM(book_A, s_fv(fv), "v" + str(fv), 
                           timeseries = trader_ts())
        
    
    virtual_160 = fv_virtual(160.)
    virtual_170 = fv_virtual(170.)
    virtual_180 = fv_virtual(180.)
    virtual_190 = fv_virtual(190.)
    
    best = trader.SASM(book_A,
                       strategy.chooseTheBest([s_fv(160.),
                                               s_fv(170.),
                                               s_fv(180.),
                                               s_fv(190.), ]),
                       "best", 
                       timeseries = trader_ts())
    
    traders = [trader_150, trader_200, trader_200_1, trader_200_2,
                best,
#                tf, tf_0_15, tf_0_015, 
                meanreversion, avg_plus, avg_minus, v_fv200,
                virtual_160, virtual_170, virtual_180, virtual_190
               ]

    return (traders + [t_A], [price_graph, eff_graph, amount_graph])

if __name__ == '__main__':
    run('registry', Complete)