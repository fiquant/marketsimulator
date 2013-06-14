import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

const = mathutils.constant

from common import expose

@expose("Trend Follower", __name__)
def TrendFollower(ctx):

    V = 1
    alpha = 0.015
    ctx.volumeStep = 30

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.Price(orderbook.OfTrader()), alpha), demo)]
    
    return [
            ctx.makeTrader_A(strategy.LiquidityProvider(
                                volumeDistr=const(V*8), 
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=const(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.Signal(linear_signal, 
                                             volumeDistr = const(V*2)), 
                            "signal", 
                            [
                             (linear_signal, ctx.amount_graph)
                            ]),
    
            ctx.makeTrader_A(strategy.TrendFollower(
                                    creationIntervalDistr = mathutils.constant(1.),
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                             "trendfollower", 
                             myVolume() + myAverage(alpha)),
            
            ctx.makeTrader_A(strategy.TrendFollowerEx(
                                       creationIntervalDistr = mathutils.constant(1.),
                                       average=mathutils.ewma(alpha),
                                       volumeDistr = const(V)),
                             "trendfollower_ex",
                             myVolume())
    ]
