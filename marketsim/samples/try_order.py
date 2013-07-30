import sys
sys.path.append(r'../..')

from marketsim import (parts, signal, strategy, observable, ops, order, scheduler)
from common import expose

@expose("Various Orders", __name__)
def Orders(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    midPrice = observable.MidPrice(ctx.book_A)

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(5)), "liquidity"),
        
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Market(
                                side = parts.side.Signal(linear_signal), 
                                volume = const(1))), 
                         "signalmarket"), 

        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = parts.side.Signal(linear_signal), 
                                price = midPrice, 
                                volume = const(1))), 
                         "signallimit"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.FixedBudget(
                                side = parts.side.Signal(linear_signal), 
                                budget = const(450))), 
                         "signalfixedbudget"), 
         
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.AlwaysBestLimit(
                                side = parts.side.Random(),
                                volume = const(1)),
                            scheduler.Timer(const(100))), 
                         "noise_alwaysbest"), 
    ]    
