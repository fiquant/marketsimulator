import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, trader, orderbook, order, ops,
                       timeserie, scheduler, observable, veusz, mathutils)

const = ops.constant

from common import expose

@expose("Mean Reversion", __name__)
def MeanReversion(ctx):

    ctx.volumeStep = 40

    alpha = 0.015
    V = 1
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    myPrice = lambda: [(observable.MidPrice(orderbook.OfTrader()), demo)]

    return [
        ctx.makeTrader_A( 
                       strategy.LiquidityProvider(
                            volumeDistr=const(V*20), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))),
                       label="liquidity"),
    
        ctx.makeTrader_A(strategy.Signal(linear_signal, 
                                         volumeDistr = const(V*3)), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
     
        ctx.makeTrader_A(strategy.MeanReversion(
                                ewma_alpha=(alpha),
                                creationIntervalDistr = ops.constant(1.),
                                volumeDistr = const(V)),
                         "meanreversion", 
                         myVolume() + myAverage() + myPrice()),
     
        ctx.makeTrader_A(strategy.MeanReversionEx(
                                ewma_alpha=(alpha),
                                creationIntervalDistr = ops.constant(1.),
                                volumeDistr = const(V)),
                         "meanreversion_ex", 
                         myVolume())
    ]    
