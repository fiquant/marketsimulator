import sys, pickle
sys.path.append(r'../..')

from marketsim._pub import (event, strategy, order, constant)
from common import expose

@expose("Dependency", __name__)
def Dependency(ctx):

    liqVol = constant(3)
    
    ctx.volumeStep = 70

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(event.Every(constant(1.)),
                                       order.side_price.Limit(volume = liqVol),
                                       initialValue=50.),
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.LiquidityProvider(event.Every(constant(1.)),
                                       order.side_price.Limit(volume = liqVol),
                                       initialValue=150.),
            "LiquidityProvider_B"),
    
        ctx.makeTrader_A(
            strategy.PairTrading(
                event.Every(constant(1.)),
                order.side.Market(),
                ctx.book_B, 
                factor=2.),
            "A dependent on B ex"),
    
        ctx.makeTrader_B(
            strategy.PairTrading(
                event.Every(constant(1.)),
                order.side.Market(),
                ctx.book_A,
                factor=.5),
            "B dependent on A ex"),
    ]
