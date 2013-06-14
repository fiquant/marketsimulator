import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, observable, mathutils)
from common import expose

@expose("Signal", __name__)
def Signal(ctx):

    const = mathutils.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(4)), "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(linear_signal), "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.SignalEx(linear_signal), "signal_ex")
    ]    
