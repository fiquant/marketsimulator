import sys
sys.path.append(r'../..')

from marketsim import (strategy, orderbook, trader, order, 
                       timeserie, scheduler, observable, veusz, ops)

const = ops.constant

from common import expose

@expose("Multiarmed Bandit", __name__)
def MultiarmedBandit(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.v0.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))

    fv_200 = fv_200_12.With(volumeDistr=const(1.), creationIntervalDistr=const(1.))
     
    def s_fv(fv):
        return fv_200.With(fundamentalValue=const(fv))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))
    
    fv_list = [100, 150, 200, 250, 300]

    def s_fv_list( fv_list = fv_list ):
        return [ s_fv(fv) for fv in fv_list]

    return [
            ctx.makeTrader_A( 
                      strategy.v0.LiquidityProvider(
                            volumeDistr=const(70.), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))), 
                      "liquidity"), 
            
    
            ctx.makeTrader_A(fv_200_12, "t200"),    
            
            ctx.makeTrader_A(strategy.ChooseTheBest(s_fv_list()), "best"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit(s_fv_list(), 
                                                       strategy.weight.TrackRecord()),
                             "TrackRecord"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit(s_fv_list(), 
                                                       strategy.weight.EfficiencyAlpha()),
                             "EfficiencyAlpha"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit(s_fv_list(), 
                                                       strategy.weight.Efficiency()),
                             "Efficiency"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit(s_fv_list(), 
                                                       strategy.weight.ChooseTheBest()),
                             "ChooseTheBest"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit(s_fv_list(), 
                                                       strategy.weight.Uniform()),
                             "Uniform"),
    ] + map(fv_virtual, fv_list)     
