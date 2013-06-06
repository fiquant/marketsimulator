from marketsim.types import *
from marketsim import (Event, order, mathutils, types, meta, 
                       registry, signal, bind, signal)
from _generic import Generic
from _two_sides import TwoSides

from _wrap import wrapper2

class SignalBase(TwoSides):
    
    def _orderFunc(self):
        threshold = self.threshold
        value = self._signalFunc()
        side =  None if (value is None or abs(value) <= self.threshold) \
                else (Side.Buy if value > 0 else Side.Sell)
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
                      signal to be listened to (default: RandomWalk)
                      
                 |orderFactory| 
                     order factory function (default: order.Market.T)
                     
                 |threshold| 
                     threshold when the trader starts to act (default: 0.7)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [('signal',        'signal.RandomWalk()',          'IObservable'),  
              ('threshold',     '0.7',                          'non_negative'),
              ('orderFactory',  'order.MarketFactory',          'Side -> Volume -> IOrder'),
              ('volumeDistr',   'mathutils.rnd.expovariate(1.)','() -> Volume')])


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
    
    def bind(self, context):
        self.scheduler = context.world
        
    def __call__(self):
        value = self.source()
        side =  None if (value is None or abs(value) <= self.threshold) \
                else (Side.Buy if value > 0 else Side.Sell)
        return side
    
@registry.expose(["Generic", 'Signal'], args = ())
def SignalEx(signal         = signal.RandomWalk(), 
             threshold      = 0., 
             orderFactory   = order.MarketFactory, 
             volumeDistr    = mathutils.rnd.expovariate(1.)):
    
    r = Generic(sideFunc     = SignalSide(signal, threshold),
                volumeFunc   = volumeDistr, 
                orderFactory = orderFactory, 
                eventGen     = signal)  
    
    return r