import sys
sys.path.append(r'../..')

from marketsim import (order, parts, signal, strategy, trader, orderbook, 
                       timeserie, observable, veusz, mathutils, ops)

const = ops.constant

from common import expose

@expose("Choose-The-Best", __name__)
def ChooseTheBest(ctx):

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
        return strategy.TwoAverages(
                    order.factory.side.Market(volume = const(1.)),
                    alpha1, alpha2,
                    creationIntervalDistr = const(1.))
        
    def strategies():
        return [cross(slow_alpha, fast_alpha), cross(fast_alpha, slow_alpha)]
        
    return [
        ctx.makeTrader_A(strategy.v0.LiquidityProvider(volumeDistr=const(45)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(order.factory.side.Market(volume = const(20)),
                                         linear_signal), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(cross(slow_alpha, fast_alpha), 
                        'avg+', 
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),
 
        ctx.makeTrader_A(cross(fast_alpha, slow_alpha), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(strategy.ChooseTheBest(
                                    strategies(), 
                                    strategy.adaptive.virtualMarket), 
                         'best virt',
                         myVolume()),

        ctx.makeTrader_A(strategy.ChooseTheBest(
                                    strategies(), 
                                    strategy.adaptive.account), 
                         'best real',
                         myVolume()),
    ]
