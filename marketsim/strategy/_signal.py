from marketsim.types import *
from marketsim import (Event, order, mathutils, types, meta, defs, Reference, 
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

class ConditionSide(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    _types = [meta.function((), Side)]
        
    _properties = [('cond', meta.function((), bool)), 
                   ('ifpart', meta.function((), Side)), 
                   ('elsepart', meta.function((), Side))]
        
    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()
    
class less_float(object):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    _types = [meta.function((), bool)]
    
    _properties = [('lhs', meta.function((), float)), 
                   ('rhs', meta.function((), float))]
    
    def __call__(self):
        return self.lhs() < self.rhs()
    
class none_side(object):
    
    def __call__(self):
        return None
    
    _types = [meta.function((), Side)]
    
from _lp_side import ConstantSide
    
def SignalSide(source, threshold = 0):
    
    return defs(ConditionSide(
                    less_float(
                        Reference('threshold'), 
                        Reference('source')), 
                    ConstantSide(Side.Buy), 
                        ConditionSide(
                            less_float(
                                Reference('source'), 
                                mathutils.negate(
                                    Reference('threshold'))), 
                        ConstantSide(Side.Sell), 
                        none_side())), 
                { 'source'    : source, 
                  'threshold' : mathutils.constant(threshold) })
    
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