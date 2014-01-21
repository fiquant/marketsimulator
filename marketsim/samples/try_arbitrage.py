import sys
sys.path.append(r'../..')

from common import expose

from marketsim._pub import math, strategy, order, constant

@expose("Arbitrage", __name__)
def Arbitrage(ctx):

    liqVol = math.random.expovariate(.1) * 2
    
    ctx.volumeStep = 70
    
    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(constant(50),
                            order.side_price.Limit(volume=liqVol)),
                        initialValue= 50.),
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(constant(50),
                            order.side_price.Limit(volume=liqVol)),
                        initialValue = 150.),
            "LiquidityProvider_B"),
            
        ctx.makeTrader_C(
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(constant(50),
                            order.side_price.Limit(volume=liqVol)),
                        initialValue = 100.),
            "LiquidityProvider_C"),

        ctx.makeMultiAssetTrader([ctx.remote_A, ctx.remote_B, ctx.remote_C],
                                 strategy.Arbitrage(), 
                                 "Arbitrager")
    ]    
