import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, order, event, const)

constant = const

from common import expose

@expose("Default", __name__)
def Complete(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200,
                                          orderFactory=order.side.Market(volume=const(12)))

    fv_200 = strategy.FundamentalValue(fundamentalValue=c_200,
                                       orderFactory=order.side.Market(volume=const(1)))
     
    def s_fv(fv):
        return strategy.TradeIfProfitable(
            strategy.FundamentalValue(fundamentalValue=const(fv),
                                       orderFactory=order.side.Market(volume=const(1))))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))
        
    
    return [
            ctx.makeTrader_A( 
                    strategy.LiquidityProvider(
                                orderFactory =
                                    order.side_price.Limit(volume=constant(170))
                                         .sideprice_WithExpiry(constant(10))),
                      "liquidity"),
            
    
            ctx.makeTrader_A(fv_200_12, "t200"),    
            ctx.makeTrader_A(fv_200, "t200_1"),

            ctx.makeTrader_A(strategy.FundamentalValue(event.Every(constant(1.)),
                                                       order.side.Market(const(1.)),
                                                       fundamentalValue=const(150.)),
                             "t150"),
            
            ctx.makeTrader_A(strategy.MeanReversion(event.Every(constant(1.)),
                                                    order.side.Market(const(1.))),
                             "mr_0_15"),
    
            ctx.makeTrader_A(strategy.CrossingAverages(event.Every(constant(1.)),
                                                  order.side.Market(const(1.)),
                                                  ewma_alpha_1=0.15,
                                                  ewma_alpha_2=0.015),
                             label="avg+"),

            ctx.makeTrader_A(strategy.CrossingAverages(event.Every(constant(1.)),
                                                  order.side.Market(const(1.)),
                                                  ewma_alpha_2=0.15,
                                                  ewma_alpha_1=0.015),
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
