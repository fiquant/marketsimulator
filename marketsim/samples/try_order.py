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
                    strategy.price.LiquidityProvider()
                                  .Strategy(
                                        event.Every(const(1.)),
                                        order.side_price.Limit(volume=const(35))),
                    "liquidity"),

        ctx.makeTrader_A(
                    strategy.price.LiquidityProvider()
                                  .Strategy(
                                        event.Every(const(100.)),
                                        order.side_price.Limit(volume=const(5))
                                             .sideprice_StopLoss(const(0.1))),
                    "liquidity stoploss"),

        ctx.makeTrader_A(
                    strategy.price.LiquidityProvider()
                                  .Strategy(
                                        event.Every(const(10.)),
                                        order.side_price.Limit(volume=const(5))
                                             .sideprice_Iceberg(const(1))),
                    "liquidity iceberg"),

        ctx.makeTrader_A(
                    strategy.price.LiquidityProvider()
                                  .Strategy(
                                        event.Every(const(10.)),
                                        order.side_price.Limit(volume=const(5))
                                             .sideprice_WithExpiry(const(5))),
                    "liquidity expiry"),

        ctx.makeTrader_A(
                    strategy.price.LiquidityProvider()
                                  .Strategy(
                                        event.Every(const(10.)),
                                        order.side_price.Limit(volume=const(15))
                                             .sideprice_Iceberg(const(1))
                                             .sideprice_WithExpiry(const(5))),
                    "liquidity iceberg expiry"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(1.)),
                            order.side.Market(volume = const(1))),
                         "signal market"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(1.)),
                            order.side.price.Limit(const(1))
                                 .side_FloatingPrice(const(100))),
                         "signal floating"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(1.)),
                            order.side.Limit(const(110), const(3))
                                 .side_Iceberg(const(1))),
                         "signal iceberg"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(1.)),
                            order.side.Limit(const(120), const(1))
                                 .side_ImmediateOrCancel),
                         "signal ioc"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(10.)),
                            order.side.price.Limit(const(1))
                                 .side_Peg),
                         "signal peg"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(1.)),
                            order.side.Market(volume = const(1))
                                 .side_StopLoss(const(0.1))),
                         "signal stoploss"),


        ctx.makeTrader_A(strategy.side.Signal(linear_signal).Strategy(
                            event.Every(const(10.)),
                            order.side.Limit(
                                price = midPrice,
                                volume = const(1))),
                         "signal limit"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(const(10)),
                            order.side.Limit(
                                price = const(120),
                                volume = const(1))),
                         "noise limit"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(const(10)),
                            order.side.Limit(price = const(120),
                                             volume = const(1))
                                 .side_WithExpiry(const(10))),
                         "noise expiry"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(const(10.)),
                                    order.side.price.Limit(const(1))
                                        .side_Peg
                                        .side_Iceberg(const(1))),
                         "iceberg peg"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(const(10.)),
                            order.side.price.Limit(const(3))
                                 .side_price_Iceberg(const(1))
                                 .side_Peg),
                         "peg iceberg"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(constant(3.)),
                            order.side.price.Limit(const(3))
                                 .side_price_Iceberg(const(1))
                                 .side_Peg
                                 .side_WithExpiry(const(3))),
                         "peg iceberg expiry"),

        ctx.makeTrader_A(strategy.side.Signal(Interlacing()).Strategy(
                            event.Every(constant(10.)),
                            order.side.price.Limit(const(1))
                                 .side_Peg
                                 .side_Iceberg(const(1))
                                 .side_WithExpiry(const(10.))),
                         "iceberg peg expiry"),
    ]
