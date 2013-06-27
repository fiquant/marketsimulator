import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, orderbook, observable, mathutils)
from common import expose, Constant

@expose("Desired position", __name__)
def DesiredPosition(ctx):

    const = mathutils.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(4)), "liquidity"),
        
        ctx.makeTrader_A(strategy.DesiredPosition(linear_signal), "desired_position", 
                         [(linear_signal, ctx.amount_graph)]),
    ]    
