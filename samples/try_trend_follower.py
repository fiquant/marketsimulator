import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, order,
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TrendFollower(ctx):

    V = 1
    alpha = 0.065
    ctx.volumeStep = 30

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    return [
            ctx.makeTrader_A( 
                             strategy.LiquidityProvider(
                                volumeDistr=const(V*4), 
                                orderFactoryT=order.WithExpiryFactory(
                                    expirationDistr=const(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.Signal(linear_signal, 
                                             volumeDistr = const(V)), 
                            "signal", 
                            [(linear_signal, ctx.amount_graph)]),
    
            ctx.makeTrader_A(strategy.TrendFollower(
                                    average=mathutils.ewma(alpha),
                                    volumeDistr = const(V)),
                             label="trendfollower"),

            ctx.makeTrader_A(strategy.TrendFollowerEx(
                                       average=mathutils.ewma(alpha),
                                       volumeDistr = const(V)),
                             label="trendfollower_ex")
    ]
    

if __name__ == '__main__':
    run("trend_follower", TrendFollower)