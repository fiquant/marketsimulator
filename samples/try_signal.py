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
    
    lp_A = trader.SASM(book_A, strategy = strategy.LiquidityProvider(volumeDistr=const(1)))
    linear_signal = signal.RandomWalk(initialValue=20, deltaDistr=const(-.1), label="20-0.1t")
    signal_trader = trader.SASM(book_A, strategy.Signal(linear_signal), "signal")
    
    price_graph += [assetPrice,
                    avg(assetPrice),
                    linear_signal,
                    observable.VolumeTraded(signal_trader)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(signal_trader),
                  observable.PnL(signal_trader)]
    
    return [lp_A, signal_trader], [price_graph, eff_graph]

if __name__ == '__main__':
    run("signal_trader", Signal)