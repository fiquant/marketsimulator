import sys
sys.path.append(r'../..')

from marketsim import (strategy, orderbook, trader, order, mathutils, 
                       timeserie, event, observable, veusz, ops)

const = ops.constant

from common import expose

@expose("Default", __name__)
def Complete(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.v0.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))

    fv_200 = fv_200_12.With(volumeDistr=const(1.))
     
    def s_fv(fv):
        return strategy.TradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))
        
    
    return [
            ctx.makeTrader_A( 
                      strategy.v0.LiquidityProvider(
                            volumeDistr=const(70.), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))), 
                      "liquidity"), 
            
    
            ctx.makeTrader_A(fv_200_12, "t200"),    
            ctx.makeTrader_A(fv_200, "t200_1"),
            ctx.makeTrader_A(fv_200.With(), "t200_2"),
    
            ctx.makeTrader_A(strategy.FundamentalValue(order.factory.side.Market(const(1.)),
                                                       fundamentalValue=const(150.)),
                             "t150"),
            
            ctx.makeTrader_A(strategy.MeanReversion(order.factory.side.Market(const(1.))),
                             "mr_0_15"),
    
            ctx.makeTrader_A(strategy.TwoAverages(order.factory.side.Market(const(1.)),
                                                  ewma_alpha1=0.15,
                                                  ewma_alpha2=0.015),
                             label="avg+"),

            ctx.makeTrader_A(strategy.TwoAverages(order.factory.side.Market(const(1.)),
                                                  ewma_alpha2=0.15,
                                                  ewma_alpha1=0.015),
                             label="avg-"),
    
            ctx.makeTrader_A(strategy.TradeIfProfitable(fv_200),
                             "v_fv200"),
            
            fv_virtual(160.),
            fv_virtual(170.),
            fv_virtual(180.),
            fv_virtual(190.),
    
            ctx.makeTrader_A(strategy.ChooseTheBest([
                                               s_fv(160.),
                                               s_fv(170.),
                                               s_fv(180.),
                                               s_fv(190.), 
                                               ]),
                             "best")
    ]     
