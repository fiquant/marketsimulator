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
            strategy.LiquidityProvider(defaultValue=50., 
                                       volumeDistr=liqVol), 
            "LiquidityProvider_A"),
    
        ctx.makeTrader_B( 
            strategy.LiquidityProvider(defaultValue=150., 
                                       volumeDistr=liqVol), 
            "LiquidityProvider_B"),
    
        ctx.makeTrader_A(strategy.Dependency(ctx.book_B, factor=2), 
                         "A dependent on B"),
    
        ctx.makeTrader_B(strategy.Dependency(ctx.book_A, factor=.5), 
                         "B dependent on A"),

        ctx.makeTrader_A(
            strategy.Generic(
                order.factory.Market(
                    parts.side.Dependency(ctx.book_B, factor=2.))),
             "A dependent on B ex"),
    
        ctx.makeTrader_B(
            strategy.Generic(
                order.factory.Market(
                    parts.side.Dependency(ctx.book_A, factor=.5))),
             "B dependent on A ex"),
    ]    
