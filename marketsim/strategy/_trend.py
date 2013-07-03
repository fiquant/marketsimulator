from marketsim.types import *
from marketsim import (orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, signal, bind)
from _periodic import Periodic
from _signal import SignalBase, SignalSide

from _wrap import wrapper2

class _TrendFollower_Impl(SignalBase):

    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr) # TODO: dependency tracking
        self._signalFunc_ = observable.Derivative(
                                observable.EWMA(
                                    observable.Price(orderbook.OfTrader()),
                                    self.ewma_alpha))
        SignalBase.__init__(self)
        
    def _signalFunc(self):
        return self._signalFunc_()
        
    _internals = ['_signalFunc_']
                
exec wrapper2('TrendFollower', 
             """ Trend follower can be considered as a sort of a signal strategy 
                 where the *signal* is a trend of the asset. 
                 Under trend we understand the first derivative of some moving average of asset prices. 
                 If the derivative is positive, the trader buys; if negative - it sells.
                 Since moving average is a continuously changing signal, we check its
                 derivative at random moments of time given by *creationIntervalDistr*. 
                 
                 It has following parameters:
                
                 |ewma_alpha| 
                     parameter |alpha| for exponentially weighted moving average
                    (default: 0.15.)
                     
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
             [('ewma_alpha',             '0.15',                          'non_negative'),
              ('threshold',              '0.',                            'non_negative'), 
              ('orderFactory',           'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',            'mathutils.rnd.expovariate(1.)', '() -> Volume')])

@registry.expose(["Periodic", 'TrendFollower'], args = ())
def TrendFollowerEx(ewma_alpha              = 0.15, 
                    threshold               = 0., 
                    orderFactory            = order.MarketFactory, 
                    creationIntervalDistr   = mathutils.rnd.expovariate(1.), 
                    volumeDistr             = mathutils.rnd.expovariate(1.)):
    
    orderBook = orderbook.OfTrader()
    trend = observable.Derivative(
                observable.EWMA(
                    observable.Price(orderBook),
                    ewma_alpha))
    
    return Periodic(orderFactory= orderFactory, 
                    volumeFunc  = volumeDistr,
                    eventGen    = scheduler.Timer(creationIntervalDistr),
                    sideFunc    = SignalSide(trend, threshold))
    
