from marketsim.ops._all import Observable
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Signal"])
class Signal_IObservableFloatFloat(Observable[Side]):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[Side].__init__(self)
        self.signal = signal if signal is not None else _const_Float(0.0)
        self.threshold = threshold if threshold is not None else 0.7
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signal' : IObservablefloat,
        'threshold' : float
    }
    def __repr__(self):
        return "Signal(%(signal)s, %(threshold)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        return _ops_Condition_IObservableBooleanSideIObservableSide(_ops_Greater_IObservableFloatFloat(self.signal,_constant_Float(self.threshold)),_side_Buy_(),_ops_Condition_IObservableBooleanSideSide(_ops_Less_IObservableFloatFloat(self.signal,_constant_Float((0-self.threshold))),_side_Sell_(),_side_Nothing_()))
    
from marketsim.ops._all import Observable
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Signal"])
class Signal_FloatFloat(Observable[Side]):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._side import Side
        from marketsim import event
        Observable[Side].__init__(self)
        self.signal = signal if signal is not None else _constant_Float(0.0)
        self.threshold = threshold if threshold is not None else 0.7
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signal' : IFunctionfloat,
        'threshold' : float
    }
    def __repr__(self):
        return "Signal(%(signal)s, %(threshold)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        return _ops_Condition_BooleanSideSide(_ops_Greater_FloatFloat(self.signal,_constant_Float(self.threshold)),_side_Buy_(),_ops_Condition_BooleanSideSide(_ops_Less_FloatFloat(self.signal,_constant_Float((0-self.threshold))),_side_Sell_(),_side_Nothing_()))
    
def Signal(signal = None,threshold = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if signal is None or rtti.can_be_casted(signal, IObservablefloat):
        if threshold is None or rtti.can_be_casted(threshold, float):
            return Signal_IObservableFloatFloat(signal,threshold)
    if signal is None or rtti.can_be_casted(signal, IFunctionfloat):
        if threshold is None or rtti.can_be_casted(threshold, float):
            return Signal_FloatFloat(signal,threshold)
    raise Exception('Cannot find suitable overload for Signal('+str(signal) +':'+ str(type(signal))+','+str(threshold) +':'+ str(type(threshold))+')')
