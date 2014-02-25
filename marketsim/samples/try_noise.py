import sys
sys.path.append(r'../..')

from marketsim._pub import strategy, order, constant

from common import expose

@expose("Noise", __name__)
def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(
                            order.side_price.Limit(
                                volume=constant(2)),
                        constant(10))),
                        "liquidity"),
        
        ctx.makeTrader_A(strategy.Noise(), "noise_ex"),
    ]
