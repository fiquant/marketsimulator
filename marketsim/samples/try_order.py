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
        
        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(ops.constant(100.)),
                        order.factory.sideprice.StopLoss(const(0.1),
                            order.factory.sideprice.Limit(volume=const(5)))),
                    "liquidity stoploss"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(ops.constant(10.)),
                        order.factory.sideprice.Iceberg(const(1),
                            order.factory.sideprice.Limit(volume=const(5)))),
                    "liquidity iceberg"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(ops.constant(10.)),
                        order.factory.sideprice.WithExpiry(const(5),
                            order.factory.sideprice.Limit(volume=const(5)))),
                    "liquidity expiry"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(ops.constant(10.)),
                        order.factory.sideprice.WithExpiry(const(5),
                            order.factory.sideprice.Iceberg(const(1),
                                order.factory.sideprice.Limit(volume=const(15))))),
                    "liquidity iceberg expiry"),

#         ctx.makeTrader_A(
#                     strategy.LiquidityProvider(
#                         event.Every(ops.constant(100.)),
#                         order.factory.sideprice.StopLoss(const(0.1),
#                             order.factory.sideprice.WithExpiry(const(5),
#                                 order.factory.sideprice.Iceberg(const(1),
#                                     order.factory.sideprice.Limit(volume=const(15)))))), 
#                     "liquidity iceberg expiry stoploss"),
        
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Market(volume = const(1)),
                            linear_signal),
                         "signal market"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.FloatingPrice(const(100),
                                order.factory.side_price.Limit(const(1))),
                            linear_signal),
                         "signal floating"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.Iceberg(const(1),
                                order.factory.side.Limit(const(110), const(3))),
                            linear_signal),
                         "signal iceberg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.ImmediateOrCancel(
                                order.factory.side.Limit(const(120), const(1))),
                            linear_signal),
                         "signal ioc"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Peg(
                                order.factory.side_price.Limit(const(1))),
                            linear_signal), 
                         "signal peg"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(1.)),
                            order.factory.side.StopLoss(
                                const(0.1),
                                order.factory.side.Market(
                                    volume = const(1))),
                            linear_signal),
                         "signal stoploss"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Limit(
                                price = midPrice,
                                volume = const(1)),
                            linear_signal),
                         "signal limit"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.factory.side.Limit(
                                price = const(120),
                                volume = const(1)),
                            Interlacing()),
                         "noise limit"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.factory.side.WithExpiry(
                                const(10),
                                order.factory.side.Limit(
                                    price = const(120),
                                    volume = const(1))),
                            Interlacing()),
                         "noise expiry"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Iceberg(
                                const(1),
                                order.factory.side.Peg(
                                    order.factory.side_price.Limit(const(1)))),
                            Interlacing()),
                         "iceberg peg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.Peg(
                                order.factory.side_price.Iceberg(const(1),
                                    order.factory.side_price.Limit(const(3)))),
                            Interlacing()),
                         "peg iceberg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(3.)),
                            order.factory.side.WithExpiry(
                                ops.constant(3.),
                                order.factory.side.Peg(
                                    order.factory.side_price.Iceberg(const(1),
                                        order.factory.side_price.Limit(const(3))))),
                            Interlacing()),
                         "peg iceberg expiry"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(ops.constant(10.)),
                            order.factory.side.WithExpiry(
                                ops.constant(10.),
                                order.factory.side.Iceberg(
                                    const(1),
                                    order.factory.side.Peg(
                                        order.factory.side_price.Limit(const(1))))),
                            Interlacing()),
                         "iceberg peg expiry"),
    ]
