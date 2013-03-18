from marketsim.types import *
from marketsim import observable, scheduler, order, mathutils, types, registry, signal
from _basic import TwoSides, Strategy
from _wrap import wrapper

class SignalBase(TwoSides):
    
    def __init__(self, trader):
        TwoSides.__init__(self, trader)
        
    def _orderFunc(self):
        threshold = self._threshold
        value = self._signalFunc()
        side = Side.Buy  if value > threshold else\
               Side.Sell if value < -threshold else\
               None
        return (side, (self._volume(side),)) if side else None

class _Signal_Impl(SignalBase):
    
    def __init__(self, trader, params):
        self._eventGen = params.signal
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        self._signalFunc = lambda: params.signal.value
        self._volume = lambda _: params.volumeDistr()
        
        SignalBase.__init__(self, trader)

exec wrapper("Signal", 
             [('signal',        'None',                         'IObservable'),  
              ('threshold',     '0.7',                          'non_negative'),
              ('orderFactory',  'order.Market.T',               'Side -> Volume -> IOrder'),
              ('volumeDistr',   'mathutils.rnd.expovariate(1.)','() -> Volume')], register=False)

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = lambda _: params.volumeDistr()
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        
        price = observable.Price(trader.orderBook)
        self._average1 = observable.Fold(price, params.average1)
        self._average2 = observable.Fold(price, params.average2)
        
        SignalBase.__init__(self, trader)
        
    def _signalFunc(self):
        avg1 = self._average1.value
        avg2 = self._average2.value
        return avg1 - avg2 if avg1 is not None and avg2 is not None else None 

exec wrapper("TwoAverages", 
             [('average1',              'mathutils.ewma(alpha = 0.15)',  'IUpdatableValue'),
              ('average2',              'mathutils.ewma(alpha = 0.015)', 'IUpdatableValue'),
              ('threshold',             '0.',                            'non_negative'), 
              ('orderFactory',          'order.Market.T',                'Side -> Volume -> IOrder'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')])

class _TrendFollower_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = lambda _: params.volumeDistr()
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        
        trend = observable.Fold(observable.Price(trader.orderBook), 
                                observable.derivative(params.average))
        self._signalFunc = lambda: trend.value
        
        SignalBase.__init__(self, trader)

exec wrapper('TrendFollower', 
             [('average',                'mathutils.ewma(alpha = 0.15)',  'IUpdatableValue'),
              ('threshold',              '0.',                            'non_negative'), 
              ('orderFactory',           'order.Market.T',                'Side -> Volume -> IOrder'),
              ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',            'mathutils.rnd.expovariate(1.)', '() -> Volume')])