import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TrendFollower(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    V = 1
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=const(V*3), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(100))),
                       label="liquidity")
    
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    signal_trader = trader.SASM(book_A, 
                                strategy.Signal(linear_signal, 
                                                volumeDistr = const(V)), 
                                "signal")
    
    alpha = 0.065
    
    trend_follower = trader.SASM(book_A, 
                                 strategy.TrendFollower(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                                 label="trendfollower")

    trend_follower_ex = trader.SASM(book_A, 
                                    strategy.TrendFollowerEx(
                                       average=mathutils.ewma(alpha),
                                       volumeDistr = const(V)),
                                    label="trendfollower_ex")
    
    price_graph += [assetPrice,
                    avg(assetPrice, alpha),
                    linear_signal,
                    observable.VolumeTraded(signal_trader), 
                    observable.VolumeTraded(trend_follower),
                    observable.VolumeTraded(trend_follower_ex)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(trend_follower),
                  observable.PnL(trend_follower)]
    eff_graph += [observable.Efficiency(trend_follower_ex),
                  observable.PnL(trend_follower_ex)]
    
    return [lp_A, signal_trader, trend_follower, trend_follower_ex], [price_graph, eff_graph]

if __name__ == '__main__':
    run("trend_follower", TrendFollower)