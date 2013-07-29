import sys
sys.path.append(r'../..')

from marketsim import (signal, strategy, observable, ops, order)
from common import expose

@expose("Various Orders", __name__)
def Signal(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    midPrice = observable.MidPrice(ctx.book_A)

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(5)), "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal2Ex(linear_signal, 
                                            order.factory.Side_Market(const(1))), 
                         "signalmarket"), 
        
        ctx.makeTrader_A(strategy.Signal2Ex(linear_signal, 
                                            order.factory.Side_Limit(
                                                price = midPrice, 
                                                volume = const(1)
                                            )), 
                         "signallimit"), 

        ctx.makeTrader_A(strategy.Signal2Ex(linear_signal, 
                                            order.factory.Side_FixedBudget(
                                                budget = const(1450), 
                                            )), 
                         "signalfixedbudget"), 
        
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.AlwaysBestLimit(
                                side = strategy.side.Random(),
                                volume = const(20))), 
                         "noise_alwaysbest"), 
        
        ctx.makeTrader_A(strategy.SignalEx(linear_signal, 
                                           volumeDistr=const(1), 
                                           orderFactory=order.StopLossFactory()), 
                         "stoploss")
    ]    
