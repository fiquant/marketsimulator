import sys
sys.path.append(r'../..')

from marketsim import (order, parts, signal, strategy, trader, orderbook, 
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
    
    def cross(alpha1, alpha2):
        return strategy.Generic(
                    order.factory.Market(
                        side = parts.side.TwoAverages(alpha1, alpha2),
                        volume = const(1.)),
                    scheduler.Timer(const(1.)))
    
    
    avg_plus_virt = strategy.TradeIfProfitable(cross(slow_alpha, fast_alpha), strategy.adaptive.virtualMarket)
    avg_minus_virt = strategy.TradeIfProfitable(cross(fast_alpha, slow_alpha), strategy.adaptive.virtualMarket)

    avg_plus_real = strategy.TradeIfProfitable(cross(slow_alpha, fast_alpha), strategy.adaptive.account)
    avg_minus_real = strategy.TradeIfProfitable(cross(fast_alpha, slow_alpha), strategy.adaptive.account)

    return [
        ctx.makeTrader_A(strategy.v0.LiquidityProvider(volumeDistr=const(45)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.v0.Signal(linear_signal,
                                         volumeDistr=const(20)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(cross(slow_alpha, fast_alpha), 
                        'avg+', 
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),
 
        ctx.makeTrader_A(cross(fast_alpha, slow_alpha), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_virt, 
                         'avg+ virt',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_virt, 
                         'avg- virt',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_real, 
                         'avg+ real',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_real, 
                         'avg- real',
                         myVolume()),
    ]
