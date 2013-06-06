import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TrendFollower(ctx):

    V = 1
    alpha = 0.15
    ctx.volumeStep = 30

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    
    return [
            ctx.makeTrader_A(strategy.LiquidityProvider(
                                volumeDistr=const(V*8), 
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=const(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.Signal(linear_signal, 
                                             volumeDistr = const(V*4)), 
                            "signal", 
                            [
                             (linear_signal, ctx.amount_graph),
                             (observable.avg(observable.Price(ctx.book_A), alpha), demo)
                            ]),
    
            ctx.makeTrader_A(strategy.TrendFollower(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                             "trendfollower", 
                            [
                             (observable.VolumeTraded(trader.SASM_Proxy()), demo)
                            ]),
            ctx.makeTrader_A(strategy.TrendFollowerEx(
                                       average=mathutils.ewma(alpha),
                                       volumeDistr = const(V)),
                             "trendfollower_ex", 
                            [
                             (observable.VolumeTraded(trader.SASM_Proxy()), demo)
                            ])
    ]
    

if __name__ == '__main__':
    run("trend_follower", TrendFollower)