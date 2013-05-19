import sys, pickle
sys.path.append(r'..')

from marketsim import strategy, orderbook, trader, scheduler, observable, veusz, mathutils, timeserie
from common import run

def Dependency(graph, world, books):

    book_A = books['Asset A']
    book_B = books['Asset B']
    
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
    book_B.timeseries = orderbook_ts()
    
    liqVol = mathutils.product(mathutils.rnd.expovariate(.1), mathutils.constant(12))
    t_A = trader.SASM(book_A, 
                      strategy.LiquidityProvider(defaultValue=50., volumeDistr=liqVol), 
                      "LiquidityProvider_A", 
                      timeseries = trader_ts())
    
    t_B = trader.SASM(book_B, 
                      strategy.LiquidityProvider(defaultValue=150., volumeDistr=liqVol), 
                      "LiquidityProvider_B", 
                      timeseries = trader_ts())
    
    dep_AB = trader.SASM(book_A, 
                         strategy.Dependency(book_B, factor=2), 
                         "A dependent on B", 
                         timeseries = trader_ts())
    
    dep_BA = trader.SASM(book_B, 
                         strategy.Dependency(book_A, factor=.5), 
                         "B dependent on A", 
                         timeseries = trader_ts())

    dep2_AB = trader.SASM(book_A, 
                         strategy.Dependency2(book_B, factor=2), 
                         "A dependent on B 2", 
                         timeseries = trader_ts())
    
    dep2_BA = trader.SASM(book_B, 
                         strategy.Dependency2(book_A, factor=.5), 
                         "B dependent on A 2", 
                         timeseries = trader_ts())

    dep_AB_ex = trader.SASM(book_A, 
                            strategy.DependencyEx(book_B, factor=2), 
                            "A dependent on B ex", 
                            timeseries = trader_ts())
    
    dep_BA_ex = trader.SASM(book_B, 
                            strategy.DependencyEx(book_A, factor=.5), 
                            "B dependent on A ex", 
                            timeseries = trader_ts())
    
    return [t_A, t_B, dep_AB, dep_BA, dep2_AB, dep2_BA, dep_AB_ex, dep_BA_ex], [price_graph, amount_graph, eff_graph]

if __name__ == '__main__':    
    run("dependency", Dependency)