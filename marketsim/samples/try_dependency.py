import sys, pickle
sys.path.append(r'../..')

from marketsim._pub import (event, strategy, order, constant, math, orderbook, trader)
from common import expose

@expose("Dependency", __name__)
def Dependency(ctx):

    V = 1
    alpha = 0.015
    ctx.volumeStep = 30
    const = constant

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=const(-1),
                                      name="200-t")

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(orderbook.OfTrader().MidPrice, demo),
                        (trader.Position(), demo),
                        (orderbook.OfTrader().MidPrice.EW().Avg.OnEveryDt(1), demo)]

    return [
            ctx.makeTrader_A(
                strategy.price.LiquidityProvider(100.)
                              .Strategy(orderFactory =
                                            order.side_price.Limit(volume=constant(V*8)).sideprice_WithExpiry(constant(100))),
                             label="liquidity"),

            ctx.makeTrader_B(
                strategy.price.LiquidityProvider(200.)
                              .Strategy(orderFactory =
                                            order.side_price.Limit(volume=constant(V*8)).sideprice_WithExpiry(constant(100))),
                             label="liquidity B"),

            ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                          .Strategy(event.Every(constant(1.)),
                                                    order.side.Market(const(V*3))),
                            "signal",
                            [
                             (linear_signal, ctx.amount_graph),
                            ]),

            ctx.makeTrader_B(
                strategy.side.PairTrading(
                    ctx.book_A,
                    factor=2.
                ).Strategy(event.Every(constant(1.)),
                           order.side.Market(const(V*5))),
                "B dependent on A ex"),
    ]
