import sys
sys.path.append(r'../..')

from marketsim import (strategy, trader, orderbook, order, timeserie,
                       scheduler, types, observable, veusz, ops)


from common import expose, Constant

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
                 volumeDistr=ops.constant(6),
                 orderFactoryT=order.WithExpiryFactory(
                     expirationDistr=ops.constant(10))),
            "liquidity"),
    
        ctx.makeTrader_A( 
            strategy.FundamentalValue(
               fundamentalValue = ops.constant(fv),
               creationIntervalDistr = ops.constant(1.),
               volumeDistr = ops.constant(1)), 
            "fv_200", 
            myVolume() + myPrice() + Constant(fv, demo)),

        ctx.makeTrader_A(
             strategy.Generic(
                order.factory.Market(
                    side = strategy.side.FundamentalValue(ops.constant(fv)),
                    volume = ops.constant(1.)), 
                scheduler.Timer(ops.constant(1.))),
            "fv_ex_200", 
            myVolume()),
    ]

