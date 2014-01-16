import sys
sys.path.append(r'../..')

from marketsim import (parts, signal, strategy, trader, orderbook, order, ops,
                       event, timeserie,  observable, veusz, mathutils)

const = ops.constant

from common import expose

@expose("Mean Reversion", __name__)
def MeanReversion(ctx):

    ctx.volumeStep = 40

    alpha = 0.015
    V = 1
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      name="200-t")

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    myPrice = lambda: [(observable.MidPrice(orderbook.OfTrader()), demo)]

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                        orderFactory = order.factory.sideprice.WithExpiry(
                            ops.constant(10),
                            order.factory.sideprice.Limit(volume=ops.constant(V*20)))),
                       label="liquidity"),
    
        ctx.makeTrader_A(strategy.Signal(
                                event.Every(ops.constant(1.)),
                                order.factory.side.Market(volume = const(V*3)),
                                linear_signal), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
     
        ctx.makeTrader_A(
                strategy.MeanReversion(
                    event.Every(ops.constant(1.)),
                    order.factory.side.Market(volume = const(V)),
                    alpha),
                 "meanreversion_ex", 
                 myVolume()),
    ]    
