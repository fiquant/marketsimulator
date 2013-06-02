import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def MeanReversion(ctx):

    ctx.volumeStep = 40

    alpha = 0.15
    V = 1
    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")

    return [
        ctx.makeTrader_A( 
                       strategy.LiquidityProvider(
                            volumeDistr=const(V*20), 
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=const(10))),
                       label="liquidity"),
    
        ctx.makeTrader_A(strategy.Signal(linear_signal, 
                                         volumeDistr = const(V*3)), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.MeanReversion(
                                average=mathutils.ewma(alpha),
                                volumeDistr = const(V)),
                         label="meanreversion"),
    
        ctx.makeTrader_A(strategy.MeanReversionEx(
                                average=mathutils.ewma(alpha),
                                volumeDistr = const(V)),
                         label="meanreversion_ex")
    ]    

if __name__ == '__main__':
    run("mean_reversion", MeanReversion)