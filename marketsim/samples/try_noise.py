import sys
sys.path.append(r'../..')

from marketsim._pub import strategy, order, constant

from common import expose

@expose("Noise", __name__)
def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(
            strategy.price.LiquidityProvider()
                          .Strategy(orderFactory =
                                        order.side_price.Limit(volume=constant(2))
                                             .sideprice_WithExpiry(constant(10))),
                        "liquidity"),
        
        ctx.makeTrader_A(strategy.side.Noise().Strategy(), "noise_ex"),
    ]
