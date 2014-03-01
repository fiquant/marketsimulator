import sys
sys.path.append(r'../..')

from marketsim._pub import (order, strategy, trader, math, orderbook, observable, event, const, constant)

from common import expose

@expose("Trade-If-Profitable", __name__)
def TradeIfProfitable(ctx):

    ctx.volumeStep = 30
    
    slow_alpha = 0.015
    fast_alpha = 0.15

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=constant(-1),
                                      name="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]
    myAverage = lambda alpha: [(orderbook.OfTrader().MidPrice.EW(alpha).Avg.OnEveryDt(1), demo)]
    
    def cross(alpha1, alpha2):
        return strategy.CrossingAverages(
                    event.Every(constant(1.)),
                    order.side.Market(volume = constant(1.)),
                    alpha1, alpha2)
    
    
    avg_plus_virt = strategy.TradeIfProfitable(cross(slow_alpha, fast_alpha), strategy.account.virtualMarket())
    avg_minus_virt = strategy.TradeIfProfitable(cross(fast_alpha, slow_alpha), strategy.account.virtualMarket())

    avg_plus_real = strategy.TradeIfProfitable(cross(slow_alpha, fast_alpha), strategy.account.real())
    avg_minus_real = strategy.TradeIfProfitable(cross(fast_alpha, slow_alpha), strategy.account.real())

    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(
            orderFactory = order.side_price.Limit(
                volume=constant(45))),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(
                                    event.Every(constant(1.)),
                                    order.side.Market(volume = constant(20)),
                                    linear_signal), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(cross(slow_alpha, fast_alpha), 
                        'avg+', 
                        myAverage(slow_alpha) + myAverage(fast_alpha) + myVolume()),
 
        ctx.makeTrader_A(cross(fast_alpha, slow_alpha), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_virt, 
                         'avg+ virt',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_virt, 
                         'avg- virt',
                         myVolume()),

        ctx.makeTrader_A(avg_plus_real, 
                         'avg+ real',
                         myVolume()),

        ctx.makeTrader_A(avg_minus_real, 
                         'avg- real',
                         myVolume()),
    ]
