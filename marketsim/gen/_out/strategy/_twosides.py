from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out.strategy._marketmaker import MarketMaker
from marketsim import context
@registry.expose(["Strategy", "TwoSides"])
class TwoSides_strategyMarketMaker(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy._marketmaker import MarketMaker_FloatFloat as _strategy_MarketMaker_FloatFloat
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_MarketMaker_FloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketMaker
    }
    def __repr__(self):
        return "TwoSides(%(x)s)" % self.__dict__
    
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
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.strategy._oneside import OneSide_strategyMarketMakerSideFloat as _strategy_OneSide_strategyMarketMakerSideFloat
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_OneSide_strategyMarketMakerSideFloat(self.x,deref_opt(_side_Sell_()),1.0)),deref_opt(_strategy_OneSide_strategyMarketMakerSideFloat(self.x,deref_opt(_side_Buy_()),-1.0))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out.strategy._marketdata import MarketData
from marketsim import context
@registry.expose(["Strategy", "TwoSides"])
class TwoSides_strategyMarketData(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy._marketdata import MarketData_StringStringStringFloatFloat as _strategy_MarketData_StringStringStringFloatFloat
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_MarketData_StringStringStringFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData
    }
    def __repr__(self):
        return "TwoSides(%(x)s)" % self.__dict__
    
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
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.strategy._oneside import OneSide_strategyMarketDataSideFloat as _strategy_OneSide_strategyMarketDataSideFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_OneSide_strategyMarketDataSideFloat(self.x,deref_opt(_side_Sell_()),1.0)),deref_opt(_strategy_OneSide_strategyMarketDataSideFloat(self.x,deref_opt(_side_Buy_()),-1.0))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def TwoSides(x = None): 
    from marketsim.gen._out.strategy._marketmaker import MarketMaker
    from marketsim.gen._out.strategy._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketMaker):
        return TwoSides_strategyMarketMaker(x)
    if x is None or rtti.can_be_casted(x, MarketData):
        return TwoSides_strategyMarketData(x)
    raise Exception('Cannot find suitable overload for TwoSides('+str(x) +':'+ str(type(x))+')')
