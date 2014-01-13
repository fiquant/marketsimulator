import sys
sys.path.append(r'../..')

from marketsim import (strategy, trader, orderbook, order, ops, Side, mathutils,
                       observable, veusz, registry, timeserie)

from common import expose

@expose("Canceller", __name__)
def Canceller(ctx):

    ctx.volumeStep = 15

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(),
                         "LiquidityProviderEx-"),

        ctx.makeTrader_A(strategy.Canceller(), "canceller"),
         
        ctx.makeTrader_A(   strategy.FundamentalValue(
                                fundamentalValue = ops.constant(1000)), 
                            "fv_1000")
        ]