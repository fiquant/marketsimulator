import sys
sys.path.append(r'..')

from marketsim import (strategy, orderbook, trader, order, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def Complete(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))

    fv_200 = fv_200_12.With(volumeDistr=const(1.))
     
    def s_fv(fv):
        return strategy.TradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))

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
            ctx.makeTrader_A(fv_200, "t200_1"),
            ctx.makeTrader_A(fv_200.With(), "t200_2"),
    
            ctx.makeTrader_A(strategy.FundamentalValue(fundamentalValue=const(150.),
                                                       volumeDistr=const(1.)),
                             "t150"),
            
            ctx.makeTrader_A(strategy.MeanReversion(volumeDistr=const(1.)),
                             "mr_0_15"),
    
            ctx.makeTrader_A(strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                  average2=mathutils.ewma(0.015),
                                                  volumeDistr=const(1.)),
                             label="avg+"),

            ctx.makeTrader_A(strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                  average2=mathutils.ewma(0.15),
                                                  volumeDistr=const(1.)),
                             label="avg-"),
    
            ctx.makeTrader_A(strategy.TradeIfProfitable(fv_200),
                             "v_fv200"),
            
            fv_virtual(160.),
            fv_virtual(170.),
            fv_virtual(180.),
            fv_virtual(190.),
    
            ctx.makeTrader_A(strategy.chooseTheBest([
                                               s_fv(160.),
                                               s_fv(170.),
                                               s_fv(180.),
                                               s_fv(190.), 
                                               ]),
                             "best")
    ]     

if __name__ == '__main__':
    run('registry', Complete)