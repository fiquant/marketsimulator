import sys
sys.path.append(r'../..')

from marketsim import (event, order, signal, strategy, orderbook, observable, mathutils, ops)
from common import expose, Constant

@expose("Relative strength index", __name__)
def RSI(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    one = const(1)
    
    rsi = observable.OnEveryDt(one.value, 
                         observable.Fold(
                            observable.MidPrice(
                                orderbook.OfTrader()), 
                            mathutils.rsi()))
    
    threshold = 30
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myRsi = lambda: [(rsi, demo)]
    
    alpha = 1./14
    
    myRsiBis = lambda: [(observable.OnEveryDt(1, 
                            observable.RSI(orderbook.OfTrader(), 
                                           1, 
                                           alpha)), 
                         demo)]
    
    return [
        ctx.makeTrader_A(
                strategy.LiquidityProvider(
                        event.Every(ops.constant(1.)),
                        order.factory.sideprice.Limit(volume=const(4))),
                "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(event.Every(ops.constant(1.)),
                                         order.factory.side.Market(), 
                                         linear_signal), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.RSIbis(event.Every(ops.constant(1.)),
                                         order.factory.side.Market(one),
                                         alpha = alpha,
                                         timeframe = 1,
                                         threshold=threshold),
                         "rsi_bis",
                         myVolume() + myRsiBis()), 
            
        ctx.makeTrader_A(strategy.v0.RSIEx(alpha = alpha,
                                        threshold=threshold, 
                                        volumeDistr=one, 
                                        creationIntervalDistr=one), 
                         "rsi_ex", (myVolume() + myRsi() + 
                                    Constant(threshold, demo) + 
                                    Constant(100-threshold, demo)))
    ]    
