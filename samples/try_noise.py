import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils,
                       scheduler, observable, veusz, registry, timeserie)

from common import run 

def Noise(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
    eff_graph = graph("efficiency")
    amount_graph = graph("amount")
     
    def trader_ts():
        thisTrader = trader.SASM_Proxy()
        return { observable.VolumeTraded(thisTrader) : amount_graph, 
                 observable.Efficiency(thisTrader)   : eff_graph }
    
    def orderbook_ts():
        assetPrice = observable.AskPrice(orderbook.Proxy())
        avg = observable.avg
        return [timeserie.ToRecord(assetPrice, price_graph), 
                timeserie.ToRecord(avg(assetPrice, alpha=0.15), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.65), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.015), price_graph)]
       
    book_A.timeseries = orderbook_ts()
    
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=mathutils.constant(2),
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))), 
                       "liquidity", 
                       timeseries = trader_ts())
    
    noise_trader = trader.SASM(book_A, strategy.Noise(), "noise", 
                               timeseries = trader_ts())
    
    noise_trader2 = trader.SASM(book_A, strategy.Noise2(), "noise2", 
                               timeseries = trader_ts())
    
    noise_ex_trader = trader.SASM(book_A, strategy.NoiseEx(), "noise_ex", 
                                  timeseries = trader_ts())
        
    noise_ex_trader2 = trader.SASM(book_A, strategy.NoiseEx2(), "noise_ex2", 
                                  timeseries = trader_ts())
        
    return [lp_A, noise_trader, noise_trader2, noise_ex_trader, noise_ex_trader2], [price_graph, eff_graph, amount_graph]


if __name__ == '__main__':    
    run("noise_trader", Noise)
