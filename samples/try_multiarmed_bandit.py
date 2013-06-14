import sys
sys.path.append(r'..')

from marketsim import (strategy, orderbook, trader, order, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def MultiarmedBandit(ctx):
    
    ctx.volumeStep = 100

    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))

    fv_200 = fv_200_12.With(volumeDistr=const(1.), creationIntervalDistr=const(1.))
     
    def s_fv(fv):
        return fv_200.With(fundamentalValue=const(fv))

    def fv_virtual(fv):
        return ctx.makeTrader_A(s_fv(fv), "v" + str(fv))
    
    def s_fv_list( fv_list = [100]):
        return [ s_fv(fv) for fv in fv_list]
        
    fv_list = [100, 150, 200, 250, 300]

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
            
            ctx.makeTrader_A(strategy.chooseTheBest( s_fv_list(fv_list) ),
                            "best"),
    
            ctx.makeTrader_A(strategy.MultiarmedBandit( s_fv_list(fv_list) ),
                             "bandit (TrackRecord)")
    ]     

if __name__ == '__main__':
    run('multiarmed_bandit', MultiarmedBandit)