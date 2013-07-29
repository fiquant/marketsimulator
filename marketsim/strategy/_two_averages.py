from marketsim.types import *
from marketsim import (orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, bind, defs, _)

from _periodic import Periodic, Generic
from _signal import SignalBase

from _wrap import wrapper2

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        price = observable.MidPrice(orderbook.OfTrader())
        self._average1 = observable.EWMA(price, self.ewma_alpha1)
        self._average2 = observable.EWMA(price, self.ewma_alpha2)
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
                      
                 |ewma_alpha1| 
                     parameter |alpha| for the first exponentially weighted moving average
                     (default: 0.15.)
                      
                 |ewma_alpha2| 
                     parameter |alpha| for the second exponentially weighted moving average
                     (default: 0.015.)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)                     
             """,
             [('ewma_alpha1',           '0.15',                          'non_negative'),
              ('ewma_alpha2',           '0.015',                         'non_negative'),
              ('threshold',             '0.',                            'non_negative'), 
              ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')])

import _wrap, side

class TwoAveragesEx(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 'price' : observable.MidPrice(orderbook.OfTrader()) }
    
    def getImpl(self):
        return  Periodic(orderFactory= self.orderFactory, 
                         volumeFunc  = self.volumeDistr,
                         eventGen    = scheduler.Timer(self.creationIntervalDistr),
                         sideFunc    = side.Signal(
                                          (observable.EWMA(_.price, self.ewma_alpha1) 
                                           - observable.EWMA(_.price, self.ewma_alpha2)),
                                          self.threshold))

_wrap.strategy(TwoAveragesEx, ['Periodic', 'TwoAverages'], 
             """ Two averages strategy compares two averages of price of the same asset but
                 with different parameters ('slow' and 'fast' averages) and when 
                 the first is greater than the second one it buys, 
                 when the first is lower than the second one it sells
                 
                 It has following parameters:

                 |ewma_alpha1| 
                     parameter |alpha| for the first exponentially weighted moving average
                     (default: 0.15.)
                      
                 |ewma_alpha2| 
                     parameter |alpha| for the second exponentially weighted moving average
                     (default: 0.015.)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)                     
             """,
             [('ewma_alpha1',           '0.15',                          'non_negative'),
              ('ewma_alpha2',           '0.015',                         'non_negative'),
              ('threshold',             '0.',                            'non_negative'), 
              ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')], 
               globals())

class TwoAverages2Ex(types.ISingleAssetStrategy):

    def getImpl(self):
        return  Generic(self.orderFactory(side.TwoAverages(self.ewma_alpha1, self.ewma_alpha2, self.threshold)),
                        scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(TwoAverages2Ex, ['Periodic', 'TwoAverages2'], 
             """ Two averages strategy compares two averages of price of the same asset but
                 with different parameters ('slow' and 'fast' averages) and when 
                 the first is greater than the second one it buys, 
                 when the first is lower than the second one it sells
                 
                 It has following parameters:

                 |ewma_alpha1| 
                     parameter |alpha| for the first exponentially weighted moving average
                     (default: 0.15.)
                      
                 |ewma_alpha2| 
                     parameter |alpha| for the second exponentially weighted moving average
                     (default: 0.015.)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)                     
             """,
             [
              ('ewma_alpha1',           '0.15',                          'non_negative'),
              ('ewma_alpha2',           '0.015',                         'non_negative'),
              ('threshold',             '0.',                            'non_negative'), 
              ('orderFactory',          'order.factory.Side_Market()',   'Side -> IOrderGenerator'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
             ], 
               globals())
