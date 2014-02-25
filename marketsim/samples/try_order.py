import sys
sys.path.append(r'../..')

from marketsim._pub import (math, strategy, order, event, const, constant, orderbook)
from common import expose, Interlacing

@expose("Various Orders", __name__)
def Orders(ctx):

    linear_signal = math.RandomWalk(initialValue=20,
                                      deltaDistr=const(-.1), 
                                      name="20-0.1t")
    
    midPrice = orderbook.MidPrice(ctx.book_A)

    return [
        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(const(1.)),
                        order.side_price.Limit(volume=const(35))),
                    "liquidity"),
        
        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(const(100.)),
                        order.side_price.StopLoss(const(0.1),
                            order.side_price.Limit(volume=const(5)))),
                    "liquidity stoploss"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(const(10.)),
                        order.side_price.Iceberg(
                            order.side_price.Limit(volume=const(5)), const(1))),
                    "liquidity iceberg"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(const(10.)),
                        order.side_price.WithExpiry(const(5),
                            order.side_price.Limit(volume=const(5)))),
                    "liquidity expiry"),

        ctx.makeTrader_A(
                    strategy.LiquidityProvider(
                        event.Every(const(10.)),
                        order.side_price.WithExpiry(const(5),
                            order.side_price.Iceberg(
                                order.side_price.Limit(volume=const(15)), const(1)))),
                    "liquidity iceberg expiry"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(1.)),
                            order.side.Market(volume = const(1)),
                            linear_signal),
                         "signal market"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(1.)),
                            order.side.FloatingPrice(
                                order.side.price.Limit(const(1)),
                                const(100.)),
                            linear_signal),
                         "signal floating"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(1.)),
                            order.side.Iceberg(
                                order.side.Limit(const(110), const(3)), const(1)),
                            linear_signal),
                         "signal iceberg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(1.)),
                            order.side.ImmediateOrCancel(
                                order.side.Limit(const(120), const(1))),
                            linear_signal),
                         "signal ioc"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10.)),
                            order.side.Peg(
                                order.side.price.Limit(const(1))),
                            linear_signal), 
                         "signal peg"), 
   
        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(1.)),
                            order.side.StopLoss(
                                const(0.1),
                                order.side.Market(
                                    volume = const(1))),
                            linear_signal),
                         "signal stoploss"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10.)),
                            order.side.Limit(
                                price = midPrice,
                                volume = const(1)),
                            linear_signal),
                         "signal limit"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.side.Limit(
                                price = const(120),
                                volume = const(1)),
                            Interlacing()),
                         "noise limit"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10)),
                            order.side.WithExpiry(
                                const(10),
                                order.side.Limit(
                                    price = const(120),
                                    volume = const(1))),
                            Interlacing()),
                         "noise expiry"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10.)),
                            order.side.Iceberg(
                                order.side.Peg(
                                    order.side.price.Limit(const(1))), const(1)),
                            Interlacing()),
                         "iceberg peg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(const(10.)),
                            order.side.Peg(
                                order.side.price.Iceberg(
                                    order.side.price.Limit(const(3)), const(1))),
                            Interlacing()),
                         "peg iceberg"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(constant(3.)),
                            order.side.WithExpiry(
                                constant(3.),
                                order.side.Peg(
                                    order.side.price.Iceberg(
                                        order.side.price.Limit(const(3)), const(1)))),
                            Interlacing()),
                         "peg iceberg expiry"),

        ctx.makeTrader_A(strategy.Signal(
                            event.Every(constant(10.)),
                            order.side.WithExpiry(
                                constant(10.),
                                order.side.Iceberg(
                                    order.side.Peg(
                                        order.side.price.Limit(const(1))), const(1))),
                            Interlacing()),
                         "iceberg peg expiry"),
    ]
