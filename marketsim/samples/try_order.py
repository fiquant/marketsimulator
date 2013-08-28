import sys
sys.path.append(r'../..')

from marketsim import (Side, mathutils, parts, signal, strategy, observable, ops, order, event)
from common import expose, Interlacing, InterlacingSide

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
                        event.Every(ops.constant(1.)),
                        order.factory.sideprice.Limit(volume=const(35))), 
                    "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Market(volume = const(1)),
                            linear_signal), 
                         "signalmarket"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.FloatingPrice(const(100),
                                order.factory.side_price.Limit(const(1))),
                            linear_signal), 
                         "signalfloating"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Iceberg(const(1),
                                order.factory.side.Limit(const(110), const(3))),
                            linear_signal), 
                         "signaliceberg"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.ImmediateOrCancel(
                                order.factory.side.Limit(const(120), const(1))),
                            linear_signal), 
                         "signalioc"), 
  
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Peg(
                                order.factory.side_price.Limit(const(1))),
                            linear_signal), 
                         "signalpeg"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.StopLoss(
                                const(0.1),
                                order.factory.side.Market(
                                    volume = const(1))),
                            linear_signal), 
                         "signalstoploss"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Limit(
                                price = midPrice, 
                                volume = const(1)),
                            linear_signal), 
                         "signallimit"), 
    
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.factory.side.Limit(
                                price = const(120), 
                                volume = const(1)),
                            Interlacing()),
                         "noiselimitmarket"), 
    
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.factory.side.WithExpiry(
                                const(10),
                                order.factory.side.Limit(
                                    price = const(120), 
                                    volume = const(1))),
                            Interlacing()),
                         "noiselimitexpiry"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Iceberg(
                                const(1),
                                order.factory.side.Peg(
                                    order.factory.side_price.Limit(const(1)))),
                            Interlacing()), 
                         "icebergpeg"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Peg(
                                order.factory.side_price.Iceberg(const(1),
                                    order.factory.side_price.Limit(const(3)))),
                            Interlacing()), 
                         "pegiceberg"), 
  
#         ctx.makeTrader_A(strategy.Generic(
#                                 order.factory.Peg(
#                                     order.meta._iceberg.Price_Factory(
#                                         const(1),
#                                         order._limit.Price_Factory(
#                                             side = InterlacingSide(),
#                                             volume = const(10)))),
#                             event.Every(const(10))), 
#                          "pegiceberg"), 
#    
#         ctx.makeTrader_A(strategy.Generic(
#                             order.factory.Peg(
#                                 order._limit.Price_Factory(
#                                     side = InterlacingSide(),
#                                     volume = const(10))),
#                             event.Every(const(10))), 
#                          "noise_peg"), 
#   
#         ctx.makeTrader_A(strategy.Generic(
#                             order.factory.WithExpiry(
#                                 ops.constant(10),
#                                 order.factory.Peg(
#                                     order.meta._iceberg.Price_Factory(
#                                         const(1),
#                                         order._limit.Price_Factory(
#                                             side = InterlacingSide(),
#                                             volume = const(10))))),
#                             event.Every(const(10))), 
#                          "pegicebergwithexpiry"), 
#    
#         ctx.makeTrader_A(strategy.Generic(
#                             order.factory.WithExpiry(
#                                 ops.constant(0.1),
#                                 order.factory.Iceberg(
#                                     const(1),
#                                     order.factory.Peg(
#                                         order._limit.Price_Factory(
#                                             side = InterlacingSide(),
#                                             volume = const(10))))),
#                             event.Every(const(10))), 
#                          "icebergpeg"), 
#    
#         ctx.makeTrader_A(strategy.Generic(
#                             order.factory.WithExpiry(
#                                 ops.constant(0.1),
#                                 order.factory.Peg(
#                                     order._limit.Price_Factory(
#                                         side = InterlacingSide(),
#                                         volume = const(10)))),
#                             event.Every(const(10))), 
#                          "noise_pegexpiry"), 
    ]    
