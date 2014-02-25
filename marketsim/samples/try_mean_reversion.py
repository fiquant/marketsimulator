import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, trader, order, math, event, constant)

from common import expose

@expose("Mean Reversion", __name__)
def MeanReversion(ctx):

    ctx.volumeStep = 40

    alpha = 0.015
    V = 1
    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=constant(-1),
                                      name="200-t")

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(
                            order.side_price.Limit(volume=constant(V*20)),
                            constant(10))),
                       label="liquidity"),
    
        ctx.makeTrader_A(strategy.Signal(
                                event.Every(constant(1.)),
                                order.side.Market(volume = constant(V*3)),
                                linear_signal), 
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
     
        ctx.makeTrader_A(
                strategy.MeanReversion(
                    event.Every(constant(1.)),
                    order.side.Market(volume = constant(V)),
                    alpha),
                 "meanreversion_ex", 
                 myVolume()),
    ]    
