import sys
sys.path.append(r'..')

from marketsim import strategy, mathutils, order

from common import expose

@expose("Noise", __name__)
def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
                                volumeDistr=mathutils.constant(2),
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=mathutils.constant(10))), 
                         "liquidity"),
        
        ctx.makeTrader_A(strategy.Noise(), "noise"),
        
        ctx.makeTrader_A(strategy.NoiseEx(), "noise_ex")
    ]
