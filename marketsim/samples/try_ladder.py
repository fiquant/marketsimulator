import sys
sys.path.append(r'../..')

from marketsim._pub import (trader, strategy, orderbook, order, event, const, side, constant, math)


from common import expose, Constant

@expose("Ladder", __name__)
def Ladder(ctx):

    const = constant
    linear_signal = math.RandomWalk(initialValue=10,
                                    deltaDistr=const(-.1),
                                    name="20-0.1t")

    return [
        ctx.makeTrader_A(
            strategy.price.LiquidityProvider()
                          .Strategy(orderFactory = order.side_price.Limit(volume=const(10.))
                                                        .sideprice_WithExpiry(const(50.))),
            "liquidity"),

        ctx.makeTrader_A(
            strategy.price.LadderMM(initialSize=2)
                          .LadderBalancer(maximalSize=3)
                          .StopLoss(lossFactor=constant(0.25)),
            "ladder mm"
        ),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(const(4))),
                         "signal"),

    ]

