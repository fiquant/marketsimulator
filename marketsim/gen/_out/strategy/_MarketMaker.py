from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import context
@registry.expose(["Strategy", "MarketMaker"])
class MarketMaker_FloatFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, delta = None, volume = None):
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.delta = delta if delta is not None else 1.0
        self.volume = volume if volume is not None else 20.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'delta' : float,
        'volume' : float
    }
    def __repr__(self):
        return "MarketMaker(%(delta)s, %(volume)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._exp import Exp_Float as _math_Exp_Float
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.math._atan import Atan_Float as _math_Atan_Float
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueFloat as _orderbook_SafeSidePrice_IOrderQueueFloat
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(deref_opt(_side_Sell_()),deref_opt(_constant_Float((self.volume*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_orderbook_SafeSidePrice_IOrderQueueFloat(deref_opt(_orderbook_Asks_IOrderBook()),deref_opt(_constant_Float((100+self.delta))))),deref_opt(_math_Exp_Float(deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Atan_Float(deref_opt(_trader_Position_IAccount()))),deref_opt(_constant_Int(1000)))))))),0.9)))))),deref_opt(_constant_Float(self.volume)))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0)))))),deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(deref_opt(_side_Buy_()),deref_opt(_constant_Float((self.volume*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_orderbook_SafeSidePrice_IOrderQueueFloat(deref_opt(_orderbook_Bids_IOrderBook()),deref_opt(_constant_Float((100-self.delta))))),deref_opt(_math_Exp_Float(deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Atan_Float(deref_opt(_trader_Position_IAccount()))),deref_opt(_constant_Int(1000)))))))),0.9)))))),deref_opt(_constant_Float(self.volume)))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MarketMaker(delta = None,volume = None): 
    from marketsim import rtti
    if delta is None or rtti.can_be_casted(delta, float):
        if volume is None or rtti.can_be_casted(volume, float):
            return MarketMaker_FloatFloat(delta,volume)
    raise Exception('Cannot find suitable overload for MarketMaker('+str(delta) +':'+ str(type(delta))+','+str(volume) +':'+ str(type(volume))+')')
