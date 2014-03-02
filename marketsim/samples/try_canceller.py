import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, const)

from common import expose

@expose("Canceller", __name__)
def Canceller(ctx):

    ctx.volumeStep = 15

    return [
        ctx.makeTrader_A(strategy.price.LiquidityProvider().Strategy(),
                         "LiquidityProviderEx-"),

        ctx.makeTrader_A(strategy.Canceller(), "canceller"),
         
        ctx.makeTrader_A(
            strategy.side.FundamentalValue(const(1000)).Strategy(),
                            "fv_1000")
        ]