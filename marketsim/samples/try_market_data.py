import sys
sys.path.append(r'../..')

from marketsim import strategy, ops
from common import expose

@expose("Market Data", __name__, only_veusz=True)
def MarketData(ctx):
    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(defaultValue=50.,
                                       volumeDistr=ops.constant(50)),
            "LiquidityProvider_A"),

        ctx.makeTrader_A(strategy.MarketData(), "marketdata"),

        ctx.makeTrader_A(strategy.MarketMaker(), "marketmaker"),

        ctx.makeTrader_A(strategy.Noise(), "noise")
    ]