import sys
sys.path.append(r'../..')

from marketsim._pub import (trader, strategy, orderbook, order, event, const)


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
                        orderFactory = order.side_price.WithExpiry(
                            order.side_price.Limit(volume=const(6)),
                            const(10))),
            "liquidity"),
    
        ctx.makeTrader_A(
             strategy.FundamentalValue(
                event.Every(const(1.)),
                order.side.Market(volume = const(1.)),
                const(fv)),
            "fv_200",
            myVolume()),
    ]

