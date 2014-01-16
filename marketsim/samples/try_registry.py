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
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200,
                                          orderFactory=order.factory.side.Market(volume=const(12)))

    fv_200 = strategy.FundamentalValue(fundamentalValue=c_200,
                                       orderFactory=order.factory.side.Market(volume=const(1)))
     
    def s_fv(fv):
        return strategy.TradeIfProfitable(
            strategy.FundamentalValue(fundamentalValue=const(fv),
                                       orderFactory=order.factory.side.Market(volume=const(1))))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))
        
    
    return [
            ctx.makeTrader_A( 
                    strategy.LiquidityProvider(
                                orderFactory = order.factory.sideprice.WithExpiry(
                                    ops.constant(10),
                                    order.factory.sideprice.Limit(
                                        volume=ops.constant(170)))),
                      "liquidity"),
            
    
            ctx.makeTrader_A(fv_200_12, "t200"),    
            ctx.makeTrader_A(fv_200, "t200_1"),

            ctx.makeTrader_A(strategy.FundamentalValue(event.Every(ops.constant(1.)),
                                                       order.factory.side.Market(const(1.)),
                                                       fundamentalValue=const(150.)),
                             "t150"),
            
            ctx.makeTrader_A(strategy.MeanReversion(event.Every(ops.constant(1.)),
                                                    order.factory.side.Market(const(1.))),
                             "mr_0_15"),
    
            ctx.makeTrader_A(strategy.TwoAverages(event.Every(ops.constant(1.)),
                                                  order.factory.side.Market(const(1.)),
                                                  ewma_alpha_1=0.15,
                                                  ewma_alpha_2=0.015),
                             label="avg+"),

            ctx.makeTrader_A(strategy.TwoAverages(event.Every(ops.constant(1.)),
                                                  order.factory.side.Market(const(1.)),
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
