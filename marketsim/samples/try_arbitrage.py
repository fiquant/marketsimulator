import sys
sys.path.append(r'../..')

from common import expose

from marketsim._pub import math, strategy, order, constant

@expose("Arbitrage", __name__)
def Arbitrage(ctx):

    liqVol = math.random.expovariate(.1) * 2.
    
    ctx.volumeStep = 70

    def makeLP(dv):
        return (
            strategy.price.LiquidityProvider(initialValue= dv)
                          .Strategy(orderFactory = order.side_price.Limit(volume=liqVol)
                                                        .sideprice_WithExpiry(constant(50))))
    
    return [
        ctx.makeTrader_A(
            makeLP(50.),
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B(
            makeLP(150.),
            "LiquidityProvider_B"),
            
        ctx.makeTrader_C(
            makeLP(100.),
            "LiquidityProvider_C"),

        ctx.makeMultiAssetTrader([ctx.remote_A, ctx.remote_B, ctx.remote_C],
                                 strategy.Arbitrage(), 
                                 "Arbitrager")
    ]    
