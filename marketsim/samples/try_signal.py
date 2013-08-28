import sys
sys.path.append(r'../..')

from marketsim import (event, parts, signal, strategy, observable, ops, order)
from common import expose

@expose("Signal", __name__)
def Signal(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")

    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(
                event.Every(ops.constant(1.)),
                order.factory.sideprice.Limit(volume=const(5))),
            "liquidity"),
        
        ctx.makeTrader_A(strategy.v0.Signal(linear_signal, 
                                         volumeDistr=const(1)), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Market(volume = const(1)),
                            linear_signal),
                         "signal_ex"), 
    ]    
