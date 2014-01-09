import sys
sys.path.append(r'../..')

from marketsim import (parts, strategy, trader, orderbook, order, timeserie,
                       event, types, observable, veusz, ops)


from common import expose, Constant

#noinspection PyArgumentList
@expose("Fundamental value", __name__)
def FundamentalValue(ctx):
    
    ctx.volumeStep = 30
    fv = 200

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myPrice = lambda: [(observable.MidPrice(orderbook.OfTrader()), demo)]

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                        orderFactory = order.factory.sideprice.WithExpiry(ops.constant(10),
                            order.factory.sideprice.Limit(volume=ops.constant(6)))),
            "liquidity"),
    
        ctx.makeTrader_A(
             strategy.FundamentalValue(
                event.Every(ops.constant(1.)),
                order.factory.side.Market(volume = ops.constant(1.)), 
                ops.constant(fv)),
            "fv_200",
            myVolume()),
    ]

