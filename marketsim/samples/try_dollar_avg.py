import sys
sys.path.append(r'../..')

from marketsim import strategy
from common import expose
from marketsim.ops import constant as const

@expose("Dollar Average", __name__, only_veusz=True)
def DollarAverage(ctx):
    return [
        ctx.makeTrader_A(strategy.DollarAverage(), "dollaravg"),

        ctx.makeTrader_A(strategy.MarketData(), "marketdata"),

        # ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(10)), "liquidity"),


    ]