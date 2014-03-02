import sys
sys.path.append(r'../..')

from marketsim._pub import (event, strategy, order, constant, math)
from common import expose

@expose("Signal", __name__)
def Signal(ctx):

    const = constant
    linear_signal = math.RandomWalk(initialValue=20,
                                      deltaDistr=const(-.1), 
                                      name="20-0.1t")

    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(
                event.Every(constant(1.)),
                order.side_price.Limit(volume=const(5))),
            "liquidity"),
        
        ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = const(1))),
                         "signal_ex"), 
    ]    
