import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def MeanReversion(graph, world, books):

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
    
    V = 1
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=const(V*20), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))),
                       label="liquidity", 
                       timeseries = trader_ts())
    
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    signal_trader = trader.SASM(book_A, 
                                strategy.Signal(linear_signal, 
                                                volumeDistr = const(V*3)), 
                                "signal", 
                                timeseries = trader_ts())
    
    signal_trader.addTimeSerie(linear_signal, amount_graph)
    
    alpha = 0.015
    
    mean_reversion = trader.SASM(book_A, 
                                 strategy.MeanReversion(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="meanreversion", 
                                 timeseries = trader_ts())
    
    mean_reversion2 = trader.SASM(book_A, 
                                 strategy.MeanReversion2(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="meanreversion2", 
                                 timeseries = trader_ts())
    
    mean_reversion_ex=trader.SASM(book_A, 
                                 strategy.MeanReversionEx(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="meanreversion_ex", 
                                 timeseries = trader_ts())
    
    mean_reversion_ex2=trader.SASM(book_A, 
                                 strategy.MeanReversionEx2(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="meanreversion_ex 2", 
                                 timeseries = trader_ts())
    
    return [lp_A, signal_trader, mean_reversion, mean_reversion2, mean_reversion_ex, mean_reversion_ex2], [price_graph, eff_graph, amount_graph]

if __name__ == '__main__':
    run("mean_reversion", MeanReversion)