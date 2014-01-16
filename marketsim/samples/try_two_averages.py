import sys
sys.path.append(r'../..')

from marketsim import (parts, signal, strategy, trader, orderbook, ops, order,
                       event, timeserie, observable, veusz, mathutils)

const = ops.constant

from common import expose

@expose("Two Averages", __name__)
def TwoAverages(ctx):

    ctx.volumeStep = 30
    
    alpha_slow = 0.015
    alpha_fast = 0.15

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      name="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    return [
        ctx.makeTrader_A(
                strategy.LiquidityProvider(
                    event.Every(ops.constant(1.)),
                    order.factory.sideprice.Limit(volume=const(10))),
                "liquidity"),

        ctx.makeTrader_A(strategy.Signal(event.Every(ops.constant(1.)),
                                         order.factory.side.Market(volume = const(3)),
                                         linear_signal), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(strategy.TwoAverages(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Market(volume = const(1.)),
                            alpha_slow, 
                            alpha_fast),
                         'avg_ex+',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAverages(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Market(volume = const(1.)),
                            alpha_fast, 
                            alpha_slow),
                         'avg_ex-',
                         myVolume()),
    ]
