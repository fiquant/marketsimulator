from marketsim.types import *
from marketsim import (Event, order, mathutils, types, meta, defs, _, 
                       registry, signal, bind, signal)
from _periodic import Periodic
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

class Condition_Impl(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

condition_tmpl = """
class Condition%(T)s(Condition_Impl):

    def __init__(self, cond, ifpart, elsepart):
        Condition_Impl.__init__(self, cond, ifpart, elsepart)
        self._alias = ['Condition[%(T)s]']
        
    _types = [meta.function((), %(T)s)]
        
    _properties = [('cond', meta.function((), bool)), 
                   ('ifpart', meta.function((), %(T)s)), 
                   ('elsepart', meta.function((), %(T)s))]
"""  

for t in ['Side', 'float']:
    exec condition_tmpl % { 'T' : t }   
    
class NotNoneFloat(mathutils.FloatFunction):
    
    def __init__(self, source, ifnone):
        self.source = source
        self.ifnone = ifnone
    
    _properties = { 'source' : types.IFloatFunction, 
                    'ifnone' : types.IFloatFunction}
        
    def __call__(self):
        v = self.source()
        return v if v is not None else self.ifnone()
    
class less_float(mathutils.FloatFunction):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    _types = [meta.function((), bool)]
    
    _properties = [('lhs', types.IFloatFunction), 
                   ('rhs', types.IFloatFunction)]
    
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
                        _.threshold, 
                        _.source), 
                    ConstantSide(Side.Buy), 
                        ConditionSide(
                            less_float(
                                _.source, 
                                mathutils.negate(_.threshold)), 
                            ConstantSide(Side.Sell), 
                            none_side())), 
                { 'source'    : source, 
                  'threshold' : mathutils.constant(threshold) })
    
@registry.expose(["Periodic", 'Signal'], args = ())
def SignalEx(signal         = signal.RandomWalk(), 
             threshold      = 0., 
             orderFactory   = order.MarketFactory, 
             volumeDistr    = mathutils.rnd.expovariate(1.)):
    
    return defs(
        Periodic(sideFunc     = SignalSide(_.signal, threshold),
                 volumeFunc   = volumeDistr, 
                 orderFactory = orderFactory, 
                 eventGen     = _.signal),
        {"signal" : signal })  
