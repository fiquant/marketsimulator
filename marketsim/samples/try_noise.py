import sys
sys.path.append(r'../..')

from marketsim import strategy, mathutils, order, ops

from common import expose, Interlacing

@expose("Noise", __name__)
def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(
                        orderFactory = order.factory.sideprice.WithExpiry(
                            ops.constant(10),
                            order.factory.sideprice.Limit(
                                volume=ops.constant(2)))),
                         "liquidity"),
        
        ctx.makeTrader_A(strategy.Noise(), "noise_ex"),
    ]
