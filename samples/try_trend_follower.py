import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TrendFollower(graph, world, books):

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
    
    V = 1
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=const(V*4), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(100))),
                       label="liquidity", 
                       timeseries = trader_ts())
    
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    signal_trader = trader.SASM(book_A, 
                                strategy.Signal(linear_signal, 
                                                volumeDistr = const(V)), 
                                "signal", 
                                timeseries = trader_ts())
    
    signal_trader.addTimeSerie(linear_signal, amount_graph)
    
    alpha = 0.065
    
    trend_follower = trader.SASM(book_A, 
                                 strategy.TrendFollower(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="trendfollower", 
                                 timeseries = trader_ts())

    trend_follower2 = trader.SASM(book_A, 
                                 strategy.TrendFollower2(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="trendfollower2", 
                                 timeseries = trader_ts())

    trend_follower_ex = trader.SASM(book_A, 
                                    strategy.TrendFollowerEx(
                                       average=mathutils.ewma(alpha),
                                       volumeDistr = const(V)),
                                    label="trendfollower_ex", 
                                    timeseries = trader_ts())
        
    return [lp_A, signal_trader, trend_follower, trend_follower2, trend_follower_ex], [price_graph, eff_graph, amount_graph]

if __name__ == '__main__':
    run("trend_follower", TrendFollower)