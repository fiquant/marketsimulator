import sys
sys.path.append(r'../..')

from marketsim import (mathutils, parts, signal, strategy, observable, ops, order, scheduler)
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
                            order.factory.StopLoss(
                                side = parts.side.Signal(linear_signal), 
                                volume = const(1),
                                maxloss = const(0.1))), 
                         "signalstoploss"), 

        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = parts.side.Signal(linear_signal), 
                                price = midPrice, 
                                volume = const(1))), 
                         "signallimit"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = parts.side.Random(), 
                                price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                volume = const(1)),
                            scheduler.Timer(const(1))), 
                         "noiselimitmarket"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                const(100), 
                                order.factory.Limit(
                                    side = parts.side.Random(), 
                                    price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                    volume = const(1))),
                            scheduler.Timer(const(1))), 
                         "noiselimitexpiry"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.IcebergLimit(
                                side = parts.side.Random(), 
                                price = midPrice + mathutils.rnd.uniform(-5, +5), 
                                volume = const(100),
                                lotsize = const(1)),
                            scheduler.Timer(const(100))), 
                         "noiseiceberglimit"), 
 
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.FixedBudget(
                                side = parts.side.Signal(linear_signal), 
                                budget = const(450))), 
                         "signalfixedbudget"), 
          
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.AlwaysBestLimit(
                                side = parts.side.Random(),
                                volume = const(100)),
                            scheduler.Timer(const(1))), 
                         "noise_alwaysbest"), 
    ]    
