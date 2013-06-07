import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TradeIfProfitable(ctx):

    ctx.volumeStep = 30
    
    alpha_slow = 0.015
    alpha_fast = 0.15

    slow = lambda: mathutils.ewma(alpha = alpha_slow)
    fast = lambda: mathutils.ewma(alpha = alpha_fast)

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.Price(orderbook.OfTrader()), alpha), demo)]
    
    avg_plus = strategy.TwoAverages(average1 = slow(), 
                                    average2 = fast(),
                                    creationIntervalDistr = mathutils.constant(1.),
                                    volumeDistr           = mathutils.constant(1.))
    
    avg_minus = strategy.TwoAverages(average1 = fast(), 
                                     average2 = slow(),
                                     creationIntervalDistr = mathutils.constant(1.),
                                     volumeDistr           = mathutils.constant(1.))
    
    avg_plus_opt = strategy.TradeIfProfitable(avg_plus)
    avg_minus_opt = strategy.TradeIfProfitable(avg_minus)

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(45)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(linear_signal,
                                         volumeDistr=const(20)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(avg_plus, 
                        'avg+', 
                        myAverage(alpha_slow) + myAverage(alpha_fast) + myVolume()),

        ctx.makeTrader_A(avg_minus, 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_opt, 
                         'avg+ opt',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_opt, 
                         'avg- opt',
                         myVolume()),
    ]

if __name__ == '__main__':
    run("trade_if_profitable", TradeIfProfitable)