import sys
sys.path.append(r'../..')

from marketsim import strategy, mathutils, order, ops

from common import expose

@expose("Noise", __name__)
def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
                                volumeDistr=ops.constant(2),
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=ops.constant(10))), 
                         "liquidity"),
        
        ctx.makeTrader_A(strategy.Noise(), "noise"),
        
        ctx.makeTrader_A(strategy.Noise(
                             orderFactory = order.AlwaysBestFactory()),
                         "noise_best"),
         
        ctx.makeTrader(ctx.remote_A, strategy.Noise2Ex(), "noise2_ex"),
         
        ctx.makeTrader(ctx.remote_A, strategy.NoiseEx(), "noise_ex")
    ]
