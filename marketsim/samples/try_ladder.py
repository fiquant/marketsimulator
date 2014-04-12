import sys
sys.path.append(r'../..')

from marketsim._pub import (trader, strategy, orderbook, order, event, const, side)


from common import expose, Constant

@expose("Ladder", __name__)
def Ladder(ctx):

    return [
        ctx.makeTrader_A(
            strategy.price.LiquidityProvider()
                          .Strategy(orderFactory = order.side_price.Limit(volume=const(6.))
                                                        .sideprice_WithExpiry(const(100.))),
            "liquidity"),

        ctx.makeTrader_A(
            strategy.price.Ladder(order.side_price.Limit(), side = side.Sell()),
            "ladder sell"
        ),

        ctx.makeTrader_A(
            strategy.price.Ladder(order.side_price.Limit(), side = side.Buy()),
            "ladder buy"
        )
    ]

