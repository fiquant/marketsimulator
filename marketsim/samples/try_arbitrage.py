import sys
sys.path.append(r'../..')

from marketsim import (order, strategy, 
                       ops, mathutils)
from common import expose

@expose("Arbitrage", __name__)
def Arbitrage(ctx):

    liqVol = mathutils.rnd.expovariate(.1) * 2
    
    ctx.volumeStep = 70
    
    factory = order.WithExpiryFactory(ops.constant(50))

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(defaultValue=50.,
                                       orderFactoryT=factory, 
                                       volumeDistr=liqVol), 
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.LiquidityProvider(defaultValue=150., 
                                       orderFactoryT=factory, 
                                       volumeDistr=liqVol), 
            "LiquidityProvider_B"),
            
        ctx.makeMultiAssetTrader([ctx.remote_A, ctx.remote_B], 
                                 strategy.Arbitrage(), 
                                 "Arbitrager")
    ]    
