import sys
sys.path.append(r'../..')

from marketsim import strategy, ops, Side, order
from common import expose

@expose("Market Data", __name__, only_veusz=True)
def MarketData(ctx):
    return [
#         ctx.makeTrader_A(strategy.v0.MarketMaker(), "marketmaker"),

        ctx.makeTrader_A(strategy.MarketMaker(), "marketmaker2"),
   
        ctx.makeTrader_A(strategy.Noise(), "noise")
    ]