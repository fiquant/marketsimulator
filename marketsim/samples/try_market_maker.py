import sys
sys.path.append(r'../..')

from marketsim._pub import strategy
from common import expose

@expose("Market Maker", __name__)
def MarketMaker(ctx):
    return [
        ctx.makeTrader_A(strategy.price.MarketMaker().TwoSides, "marketmaker2"),
   
        ctx.makeTrader_A(strategy.side.Noise().Strategy(), "noise")
    ]