import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, trader, orderbook, constant, order, event, math)

const = constant

from common import expose

@expose("Two Averages", __name__)
def TwoAverages(ctx):

    ctx.volumeStep = 30
    
    alpha_slow = 0.015
    alpha_fast = 0.15

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=const(-1), 
                                      name="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(orderbook.OfTrader().MidPrice, demo),
                        (trader.Position() / const(10.), demo),
                        (orderbook.OfTrader().MidPrice.EW(alpha_fast).Avg.OnEveryDt(1), demo),
                        (orderbook.OfTrader().MidPrice.EW(alpha_slow).Avg.OnEveryDt(1), demo)]

    return [
        ctx.makeTrader_A(
                strategy.price.LiquidityProvider(initialValue=10.)
                              .Strategy(
                                    event.Every(constant(1.)),
                                    order.side_price.Limit(volume=const(10))),
                "liquidity"),

        ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = const(3))),
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(strategy.side.CrossingAverages(alpha_slow,
                                                        alpha_fast)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = const(1.))),
                         'avg_ex+',
                         myVolume()),

        ctx.makeTrader_A(strategy.side.CrossingAverages(alpha_fast,
                                                        alpha_slow)
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = const(1.))),
                         'avg_ex-',
                         myVolume()),
    ]
