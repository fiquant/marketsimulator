import sys
sys.path.append(r'../..')

from marketsim._pub import strategy
from common import expose

@expose("Market Data", __name__, only_veusz=True)
def MarketData(ctx):
    return [
        ctx.makeTrader_A(strategy.MarketData(), "marketdata2"),

        ctx.makeTrader_A(strategy.Noise(), "noise")
    ]