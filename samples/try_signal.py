import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def Signal(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(volumeDistr=const(2)),
                       "liquidity")
    
    linear_signal = signal.RandomWalk(initialValue=20, deltaDistr=const(-.1), label="20-0.1t")
    signal_trader = trader.SASM(book_A, strategy.Signal(linear_signal), "signal")
    signal_ex_trader = trader.SASM(book_A, strategy.SignalEx(linear_signal), "signal_ex")
    
    price_graph += [assetPrice,
                    avg(assetPrice),
                    linear_signal,
                    observable.VolumeTraded(signal_trader), 
                    observable.VolumeTraded(signal_ex_trader)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(signal_trader),
                  observable.PnL(signal_trader)]
    eff_graph += [observable.Efficiency(signal_ex_trader),
                  observable.PnL(signal_ex_trader)]
    
    return [lp_A, signal_trader, signal_ex_trader], [price_graph, eff_graph]

if __name__ == '__main__':
    run("signal_trader", Signal)