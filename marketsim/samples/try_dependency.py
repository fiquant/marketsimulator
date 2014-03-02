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
            strategy.price.LiquidityProvider(50.)
                           .Strategy(event.Every(constant(1.)),
                                     order.side_price.Limit(volume = liqVol)),
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.price.LiquidityProvider(150.)
                           .Strategy(event.Every(constant(1.)),
                                     order.side_price.Limit(volume = liqVol)),
            "LiquidityProvider_B"),
    
        ctx.makeTrader_A(
            strategy.side.PairTrading(
                ctx.book_B,
                factor=2.
            ).Strategy(
                event.Every(constant(1.)),
                order.side.Market()),
            "A dependent on B ex"),
    
        ctx.makeTrader_B(
            strategy.side.PairTrading(
                ctx.book_A,
                factor=.5
            ).Strategy(
                event.Every(constant(1.)),
                order.side.Market()),
            "B dependent on A ex"),
    ]
