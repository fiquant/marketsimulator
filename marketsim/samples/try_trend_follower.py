import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, trader, order, constant, event, math)

const = constant

from common import expose

@expose("Trend Follower", __name__)
def TrendFollower(ctx):

    V = 1
    alpha = 0.015
    ctx.volumeStep = 30

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=const(-1), 
                                      name="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]

    return [
            ctx.makeTrader_A(
                strategy.LiquidityProvider(
                            orderFactory =
                                order.side_price.Limit(volume=constant(V*8)).sideprice_WithExpiry(constant(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.Signal(event.Every(constant(1.)),
                                             order.side.Market(const(V*2)),
                                             linear_signal), 
                            "signal", 
                            [
                             (linear_signal, ctx.amount_graph)
                            ]),
    
            ctx.makeTrader_A(strategy.TrendFollower(
                                event.Every(constant(1.)),
                                order.side.Market(volume = const(V)),
                                alpha),
                             "trendfollower_ex",
                             myVolume()), 
    ]
