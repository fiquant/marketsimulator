from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Signal"])
class Signal_IObservableFloatFloat(ObservableSide):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        ObservableSide.__init__(self)
        self.signal = signal if signal is not None else call(_const_Float,0.0)
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
        from marketsim import call
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        return call(_ops_Condition_IObservableBooleanSideIObservableSide,call(_ops_Greater_IObservableFloatFloat,self.signal,call(_constant_Float,self.threshold)),call(_side_Buy_,),call(_ops_Condition_IObservableBooleanSideSide,call(_ops_Less_IObservableFloatFloat,self.signal,call(_constant_Float,(0-self.threshold))),call(_side_Sell_,),call(_side_Nothing_,)))
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._side import Side
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Signal"])
class Signal_FloatFloat(ObservableSide):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._side import Side
        from marketsim import call
        from marketsim import event
        ObservableSide.__init__(self)
        self.signal = signal if signal is not None else call(_constant_Float,0.0)
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
        from marketsim import call
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        return call(_ops_Condition_BooleanSideSide,call(_ops_Greater_FloatFloat,self.signal,call(_constant_Float,self.threshold)),call(_side_Buy_,),call(_ops_Condition_BooleanSideSide,call(_ops_Less_FloatFloat,self.signal,call(_constant_Float,(0-self.threshold))),call(_side_Sell_,),call(_side_Nothing_,)))
    
def Signal(signal = None,threshold = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if signal is None or rtti.can_be_casted(signal, IObservablefloat):
        if threshold is None or rtti.can_be_casted(threshold, float):
            return Signal_IObservableFloatFloat(signal,threshold)
    if signal is None or rtti.can_be_casted(signal, IFunctionfloat):
        if threshold is None or rtti.can_be_casted(threshold, float):
            return Signal_FloatFloat(signal,threshold)
    raise Exception('Cannot find suitable overload for Signal('+str(signal) +':'+ str(type(signal))+','+str(threshold) +':'+ str(type(threshold))+')')
