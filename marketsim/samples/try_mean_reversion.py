import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, trader, order, math, event, constant, orderbook)

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
    myVolume = lambda: [(trader.Position() / 3, demo),
                        (orderbook.OfTrader().MidPrice.EW(alpha).Avg.OnEveryDt(1), demo),
                        (orderbook.OfTrader().Asks.BestPrice, demo),
                        (orderbook.OfTrader().Bids.BestPrice, demo)]

    return [
        ctx.makeTrader_A( 
            strategy.price.LiquidityProvider(initialValue=30.)
                          .Strategy(orderFactory =
                                        order.side_price.Limit(volume=constant(V*20))
                                             .sideprice_WithExpiry(constant(10))),
                       label="liquidity"),
    
        ctx.makeTrader_A(strategy.side.Noise()
                                      .Strategy(event.Every(constant(1.)),
                                                order.side.Market(volume = constant(V*3))),
                         "signal", 
                         [(linear_signal, ctx.amount_graph)]),
     
        ctx.makeTrader_A(
                strategy.side.MeanReversion(
                    alpha
                ).Strategy(
                    event.Every(constant(1.)),
                    order.side.Market(volume = constant(V))),
                 "meanreversion_ex", 
                 myVolume()),
    ]    
