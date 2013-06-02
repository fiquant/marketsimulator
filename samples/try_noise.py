import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils,
                       scheduler, observable, veusz, registry, timeserie)

from common import run 

def Noise(ctx):
    
    ctx.volumeStep = 10

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
                                volumeDistr=mathutils.constant(2),
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=mathutils.constant(10))), 
                         "liquidity"),
        
        ctx.makeTrader_A(strategy.Noise(), "noise"),
        
        ctx.makeTrader_A(strategy.NoiseEx(), "noise_ex")
    ]


if __name__ == '__main__':    
    run("noise_trader", Noise)
