import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, trader, orderbook, ops,
                       timeserie, scheduler, observable, veusz, mathutils)

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
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(10)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(linear_signal,
                                         volumeDistr=const(3)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(strategy.TwoAverages(ewma_alpha1 = alpha_slow, 
                                              ewma_alpha2 = alpha_fast,
                                              creationIntervalDistr = const(1.),
                                              volumeDistr           = const(1.)), 
                        'avg+', 
                        myAverage(alpha_slow) + myAverage(alpha_fast) + myVolume()),

        ctx.makeTrader_A(strategy.TwoAverages(ewma_alpha2 = alpha_slow, 
                                              ewma_alpha1 = alpha_fast,
                                              creationIntervalDistr = const(1.),
                                              volumeDistr           = const(1.)), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAveragesEx(ewma_alpha1 = alpha_slow, 
                                                ewma_alpha2 = alpha_fast,
                                                creationIntervalDistr = const(1.),
                                                volumeDistr           = const(1.)), 
                         'avg_ex+',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAveragesEx(ewma_alpha2 = alpha_slow, 
                                                ewma_alpha1 = alpha_fast,
                                                creationIntervalDistr = const(1.),
                                                volumeDistr           = const(1.)), 
                         'avg_ex-',
                         myVolume())
    ]
