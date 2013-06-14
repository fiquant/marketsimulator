import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, timeserie,
                       scheduler, types, observable, veusz, mathutils)


class Constant(object):
    
    def __init__(self, value):
        self.value = value
        
    @property
    def label(self):
        return "C=" + str(self.value)
    
    def __call__(self):
        return self.value
    
    _properties = { 'value' : float }

from common import expose

@expose("Fundamental value", __name__)
def FundamentalValue(ctx):
    
    ctx.volumeStep = 30
    fv = 200

    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myPrice = lambda: [(observable.Price(orderbook.OfTrader()), demo)]

    return [
        ctx.makeTrader_A( 
            strategy.LiquidityProvider(
                 volumeDistr=mathutils.constant(6),
                 orderFactoryT=order.WithExpiryFactory(
                     expirationDistr=mathutils.constant(10))),
            "liquidity"),
    
        ctx.makeTrader_A( 
            strategy.FundamentalValue(
               fundamentalValue = mathutils.constant(fv),
               creationIntervalDistr = mathutils.constant(1.),
               volumeDistr = mathutils.constant(1)), 
            "fv_200", 
            myVolume() + myPrice() + [(observable.OnEveryDt(10, Constant(fv)), demo)]),

        ctx.makeTrader_A(
            strategy.FundamentalValueEx(
               fundamentalValue = mathutils.constant(fv),
               creationIntervalDistr = mathutils.constant(1.),
               volumeDistr = mathutils.constant(1)), 
            "fv_ex_200", 
            myVolume())
    ]

