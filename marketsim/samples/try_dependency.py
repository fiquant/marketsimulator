import sys, pickle
sys.path.append(r'../..')

from marketsim import (parts, strategy, orderbook, trader, scheduler, observable, 
                       veusz, ops, mathutils, timeserie, order)
from common import expose

@expose("Dependency", __name__)
def Dependency(ctx):

    liqVol = ops.constant(2)
    
    ctx.volumeStep = 70

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(order.factory.sideprice.Limit(volume = liqVol),
                                       defaultValue=50.), 
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.LiquidityProvider(order.factory.sideprice.Limit(volume = liqVol),
                                       defaultValue=150.), 
            "LiquidityProvider_B"),
    
        ctx.makeTrader_A(
            strategy.Dependency(
                order.factory.side.Market(),
                ctx.book_B, 
                factor=2.),
            "A dependent on B ex"),
    
        ctx.makeTrader_B(
            strategy.Dependency(
                order.factory.side.Market(),
                ctx.book_A, 
                factor=.5),
            "B dependent on A ex"),
    ]    
