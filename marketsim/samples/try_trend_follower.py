import sys
sys.path.append(r'../..')

from marketsim import (parts, signal, strategy, trader, orderbook, order, ops,
                       event, timeserie, observable, veusz, mathutils)

const = ops.constant

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
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    return [
            ctx.makeTrader_A(strategy.v0.LiquidityProvider(
                                volumeDistr=const(V*8), 
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=const(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.Signal(event.Every(ops.constant(1.)),
                                             order.factory.side.Market(const(V*2)),
                                             linear_signal), 
                            "signal", 
                            [
                             (linear_signal, ctx.amount_graph)
                            ]),
    
            ctx.makeTrader_A(strategy.v0.TrendFollower(
                                    creationIntervalDistr = const(1.),
                                    ewma_alpha = (alpha),
                                    volumeDistr = const(V)),
                             "trendfollower", 
                             myVolume() + myAverage(alpha)),
            
            ctx.makeTrader_A(strategy.TrendFollower(
                                event.Every(ops.constant(1.)),
                                order.factory.side.Market(volume = const(V)),
                                alpha),
                             "trendfollower_ex",
                             myVolume()), 
    ]
