from marketsim.types import *
from marketsim import Event, observable, scheduler, order, mathutils, types, meta, registry, signal, Method
from _basic import TwoSides, Strategy, Generic
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
        self._signalFunc = params.signal
        self._volume = Method(params, 'volumeDistr')
        
        SignalBase.__init__(self, trader)

exec wrapper("Signal", 
             [('signal',        'None',                         'IObservable'),  
              ('threshold',     '0.7',                          'non_negative'),
              ('orderFactory',  'order.MarketFactory',          'Side -> Volume -> IOrder'),
              ('volumeDistr',   'mathutils.rnd.expovariate(1.)','() -> Volume')], register=False)

class SignalSide(object):
    
    def __init__(self, source, threshold = 0):
        self.source = source
        self.threshold = threshold
        self._alias = "SignalSide"
        
    _properties = { 'source'    : meta.function((), float),
                    'threshold' : float }
    
    _types = [meta.function((), Side)]
        
    def __call__(self):
        value = self.source()
        side = Side.Buy  if value > self.threshold else\
               Side.Sell if value < -self.threshold else\
               None
        return side
    
class SignalValue(object):
    
    def __init__(self, signal):
        self.signal = signal
        
    _properties = { 'signal' : types.IObservable }
    _types = [meta.function((), float)]
        
    def __call__(self):
        return self.signal()

class SignalEvent(Event):
    
    def __init__(self, signal):
        Event.__init__(self)
        self.signal = signal
        self.signal.advise(self)
        
    def schedule(self):
        self.signal.schedule()
        
    def dispose(self):
        self.signal.unadvise(self)
        
    _properties = { 'signal' : types.IObservable }
        

def SignalEx(signal, 
             threshold      = 0, 
             orderFactory   = order.MarketFactory, 
             volumeDistr    = mathutils.rnd.expovariate(1.)):
    
    r = Generic(sideFunc     = SignalSide(SignalValue(signal), threshold),
                volumeFunc   = volumeDistr, 
                orderFactory = orderFactory, 
                eventGen     = SignalEvent(signal))  
    
    r._alias = 'SignalEx'
    
    return r

registry.startup.append(lambda instance: instance.insert(SignalEx(signal.RandomWalk())))
  

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = Method(params, 'volumeDistr')
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
              ('orderFactory',          'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',           'mathutils.rnd.expovariate(1.)', '() -> Volume')])

class _TrendFollower_Impl(SignalBase):
    
    def __init__(self, trader, params):
        
        self._eventGen = scheduler.Timer(params.creationIntervalDistr)
        self._volume = Method(params, 'volumeDistr')
        self._threshold = params.threshold
        self._orderFactoryT = params.orderFactory
        
        trend = observable.Fold(observable.Price(trader.orderBook), 
                                observable.derivative(params.average))
        self._signalFunc = trend
        
        SignalBase.__init__(self, trader)

exec wrapper('TrendFollower', 
             [('average',                'mathutils.ewma(alpha = 0.15)',  'IUpdatableValue'),
              ('threshold',              '0.',                            'non_negative'), 
              ('orderFactory',           'order.MarketFactory',           'Side -> Volume -> IOrder'),
              ('creationIntervalDistr',  'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
              ('volumeDistr',            'mathutils.rnd.expovariate(1.)', '() -> Volume')])