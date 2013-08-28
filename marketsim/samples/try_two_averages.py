import sys
sys.path.append(r'../..')

from marketsim import (parts, signal, strategy, trader, orderbook, ops, order,
                       timeserie, observable, veusz, mathutils)

const = ops.constant

from common import expose

@expose("Two Averages", __name__)
def TwoAverages(ctx):

    ctx.volumeStep = 30
    
    alpha_slow = 0.015
    alpha_fast = 0.15

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    return [
        ctx.makeTrader_A(
                strategy.LiquidityProvider(
                    order.factory.sideprice.Limit(volume=const(10))),
                "liquidity"),

        ctx.makeTrader_A(strategy.Signal(order.factory.side.Market(volume = const(3)),
                                         linear_signal), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(strategy.v0.TwoAverages(ewma_alpha1 = alpha_slow, 
                                              ewma_alpha2 = alpha_fast,
                                              creationIntervalDistr = const(1.),
                                              volumeDistr           = const(1.)), 
                        'avg+', 
                        myAverage(alpha_slow) + myAverage(alpha_fast) + myVolume()),

        ctx.makeTrader_A(strategy.v0.TwoAverages(ewma_alpha2 = alpha_slow, 
                                              ewma_alpha1 = alpha_fast,
                                              creationIntervalDistr = const(1.),
                                              volumeDistr           = const(1.)), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAverages(
                            order.factory.side.Market(volume = const(1.)),
                            alpha_slow, 
                            alpha_fast,
                            creationIntervalDistr = const(1.)),
                         'avg_ex+',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAverages(
                            order.factory.side.Market(volume = const(1.)),
                            alpha_fast, 
                            alpha_slow,
                            creationIntervalDistr = const(1.)),
                         'avg_ex-',
                         myVolume()),
    ]
