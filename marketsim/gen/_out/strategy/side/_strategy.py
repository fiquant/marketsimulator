from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysideMeanReversionIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_FloatIOrderBook as _strategy_side_MeanReversion_FloatIOrderBook
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_FloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysideMeanReversion as _strategy_side_Side_strategysideMeanReversion
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysideMeanReversion(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysideFundamentalValueIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysideFundamentalValue as _strategy_side_Side_strategysideFundamentalValue
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysideFundamentalValue(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysideTrendFollowerIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysideTrendFollower as _strategy_side_Side_strategysideTrendFollower
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysideTrendFollower(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysideCrossingAveragesIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysideCrossingAverages as _strategy_side_Side_strategysideCrossingAverages
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysideCrossingAverages(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.side._signal import Signal
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysideSignalIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysideSignal as _strategy_side_Side_strategysideSignal
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysideSignal(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "Strategy"])
class Strategy_strategysidePairTradingIEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloatIOrderBook as _strategy_side_PairTrading_IOrderBookFloatIOrderBook
        from marketsim import event
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Strategy(%(x)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._side import Side_strategysidePairTrading as _strategy_side_Side_strategysidePairTrading
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Side_strategysidePairTrading(self.x)))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def Strategy(x = None,eventGen = None,orderFactory = None): 
    from marketsim import rtti
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    if x is None or rtti.can_be_casted(x, MeanReversion):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysideMeanReversionIEventSideIObservableIOrder(x,eventGen,orderFactory)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysideFundamentalValueIEventSideIObservableIOrder(x,eventGen,orderFactory)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysideTrendFollowerIEventSideIObservableIOrder(x,eventGen,orderFactory)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysideCrossingAveragesIEventSideIObservableIOrder(x,eventGen,orderFactory)
    if x is None or rtti.can_be_casted(x, Signal):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysideSignalIEventSideIObservableIOrder(x,eventGen,orderFactory)
    if x is None or rtti.can_be_casted(x, PairTrading):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
                return Strategy_strategysidePairTradingIEventSideIObservableIOrder(x,eventGen,orderFactory)
    raise Exception('Cannot find suitable overload for Strategy('+str(x) +':'+ str(type(x))+','+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+')')
