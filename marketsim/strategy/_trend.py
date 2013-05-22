from marketsim.types import *
from marketsim import (orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, signal, bind)
from _generic import Generic
from _signal import SignalBase, SignalSide

from _wrap import wrapper2

class _TrendFollower_Impl(SignalBase):

    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        self._signalFunc = observable.Fold(observable.Price(orderbook.OfTrader()), 
                                           observable.derivative(self.average))
        SignalBase.__init__(self)
        
    _internals = ['_signalFunc']
                
exec wrapper2('TrendFollower', 
             """ Trend follower can be considered as a sort of a signal strategy 
                 where the *signal* is a trend of the asset. 
                 Under trend we understand the first derivative of some moving average of asset prices. 
                 If the derivative is positive, the trader buys; if negative - it sells.
                 Since moving average is a continuously changing signal, we check its
                 derivative at random moments of time given by *creationIntervalDistr*. 
                 
                 It has following parameters:
                
                 |average| 
                     moving average functional. By default, we use exponentially weighted
                     moving average with |alpha| = 0.15.
                     
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                     
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation
                     (default: exponential distribution with |lambda| = 1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('average',                'mathutils.ewma(alpha = 0.15)',  'IUpdatableValue'),
              ('threshold',              '0.',                            'non_negative'), 
              ('orderFactory',           'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',            'mathutils.rnd.expovariate(1.)', '() -> Volume')])

@registry.expose(["Generic", 'TrendFollower'], args = ())
def TrendFollowerEx(average                 = mathutils.ewma(alpha = 0.15), 
                    threshold               = 0., 
                    orderFactory            = order.MarketFactory, 
                    creationIntervalDistr   = mathutils.rnd.expovariate(1.), 
                    volumeDistr             = mathutils.rnd.expovariate(1.)):
    
    orderBook = orderbook.OfTrader()
    trend = observable.Fold(observable.Price(orderBook), 
                            observable.derivative(average))
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr,
                eventGen    = scheduler.Timer(creationIntervalDistr),
                sideFunc    = SignalSide(trend, threshold))
    
    return r
    
