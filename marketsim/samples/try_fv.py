import sys
sys.path.append(r'../..')

from marketsim._pub import (trader, strategy, orderbook, order, event, constant)


from common import expose, Constant

@expose("Fundamental value", __name__)
def FundamentalValue(ctx):
    
    ctx.volumeStep = 30
    fv = 200

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(trader.Position(), demo)]
    myPrice = lambda: [(orderbook.MidPrice(), demo)]

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                        orderFactory = order.side_price.WithExpiry(constant(10),
                            order.side_price.Limit(volume=constant(6)))),
            "liquidity"),
    
        ctx.makeTrader_A(
             strategy.FundamentalValue(
                event.Every(constant(1.)),
                order.side.Market(volume = constant(1.)),
                constant(fv)),
            "fv_200",
            myVolume()),
    ]

