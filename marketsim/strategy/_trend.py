from marketsim.types import *
from marketsim import (orderbook, Event, observable, scheduler, order, mathutils, types, meta, 
                       registry, signal, bind)
from _basic import TwoSides, Strategy, Generic
from _wrap import wrapper2

class SignalBase(TwoSides):
    
    def _orderFunc(self):
        threshold = self._threshold
        value = self._signalFunc()
        side = Side.Buy  if value > threshold else\
               Side.Sell if value < -threshold else\
               None
        return (side, (self._volume(side),)) if side else None


class _Signal_Impl(SignalBase):

    @property
    def _eventGen(self):    
        return self.signal
    
    @property
    def _threshold(self):
        return self.threshold
    
    @property 
    def _orderFactoryT(self): 
        return self.orderFactory

    @property
    def _signalFunc(self): 
        return self.signal
    
    @property
    def _volume(self):
        return bind.Method(self, 'volumeDistr')

exec wrapper2("Signal", 
             """ Signal strategy listens to some discrete signal
                 and when the signal becomes more than some threshold the strategy starts to buy. 
                 When the signal gets lower than -threshold the strategy starts to sell. 
                 
                 It has following parameters:

                 |signal| 
                      signal to be listened to
                      
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                     
                 |threshold| 
                     threshold when the trader starts to act (default: 0.7)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('signal',        'None',                         'IObservable'),  
              ('threshold',     '0.7',                          'non_negative'),
              ('orderFactory',  'order.MarketFactory',          'Side -> Volume -> IOrder'),
              ('volumeDistr',   'mathutils.rnd.expovariate(1.)','() -> Volume')], register=False)


class SignalSide(object):
    """ Function determining side of a trade given a signal value.
        If signal value is greater than *threshold*, returns *Side.Buy*
        If signal value is lower than *-threshold*, returns *Side.Sell*
        Otherwise returns *None*
    """
    
    def __init__(self, source, threshold = 0):
        self.source = source
        self.threshold = threshold
        self._alias = ["SignalSide"]
        
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
    """ Returns signal value
    
        Note: we need it since current type system doesn't allow to cast IObservable to () -> float
    """
    
    def __init__(self, signal):
        self.signal = signal
        
    _properties = { 'signal' : types.IObservable }
    _types = [meta.function((), float)]
        
    def __call__(self):
        return self.signal.value

class SignalEvent(Event):
    """ Represents event about signal value change
    
        Note: we need it since current type system doesn't allow to cast IObservable to Event
    """
    
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
    
    r._alias = ["Generic", 'Signal']
    
    return r

registry.startup.append(lambda instance: instance.insert(SignalEx(signal.RandomWalk())))

class _TwoAverages_Impl(SignalBase):
    
    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        SignalBase.__init__(self)
        
    _internals = ['_eventGen']
        
    @property
    def _volume(self):
        return bind.Method(self, 'volumeDistr')
    
    @property
    def _threshold(self): 
        return self.threshold
    
    @property
    def _orderFactoryT(self): 
        return self.orderFactory
        
    def bind(self, context):
        SignalBase.bind(self, context)
        price = observable.Price(self._trader.orderBook)
        self._average1 = observable.Fold(price, self.average1, self._scheduler)
        self._average2 = observable.Fold(price, self.average2, self._scheduler)
        
    def _signalFunc(self):
        avg1 = self._average1.value
        avg2 = self._average2.value
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

  
def TwoAveragesEx(average1 = mathutils.ewma(alpha = 0.15), 
                  average2 = mathutils.ewma(alpha = 0.015), 
                  threshold             = 0, 
                  orderFactory          = order.MarketFactory, 
                  creationIntervalDistr = mathutils.rnd.expovariate(1.), 
                  volumeDistr           = mathutils.rnd.expovariate(1.)):
    
    orderBook = orderbook.OfTrader()
    price = observable.Price(orderBook)
    
    r = Generic(orderFactory= orderFactory, 
                volumeFunc  = volumeDistr,
                eventGen    = scheduler.Timer(creationIntervalDistr),
                sideFunc    = SignalSide(
                                 mathutils.sub(
                                     observable.Fold(price, average1),
                                     observable.Fold(price, average2)),
                                 threshold))
    
    r._alias = ["Generic", 'TwoAverages']
    
    return r

class _TrendFollower_Impl(SignalBase):

    def __init__(self):
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        SignalBase.__init__(self)
        
    _internals = ['_eventGen']
        
    @property
    def _volume(self):
        return bind.Method(self, 'volumeDistr')
    
    @property
    def _threshold(self):
        return self.threshold
    
    @property
    def _orderFactoryT(self):
        return self.orderFactory
        
    def bind(self, context):
        SignalBase.bind(self, context)
        self._signalFunc = observable.Fold(observable.Price(self._trader.orderBook), 
                                           observable.derivative(self.average), 
                                           self._scheduler)

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
    
    r._alias = ["Generic", 'TrendFollower']
    
    return r
    
