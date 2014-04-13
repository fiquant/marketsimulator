# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim import context
from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "MarketMakerSide"])
class OneSide_strategypriceMarketMakerIObservableSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out.strategy.price._marketmaker import MarketMaker_FloatFloat as _strategy_price_MarketMaker_FloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketMaker_FloatFloat())
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
        'x' : MarketMaker,
        'side' : IObservableSide,
        'sign' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "MarketMakerSide(%(x)s, %(side)s, %(sign)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
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
        from marketsim.gen._out.math._atan import Atan_Float as _math_Atan_Float
        from marketsim.gen._out.orderbook._queue import Queue_IOrderBookSide as _orderbook_Queue_IOrderBookSide
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.strategy.price._delta import Delta_strategypriceMarketMaker as _strategy_price_Delta_strategypriceMarketMaker
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.math._exp import Exp_Float as _math_Exp_Float
        from marketsim.gen._out.strategy.price._volume import Volume_strategypriceMarketMaker as _strategy_price_Volume_strategypriceMarketMaker
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueFloat as _orderbook_SafeSidePrice_IOrderQueueFloat
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_price_Volume_strategypriceMarketMaker(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_orderbook_SafeSidePrice_IOrderQueueFloat(deref_opt(_orderbook_Queue_IOrderBookSide(deref_opt(_orderbook_OfTrader_IAccount()),self.side)),deref_opt(_constant_Float((100+(deref_opt(_strategy_price_Delta_strategypriceMarketMaker(self.x))*self.sign)))))),deref_opt(_math_Exp_Float(deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Atan_Float(deref_opt(_trader_Position_IAccount()))),deref_opt(_constant_Int(1000)))))))),0.9)))))),deref_opt(_constant_Float(deref_opt(_strategy_price_Volume_strategypriceMarketMaker(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
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
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim import context
from marketsim.gen._out.strategy.price._marketdata import MarketData
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "MarketDataSide"])
class OneSide_strategypriceMarketDataIObservableSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim.gen._out.strategy.price._marketdata import MarketData_StringStringStringFloatFloat as _strategy_price_MarketData_StringStringStringFloatFloat
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketData_StringStringStringFloatFloat())
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
        return "MarketDataSide(%(x)s, %(side)s, %(sign)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
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
        from marketsim.gen._out.strategy.price._ticker import Ticker_strategypriceMarketData as _strategy_price_Ticker_strategypriceMarketData
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.strategy.price._volume import Volume_strategypriceMarketData as _strategy_price_Volume_strategypriceMarketData
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.strategy.price._end import End_strategypriceMarketData as _strategy_price_End_strategypriceMarketData
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        from marketsim.gen._out.strategy.price._delta import Delta_strategypriceMarketData as _strategy_price_Delta_strategypriceMarketData
        from marketsim.gen._out.ops._add import Add_IObservableFloatFloat as _ops_Add_IObservableFloatFloat
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.strategy.price._start import Start_strategypriceMarketData as _strategy_price_Start_strategypriceMarketData
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_price_Volume_strategypriceMarketData(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Add_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(deref_opt(_strategy_price_Ticker_strategypriceMarketData(self.x)),deref_opt(_strategy_price_Start_strategypriceMarketData(self.x)),deref_opt(_strategy_price_End_strategypriceMarketData(self.x)))),deref_opt(_constant_Float((deref_opt(_strategy_price_Delta_strategypriceMarketData(self.x))*self.sign))))))))),deref_opt(_constant_Float(deref_opt(_strategy_price_Volume_strategypriceMarketData(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
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
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import context
from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "MarketMakerSide"])
class OneSide_strategypriceMarketMakerSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out.strategy.price._marketmaker import MarketMaker_FloatFloat as _strategy_price_MarketMaker_FloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketMaker_FloatFloat())
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
        'x' : MarketMaker,
        'side' : IFunctionSide,
        'sign' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "MarketMakerSide(%(x)s, %(side)s, %(sign)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
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
        from marketsim.gen._out.math._atan import Atan_Float as _math_Atan_Float
        from marketsim.gen._out.orderbook._queue import Queue_IOrderBookSide as _orderbook_Queue_IOrderBookSide
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.strategy.price._delta import Delta_strategypriceMarketMaker as _strategy_price_Delta_strategypriceMarketMaker
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.math._exp import Exp_Float as _math_Exp_Float
        from marketsim.gen._out.strategy.price._volume import Volume_strategypriceMarketMaker as _strategy_price_Volume_strategypriceMarketMaker
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueFloat as _orderbook_SafeSidePrice_IOrderQueueFloat
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_price_Volume_strategypriceMarketMaker(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_orderbook_SafeSidePrice_IOrderQueueFloat(deref_opt(_orderbook_Queue_IOrderBookSide(deref_opt(_orderbook_OfTrader_IAccount()),self.side)),deref_opt(_constant_Float((100+(deref_opt(_strategy_price_Delta_strategypriceMarketMaker(self.x))*self.sign)))))),deref_opt(_math_Exp_Float(deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Atan_Float(deref_opt(_trader_Position_IAccount()))),deref_opt(_constant_Int(1000)))))))),0.9)))))),deref_opt(_constant_Float(deref_opt(_strategy_price_Volume_strategypriceMarketMaker(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
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
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import context
from marketsim.gen._out.strategy.price._marketdata import MarketData
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "MarketDataSide"])
class OneSide_strategypriceMarketDataSideFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, side = None, sign = None):
        from marketsim.gen._out.strategy.price._marketdata import MarketData_StringStringStringFloatFloat as _strategy_price_MarketData_StringStringStringFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_MarketData_StringStringStringFloatFloat())
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
        return "MarketDataSide(%(x)s, %(side)s, %(sign)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
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
        from marketsim.gen._out.strategy.price._ticker import Ticker_strategypriceMarketData as _strategy_price_Ticker_strategypriceMarketData
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.strategy.price._volume import Volume_strategypriceMarketData as _strategy_price_Volume_strategypriceMarketData
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.strategy.price._end import End_strategypriceMarketData as _strategy_price_End_strategypriceMarketData
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        from marketsim.gen._out.strategy.price._delta import Delta_strategypriceMarketData as _strategy_price_Delta_strategypriceMarketData
        from marketsim.gen._out.ops._add import Add_IObservableFloatFloat as _ops_Add_IObservableFloatFloat
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.strategy.price._start import Start_strategypriceMarketData as _strategy_price_Start_strategypriceMarketData
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(self.side,deref_opt(_constant_Float((deref_opt(_strategy_price_Volume_strategypriceMarketData(self.x))*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Add_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(deref_opt(_strategy_price_Ticker_strategypriceMarketData(self.x)),deref_opt(_strategy_price_Start_strategypriceMarketData(self.x)),deref_opt(_strategy_price_End_strategypriceMarketData(self.x)))),deref_opt(_constant_Float((deref_opt(_strategy_price_Delta_strategypriceMarketData(self.x))*self.sign))))))))),deref_opt(_constant_Float(deref_opt(_strategy_price_Volume_strategypriceMarketData(self.x)))))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))
    
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
    
def OneSide(x = None,side = None,sign = None): 
    from marketsim import rtti
    from marketsim.gen._out._side import Side
    from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out.strategy.price._marketdata import MarketData
    from marketsim.gen._out._iobservable._iobservableside import IObservableSide
    if x is None or rtti.can_be_casted(x, MarketMaker):
        if side is None or rtti.can_be_casted(side, IObservableSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategypriceMarketMakerIObservableSideFloat(x,side,sign)
    if x is None or rtti.can_be_casted(x, MarketData):
        if side is None or rtti.can_be_casted(side, IObservableSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategypriceMarketDataIObservableSideFloat(x,side,sign)
    if x is None or rtti.can_be_casted(x, MarketMaker):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategypriceMarketMakerSideFloat(x,side,sign)
    if x is None or rtti.can_be_casted(x, MarketData):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            if sign is None or rtti.can_be_casted(sign, float):
                return OneSide_strategypriceMarketDataSideFloat(x,side,sign)
    raise Exception('Cannot find suitable overload for OneSide('+str(x) +':'+ str(type(x))+','+str(side) +':'+ str(type(side))+','+str(sign) +':'+ str(type(sign))+')')
