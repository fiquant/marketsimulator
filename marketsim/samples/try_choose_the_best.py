import sys
sys.path.append(r'../..')

from marketsim import (strategy, orderbook, trader, order, 
                       timeserie, scheduler, observable, veusz, ops)

const = ops.constant
from common import expose

@expose("Choose-The-Best", __name__)
def ChooseTheBest(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))

    fv_200 = fv_200_12.With(volumeDistr=const(1.), creationIntervalDistr=const(1.))
     
    def s_fv(fv):
        return fv_200.With(fundamentalValue=const(fv))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))

    return [
            ctx.makeTrader_A( 
                      strategy.LiquidityProvider(
                            volumeDistr=const(70.), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))), 
                      "liquidity"), 
            
    
            ctx.makeTrader_A(fv_200_12, "t200"),    
    
            fv_virtual(100.),
            fv_virtual(150.),
            fv_virtual(200.),
            fv_virtual(250.),
            fv_virtual(300.),
    
            ctx.makeTrader_A(strategy.ChooseTheBest([
                                               s_fv(100.),
                                               s_fv(150.), 
                                               s_fv(200.), 
                                               s_fv(250.), 
                                               s_fv(300.), 
                                               ]),
                             "best")
    ]     
