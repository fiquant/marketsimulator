import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils, ops)

const = ops.constant

from common import expose

@expose("Trade-If-Profitable", __name__)
def TradeIfProfitable(ctx):

    ctx.volumeStep = 30
    
    slow_alpha = 0.015
    fast_alpha = 0.15

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.MidPrice(orderbook.OfTrader()), alpha), demo)]
    
    avg_plus = strategy.TwoAverages(ewma_alpha1 = slow_alpha, 
                                    ewma_alpha2 = fast_alpha,
                                    creationIntervalDistr = ops.constant(1.),
                                    volumeDistr           = ops.constant(1.))
    
    avg_minus = strategy.TwoAverages(ewma_alpha2 = slow_alpha, 
                                     ewma_alpha1 = fast_alpha,
                                     creationIntervalDistr = ops.constant(1.),
                                     volumeDistr           = ops.constant(1.))
    
    avg_plus_opt = strategy.TradeIfProfitable(avg_plus)
    avg_minus_opt = strategy.TradeIfProfitable(avg_minus)

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(45)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(linear_signal,
                                         volumeDistr=const(20)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(avg_plus, 
                        'avg+', 
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),

        ctx.makeTrader_A(avg_minus, 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_opt, 
                         'avg+ opt',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_opt, 
                         'avg- opt',
                         myVolume()),
    ]
