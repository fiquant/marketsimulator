import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils, Side,
                       scheduler, observable, veusz, registry, timeserie)

from common import run 

def Canceller(ctx):

    ctx.volumeStep = 15

    return [
        ctx.makeTrader_A(strategy.LiquidityProviderSide(side = Side.Sell),
                         "LiquidityProvider-"),
        
        ctx.makeTrader_A(strategy.LiquidityProviderEx(
                            orderFactory=order.WithExpiryFactory(
                                    expirationDistr=mathutils.constant(1))),
                         "LiquidityProviderEx-"),
        
        ctx.makeTrader_A(strategy.LiquidityProviderSide(side = Side.Buy),
                         "LiquidityProviderBuy"),
    
        ctx.makeTrader_A(   strategy.Array([
                                strategy.LiquidityProviderSide(side = Side.Sell),
                                strategy.Canceller()
                            ]),
                           label = "LiquidityProviderWithCanceller"),
        
        ctx.makeTrader_A(  strategy.LiquidityProviderSide(
                                side = Side.Sell,
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=mathutils.constant(10))),
                           "LiquidityProviderWithExpiry"),
        
        ctx.makeTrader_A(   strategy.FundamentalValue(
                                fundamentalValue = mathutils.constant(1000)), 
                            "fv_1000")
]
    
if __name__ == '__main__':    
    run("canceller", Canceller)
