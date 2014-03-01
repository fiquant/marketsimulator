from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim.gen._out.strategy._marketdata import MarketData
from marketsim import context
@registry.expose(["Strategy", "OneSide"])
class OneSide_strategyMarketDataIObservableSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out.strategy._marketdata import MarketData_StringStringStringFloatFloat as _strategy_MarketData_StringStringStringFloatFloat
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_MarketData_StringStringStringFloatFloat())
        self.side = side if side is not None else deref_opt(_side_observableSell_())
        self.sign = sign if sign is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData,
        'side' : IObservableSide,
        'sign' : float
    }
    def __repr__(self):
        return "OneSide(%(x)s, %(side)s, %(sign)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._delta import Delta_strategyMarketData as _strategy_Delta_strategyMarketData
        from marketsim import deref_opt
        from marketsim.gen._out.ops._add import Add_IObservableFloatFloat as _ops_Add_IObservableFloatFloat
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.strategy._end import End_strategyMarketData as _strategy_End_strategyMarketData
        from marketsim.gen._out.strategy._start import Start_strategyMarketData as _strategy_Start_strategyMarketData
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.strategy._volume import Volume_strategyMarketData as _strategy_Volume_strategyMarketData
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.strategy._ticker import Ticker_strategyMarketData as _strategy_Ticker_strategyMarketData
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_Volume_strategyMarketData(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Add_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(deref_opt(_strategy_Ticker_strategyMarketData(self.x)),deref_opt(_strategy_Start_strategyMarketData(self.x)),deref_opt(_strategy_End_strategyMarketData(self.x)))),deref_opt(_constant_Float((deref_opt(_strategy_Delta_strategyMarketData(self.x))*self.sign))))))))),deref_opt(_constant_Float(deref_opt(_strategy_Volume_strategyMarketData(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import registry
from marketsim.gen._out.strategy._marketdata import MarketData
from marketsim import context
@registry.expose(["Strategy", "OneSide"])
class OneSide_strategyMarketDataSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy._marketdata import MarketData_StringStringStringFloatFloat as _strategy_MarketData_StringStringStringFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_MarketData_StringStringStringFloatFloat())
        self.side = side if side is not None else deref_opt(_side_Sell_())
        self.sign = sign if sign is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData,
        'side' : IFunctionSide,
        'sign' : float
    }
    def __repr__(self):
        return "OneSide(%(x)s, %(side)s, %(sign)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._delta import Delta_strategyMarketData as _strategy_Delta_strategyMarketData
        from marketsim import deref_opt
        from marketsim.gen._out.ops._add import Add_IObservableFloatFloat as _ops_Add_IObservableFloatFloat
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.strategy._end import End_strategyMarketData as _strategy_End_strategyMarketData
        from marketsim.gen._out.strategy._start import Start_strategyMarketData as _strategy_Start_strategyMarketData
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.strategy._volume import Volume_strategyMarketData as _strategy_Volume_strategyMarketData
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.strategy._ticker import Ticker_strategyMarketData as _strategy_Ticker_strategyMarketData
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_Volume_strategyMarketData(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Add_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(deref_opt(_strategy_Ticker_strategyMarketData(self.x)),deref_opt(_strategy_Start_strategyMarketData(self.x)),deref_opt(_strategy_End_strategyMarketData(self.x)))),deref_opt(_constant_Float((deref_opt(_strategy_Delta_strategyMarketData(self.x))*self.sign))))))))),deref_opt(_constant_Float(deref_opt(_strategy_Volume_strategyMarketData(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def OneSide(x = None,side = None,sign = None): 
    from marketsim.gen._out._iobservable._iobservableside import IObservableSide
    from marketsim import rtti
    from marketsim.gen._out._side import Side
    from marketsim.gen._out.strategy._marketdata import MarketData
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    if x is None or rtti.can_be_casted(x, MarketData):
        if side is None or rtti.can_be_casted(side, IObservableSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategyMarketDataIObservableSideFloat(x,side,sign)
    if x is None or rtti.can_be_casted(x, MarketData):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategyMarketDataSideFloat(x,side,sign)
    raise Exception('Cannot find suitable overload for OneSide('+str(x) +':'+ str(type(x))+','+str(side) +':'+ str(type(side))+','+str(sign) +':'+ str(type(sign))+')')
