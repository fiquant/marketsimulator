import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, orderbook, observable, mathutils)
from common import expose, Constant

@expose("Relative strength index", __name__)
def RSI(ctx):

    const = mathutils.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    one = mathutils.constant(1)
    
    rsi = observable.OnEveryDt(one.value, 
                         observable.Fold(
                            observable.Price(
                                orderbook.OfTrader()), 
                            mathutils.rsi()))
    
    threshold = 30
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myRsi = lambda: [(rsi, demo)]
    
    alpha = 1./14
    
    myRsiBis = lambda: [(observable.OnEveryDt(1, 
                            observable.RSI(orderbook.OfTrader(), 
                                           0, 
                                           alpha)), 
                         demo)]
    
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(4)), "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(linear_signal), "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.RSIbis(alpha = alpha,
                                         timeframe = 0,
                                         threshold=threshold, 
                                         volumeDistr=one, 
                                         creationIntervalDistr=one),
                         "rsi_bis",
                         myVolume() + myRsiBis()), 
            
        ctx.makeTrader_A(strategy.RSIEx(alpha = alpha,
                                        threshold=threshold, 
                                        volumeDistr=one, 
                                        creationIntervalDistr=one), 
                         "rsi_ex", (myVolume() + myRsi() + 
                                    Constant(threshold, demo) + 
                                    Constant(100-threshold, demo)))
    ]    
