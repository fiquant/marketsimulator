from marketsim.types import *
from marketsim import (Event, order, mathutils, types, meta, 
                       registry, signal, bind)
from _generic import Generic
from _two_sides import TwoSides

from _wrap import wrapper2

class SignalBase(TwoSides):
    
    def _orderFunc(self):
        threshold = self.threshold
        value = self._signalFunc()
        side = Side.Buy  if value > threshold else\
               Side.Sell if value < -threshold else\
               None
        return (side, (self._volume(side),)) if side else None

    
    def _volume(self, side):
        return self.volumeDistr()

class _Signal_Impl(SignalBase):

    @property
    def _eventGen(self):    
        return self.signal
    
    @property
    def _signalFunc(self): 
        return self.signal
    
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
