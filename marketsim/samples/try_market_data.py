import sys
sys.path.append(r'../..')

from marketsim import strategy, ops
from common import expose

@expose("Market Data", __name__, only_veusz=True)
def MarketData(ctx):
    return [
        #ctx.makeTrader_A(strategy.v0.MarketData(), "marketdata"),

        ctx.makeTrader_A(strategy.MarketData(), "marketdata2"),

        ctx.makeTrader_A(strategy.v0.MarketMaker(), "marketmaker"),
 
        ctx.makeTrader_A(strategy.MarketMaker(), "marketmaker2"),
   
        ctx.makeTrader_A(strategy.Noise(), "noise")
    ]