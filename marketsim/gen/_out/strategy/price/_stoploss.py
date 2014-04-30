# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Price function", "StopLoss"])
class StopLoss_ISuspendableStrategyIObservableFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, inner = None, lossFactor = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim import deref_opt
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_const_Float(0.2))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
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
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.inner.bind_ex(self._ctx_ex)
        self.lossFactor.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.inner.reset_ex(generation)
        self.lossFactor.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
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
    
    @property
    def suspended(self):
        return self.inner.suspended
    
    def set_suspended(self, value):
        self.inner.suspended = value
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Price function", "StopLoss"])
class StopLoss_ISuspendableStrategyFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, inner = None, lossFactor = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_constant_Float(0.2))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
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
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.inner.bind_ex(self._ctx_ex)
        self.lossFactor.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.inner.reset_ex(generation)
        self.lossFactor.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
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
    
    @property
    def suspended(self):
        return self.inner.suspended
    
    def set_suspended(self, value):
        self.inner.suspended = value
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
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
