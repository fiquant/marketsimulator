# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Price function", "StopLoss"])
class StopLoss_ISuspendableStrategyIObservableFloat(ISuspendableStrategy):
    """ 
    """ 
    def __init__(self, inner = None, lossFactor = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import deref_opt
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_const_Float(0.2))
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISuspendableStrategy,
        'lossFactor' : IObservablefloat
    }
    
    
    
    
    def __repr__(self):
        return "StopLoss(%(inner)s, %(lossFactor)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.inner.bind_ex(self._ctx_ex)
        self.lossFactor.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self.impl.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.strategy.price._clearable import Clearable_ISuspendableStrategyBoolean as _strategy_price_Clearable_ISuspendableStrategyBoolean
        from marketsim.gen._out.strategy.price._islosstoohigh import isLossTooHigh_IObservableFloat as _strategy_price_isLossTooHigh_IObservableFloat
        from marketsim import deref_opt
        return deref_opt(_strategy_price_Clearable_ISuspendableStrategyBoolean(self.inner,deref_opt(_strategy_price_isLossTooHigh_IObservableFloat(self.lossFactor))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context
@registry.expose(["Price function", "StopLoss"])
class StopLoss_ISuspendableStrategyFloat(ISuspendableStrategy):
    """ 
    """ 
    def __init__(self, inner = None, lossFactor = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_constant_Float(0.2))
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISuspendableStrategy,
        'lossFactor' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "StopLoss(%(inner)s, %(lossFactor)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.inner.bind_ex(self._ctx_ex)
        self.lossFactor.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self.impl.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.strategy.price._clearable import Clearable_ISuspendableStrategyBoolean as _strategy_price_Clearable_ISuspendableStrategyBoolean
        from marketsim.gen._out.strategy.price._islosstoohigh import isLossTooHigh_Float as _strategy_price_isLossTooHigh_Float
        from marketsim import deref_opt
        return deref_opt(_strategy_price_Clearable_ISuspendableStrategyBoolean(self.inner,deref_opt(_strategy_price_isLossTooHigh_Float(self.lossFactor))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def StopLoss(inner = None,lossFactor = None): 
    from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISuspendableStrategy):
        if lossFactor is None or rtti.can_be_casted(lossFactor, IObservablefloat):
            return StopLoss_ISuspendableStrategyIObservableFloat(inner,lossFactor)
    if inner is None or rtti.can_be_casted(inner, ISuspendableStrategy):
        if lossFactor is None or rtti.can_be_casted(lossFactor, IFunctionfloat):
            return StopLoss_ISuspendableStrategyFloat(inner,lossFactor)
    raise Exception('Cannot find suitable overload for StopLoss('+str(inner) +':'+ str(type(inner))+','+str(lossFactor) +':'+ str(type(lossFactor))+')')
