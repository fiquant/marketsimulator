# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Price function", "isLossTooHigh"])
class isLossTooHigh_IObservableFloat(Observablebool):
    """ 
    """ 
    def __init__(self, lossFactor = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import _
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim import event
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_const_Float(0.2))
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lossFactor' : IObservablefloat
    }
    
    
    def __repr__(self):
        return "isLossTooHigh(%(lossFactor)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
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
        
        self.lossFactor.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        rtti.typecheck(IObservablefloat, self.lossFactor)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.lossFactor.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
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
        from marketsim.gen._out._false import false_ as _false_
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableBooleanBoolean as _ops_Condition_IObservableBooleanIObservableBooleanBoolean
        from marketsim.gen._out.ops._div import Div_IObservableFloatIObservableFloat as _ops_Div_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableBooleanIObservableBoolean as _ops_Condition_IObservableBooleanIObservableBooleanIObservableBoolean
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.trader._pershareprice import PerSharePrice_IAccount as _trader_PerSharePrice_IAccount
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.ops._less import Less_IObservableFloatIObservableFloat as _ops_Less_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIObservableFloat as _ops_Greater_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._sub import Sub_FloatIObservableFloat as _ops_Sub_FloatIObservableFloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanIObservableBooleanIObservableBoolean(deref_opt(_ops_Greater_IObservableFloatFloat(deref_opt(_trader_Position_IAccount()),deref_opt(_constant_Int(0)))),deref_opt(_ops_Greater_IObservableFloatIObservableFloat(deref_opt(_trader_PerSharePrice_IAccount()),deref_opt(_ops_Div_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook()))),deref_opt(_ops_Sub_FloatIObservableFloat(deref_opt(_constant_Int(1)),self.lossFactor)))))),deref_opt(_ops_Condition_IObservableBooleanIObservableBooleanBoolean(deref_opt(_ops_Less_IObservableFloatFloat(deref_opt(_trader_Position_IAccount()),deref_opt(_constant_Int(0)))),deref_opt(_ops_Less_IObservableFloatIObservableFloat(deref_opt(_trader_PerSharePrice_IAccount()),deref_opt(_ops_Mul_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook()))),deref_opt(_ops_Sub_FloatIObservableFloat(deref_opt(_constant_Int(1)),self.lossFactor)))))),deref_opt(_false_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Price function", "isLossTooHigh"])
class isLossTooHigh_Float(Observablebool):
    """ 
    """ 
    def __init__(self, lossFactor = None):
        from marketsim import _
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_constant_Float(0.2))
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lossFactor' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "isLossTooHigh(%(lossFactor)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
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
        
        self.lossFactor.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.lossFactor)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.lossFactor.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
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
        from marketsim.gen._out._false import false_ as _false_
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableBooleanBoolean as _ops_Condition_IObservableBooleanIObservableBooleanBoolean
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableBooleanIObservableBoolean as _ops_Condition_IObservableBooleanIObservableBooleanIObservableBoolean
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.trader._pershareprice import PerSharePrice_IAccount as _trader_PerSharePrice_IAccount
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.ops._less import Less_IObservableFloatIObservableFloat as _ops_Less_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIObservableFloat as _ops_Greater_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanIObservableBooleanIObservableBoolean(deref_opt(_ops_Greater_IObservableFloatFloat(deref_opt(_trader_Position_IAccount()),deref_opt(_constant_Int(0)))),deref_opt(_ops_Greater_IObservableFloatIObservableFloat(deref_opt(_trader_PerSharePrice_IAccount()),deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook()))),deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Int(1)),self.lossFactor)))))),deref_opt(_ops_Condition_IObservableBooleanIObservableBooleanBoolean(deref_opt(_ops_Less_IObservableFloatFloat(deref_opt(_trader_Position_IAccount()),deref_opt(_constant_Int(0)))),deref_opt(_ops_Less_IObservableFloatIObservableFloat(deref_opt(_trader_PerSharePrice_IAccount()),deref_opt(_ops_Mul_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook()))),deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Int(1)),self.lossFactor)))))),deref_opt(_false_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def isLossTooHigh(lossFactor = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if lossFactor is None or rtti.can_be_casted(lossFactor, IObservablefloat):
        return isLossTooHigh_IObservableFloat(lossFactor)
    if lossFactor is None or rtti.can_be_casted(lossFactor, IFunctionfloat):
        return isLossTooHigh_Float(lossFactor)
    raise Exception('Cannot find suitable overload for isLossTooHigh('+str(lossFactor) +':'+ str(type(lossFactor))+')')
