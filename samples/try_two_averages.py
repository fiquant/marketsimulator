import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TwoAverages(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    lp_A = trader.SASM(book_A, strategy = strategy.LiquidityProvider(volumeDistr=const(8)))
    linear_signal = signal.RandomWalk(initialValue=200, deltaDistr=const(-1), label="200-t")
    signal_trader = trader.SASM(book_A, strategy.Signal(linear_signal, volumeDistr=const(3)), "signal")
    
    slow = mathutils.ewma(alpha = 0.015)
    fast = mathutils.ewma(alpha = 0.15)
    
    avg_plus = trader.SASM(book_A, strategy.TwoAverages(average1 = slow, average2 = fast), 'avg+')
    avg_minus = trader.SASM(book_A, strategy.TwoAverages(average1 = fast, average2 = slow), 'avg-')
    
    price_graph += [assetPrice,
                    avg(assetPrice, 0.015),
                    avg(assetPrice, 0.15),
                    linear_signal,
                    observable.VolumeTraded(signal_trader),
                    observable.VolumeTraded(avg_plus),
                    observable.VolumeTraded(avg_minus)]
    
    eff_graph = graph("efficiency")
    eff_graph += [
                  observable.Efficiency(avg_plus),
                  observable.Efficiency(avg_minus),
                  ]
    
    return [lp_A, signal_trader, avg_plus, avg_minus], [price_graph, eff_graph]

if __name__ == '__main__':
    run("two_averages", TwoAverages)