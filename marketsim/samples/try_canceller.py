import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, const, order)

from common import expose

@expose("Canceller", __name__)
def Canceller(ctx):

    ctx.volumeStep = 15

    return [
        ctx.makeTrader_A(strategy.price.LiquidityProvider()
                                       .Strategy(orderFactory=order.side_price.Limit(const(10))),
                         "LiquidityProviderEx-"),

        ctx.makeTrader_A(strategy.Canceller(), "canceller"),
         
        ctx.makeTrader_A(
            strategy.side.FundamentalValue(fv=const(200)).Strategy(),
                            "fv_1000")
        ]