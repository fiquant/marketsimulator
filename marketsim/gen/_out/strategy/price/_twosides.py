# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
@registry.expose(["Price function", "MarketMaker"])
class TwoSides_strategypriceMarketMaker(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.event._event import Event
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out.strategy.price._marketmaker import MarketMaker_FloatFloat as _strategy_price_MarketMaker_FloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketMaker_FloatFloat())
        self.impl = self.getImpl()
        
        self.on_order_created = Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketMaker
    }
    
    
    def __repr__(self):
        return "MarketMaker(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
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
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
        rtti.typecheck(MarketMaker, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
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
        from marketsim.gen._out.strategy.price._oneside import OneSide_strategypriceMarketMakerSideFloat as _strategy_price_OneSide_strategypriceMarketMakerSideFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim import deref_opt
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_price_OneSide_strategypriceMarketMakerSideFloat(self.x,deref_opt(_side_Sell_()),1.0)),deref_opt(_strategy_price_OneSide_strategypriceMarketMakerSideFloat(self.x,deref_opt(_side_Buy_()),-1.0))))
    
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
from marketsim.gen._out.strategy.price._marketdata import MarketData
@registry.expose(["Price function", "MarketData"])
class TwoSides_strategypriceMarketData(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.price._marketdata import MarketData_StringStringStringFloatFloat as _strategy_price_MarketData_StringStringStringFloatFloat
        from marketsim.gen._out.event._event import Event
        from marketsim import _
        from marketsim import event
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketData_StringStringStringFloatFloat())
        self.impl = self.getImpl()
        
        self.on_order_created = Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData
    }
    
    
    def __repr__(self):
        return "MarketData(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
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
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.strategy.price._marketdata import MarketData
        rtti.typecheck(MarketData, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
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
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.strategy.price._oneside import OneSide_strategypriceMarketDataSideFloat as _strategy_price_OneSide_strategypriceMarketDataSideFloat
        from marketsim import deref_opt
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_price_OneSide_strategypriceMarketDataSideFloat(self.x,deref_opt(_side_Sell_()),1.0)),deref_opt(_strategy_price_OneSide_strategypriceMarketDataSideFloat(self.x,deref_opt(_side_Buy_()),-1.0))))
    
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
    
def TwoSides(x = None): 
    from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
    from marketsim.gen._out.strategy.price._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketMaker):
        return TwoSides_strategypriceMarketMaker(x)
    if x is None or rtti.can_be_casted(x, MarketData):
        return TwoSides_strategypriceMarketData(x)
    raise Exception('Cannot find suitable overload for TwoSides('+str(x) +':'+ str(type(x))+')')
