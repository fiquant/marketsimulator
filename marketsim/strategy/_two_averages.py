from marketsim.types import *
from marketsim import (orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, bind, defs, _)

from _generic import Periodic
from _signal import SignalBase, SignalSide

from _wrap import wrapper2

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        price = observable.Price(orderbook.OfTrader())
        self._average1 = observable.Fold(price, self.average1)
        self._average2 = observable.Fold(price, self.average2)
        SignalBase.__init__(self)
        
    _internals = ['_average1', '_average2']
        
    def _signalFunc(self):
        avg1 = self._average1()
        avg2 = self._average2()
        return avg1 - avg2 if avg1 is not None and avg2 is not None else None 

exec wrapper2("TwoAverages", 
             """ Two averages strategy compares two averages of price of the same asset but
                 with different parameters ('slow' and 'fast' averages) and when 
                 the first is greater than the second one it buys, 
                 when the first is lower than the second one it sells
                 
                 It has following parameters:

                 |average1| 
                      functional used to obtain the first average
                      (defaut: expenentially weighted moving average with |alpha| = 0.15)
                      
                 |average2| 
                      functional used to obtain the second average
                      (defaut: expenentially weighted moving average with |alpha| = 0.015)
                      
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                     
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)                     
             """,
             [('average1',              'mathutils.ewma(alpha = 0.15)',  'IUpdatableValue'),
              ('average2',              'mathutils.ewma(alpha = 0.015)', 'IUpdatableValue'),
              ('threshold',             '0.',                            'non_negative'), 
              ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')])

  
@registry.expose(["Periodic", 'TwoAverages'], args = ())
def TwoAveragesEx(average1 = None, #mathutils.ewma(alpha = 0.15), 
                  average2 = None, #mathutils.ewma(alpha = 0.015), 
                  threshold             = 0, 
                  orderFactory          = order.MarketFactory, 
                  creationIntervalDistr = mathutils.rnd.expovariate(1.), 
                  volumeDistr           = mathutils.rnd.expovariate(1.)):
    
    if average1 is None: average1 = mathutils.ewma(alpha = 0.15)
    if average2 is None: average2 = mathutils.ewma(alpha = 0.015)
    
    return defs(
        Periodic(orderFactory= orderFactory, 
                 volumeFunc  = volumeDistr,
                 eventGen    = scheduler.Timer(creationIntervalDistr),
                 sideFunc    = SignalSide(
                                  mathutils.sub(
                                     observable.Fold(_.price, average1),
                                     observable.Fold(_.price, average2)),
                                  threshold)), 
        { 'price' : observable.Price(orderbook.OfTrader()) })
