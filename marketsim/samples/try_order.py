import sys
sys.path.append(r'../..')

from marketsim import (Side, mathutils, parts, signal, strategy, observable, ops, order, scheduler)
from common import expose, InterlacingSide

@expose("Various Orders", __name__)
def Orders(ctx):

    const = ops.constant
    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")
    
    midPrice = observable.MidPrice(ctx.book_A)

    return [
        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        order.factory.sideprice.Limit(volume=const(25))), 
                    "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.Market(volume = const(1)),
                            linear_signal), 
                         "signalmarket"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.FloatingPrice(const(100),
                                order.factory.side_price.Limit(const(1))),
                            linear_signal), 
                         "signalfloating"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.Iceberg(const(1),
                                order.factory.side.Limit(const(110), const(3))),
                            linear_signal), 
                         "signaliceberg"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.ImmediateOrCancel(
                                order.factory.side.Limit(const(120), const(1))),
                            linear_signal), 
                         "signalioc"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.Peg(
                                order.factory.side_price.Limit(const(1))),
                            linear_signal), 
                         "signalpeg"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.StopLoss(
                                const(0.1),
                                order.factory.side.Market(
                                    volume = const(1))),
                            linear_signal), 
                         "signalstoploss"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.Limit(
                                price = midPrice, 
                                volume = const(1)),
                            linear_signal), 
                         "signallimit"), 
    
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Limit(
                                side = InterlacingSide(), 
                                price = midPrice, 
                                volume = const(1)),
                            scheduler.Timer(const(1))), 
                         "noiselimitmarket"), 
    
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                const(100), 
                                order.factory.Limit(
                                    side = InterlacingSide(), 
                                    price = midPrice, 
                                    volume = const(1))),
                            scheduler.Timer(const(1))), 
                         "noiselimitexpiry"), 
   
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Iceberg(
                                const(1),
                                order.factory.Limit(
                                    side = InterlacingSide(),
                                    price = midPrice, 
                                    volume = const(10))),
                            scheduler.Timer(const(10))), 
                         "noiseiceberglimit"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            order.factory.side.FixedBudget(budget = const(450)),
                            linear_signal), 
                         "signalfixedbudget"), 
             
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Iceberg(
                                const(1),
                                order.factory.Peg(
                                    order._limit.Price_Factory(
                                        side = InterlacingSide(),
                                        volume = const(10)))),
                            scheduler.Timer(const(10))), 
                         "icebergpeg"), 
   
        ctx.makeTrader_A(strategy.Generic(
                                order.factory.Peg(
                                    order.meta._iceberg.Price_Factory(
                                        const(1),
                                        order._limit.Price_Factory(
                                            side = InterlacingSide(),
                                            volume = const(10)))),
                            scheduler.Timer(const(10))), 
                         "pegiceberg"), 
   
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.Peg(
                                order._limit.Price_Factory(
                                    side = InterlacingSide(),
                                    volume = const(10))),
                            scheduler.Timer(const(10))), 
                         "noise_peg"), 
  
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                ops.constant(10),
                                order.factory.Peg(
                                    order.meta._iceberg.Price_Factory(
                                        const(1),
                                        order._limit.Price_Factory(
                                            side = InterlacingSide(),
                                            volume = const(10))))),
                            scheduler.Timer(const(10))), 
                         "pegicebergwithexpiry"), 
   
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                ops.constant(0.1),
                                order.factory.Iceberg(
                                    const(1),
                                    order.factory.Peg(
                                        order._limit.Price_Factory(
                                            side = InterlacingSide(),
                                            volume = const(10))))),
                            scheduler.Timer(const(10))), 
                         "icebergpeg"), 
   
        ctx.makeTrader_A(strategy.Generic(
                            order.factory.WithExpiry(
                                ops.constant(0.1),
                                order.factory.Peg(
                                    order._limit.Price_Factory(
                                        side = InterlacingSide(),
                                        volume = const(10)))),
                            scheduler.Timer(const(10))), 
                         "noise_pegexpiry"), 
    ]    
