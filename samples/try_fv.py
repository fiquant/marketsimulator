import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, timeserie,
                       scheduler, observable, veusz, mathutils)

from common import run 

def FundamentalValue(ctx):

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                 volumeDistr=mathutils.constant(5),
                 orderFactoryT=order.WithExpiryFactory(
                     expirationDistr=mathutils.constant(10))),
            "liquidity"),
    
        ctx.makeTrader_A( 
            strategy.FundamentalValue(
               fundamentalValue = mathutils.constant(200),
               volumeDistr = mathutils.constant(1)), 
            "fv_200"),

        ctx.makeTrader_A(
            strategy.FundamentalValueEx(
               fundamentalValue = mathutils.constant(200),
               volumeDistr = mathutils.constant(1)), 
            "fv_ex_200")
    ]

if __name__ == '__main__':    
    run("fv_200_trader", FundamentalValue)
        
