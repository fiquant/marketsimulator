import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def Signal(ctx):

    linear_signal = signal.RandomWalk(initialValue=20, 
                                      deltaDistr=const(-.1), 
                                      label="20-0.1t")

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(2)),
                         "liquidity"),
        
        ctx.makeTrader_A(strategy.Signal(linear_signal), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
    
        ctx.makeTrader_A(strategy.SignalEx(linear_signal), 
                         "signal_ex")
    ]    

if __name__ == '__main__':
    run("signal_trader", Signal)