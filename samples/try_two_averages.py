import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TwoAverages(ctx):

    slow = mathutils.ewma(alpha = 0.015)
    fast = mathutils.ewma(alpha = 0.15)

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(10)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(linear_signal,
                                         volumeDistr=const(3)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),

        ctx.makeTrader_A(strategy.TwoAverages(average1 = slow, 
                                              average2 = fast), 
                        'avg+'),

        ctx.makeTrader_A(strategy.TwoAverages(average1 = fast, 
                                              average2 = slow), 
                         'avg-'),

        ctx.makeTrader_A(strategy.TwoAveragesEx(average1 = slow, 
                                                average2 = fast), 
                         'avg_ex+'),

        ctx.makeTrader_A(strategy.TwoAveragesEx(average1 = fast, 
                                                average2 = slow), 
                         'avg_ex-')
    ]

if __name__ == '__main__':
    run("two_averages", TwoAverages)