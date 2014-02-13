from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import float
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
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.event._after import After_IFunctionFloat as _event_After_IFunctionFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IFunctionFloatIOrderGenerator as _order_Iceberg_IFunctionFloatIOrderGenerator
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit_SideIFunctionFloat
        from marketsim.gen._out.order._floatingprice import FloatingPrice_IObservableFloatFloatIOrderGenerator as _order_FloatingPrice_IObservableFloatFloatIOrderGenerator
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.math._exp import Exp_IFunctionFloat as _math_Exp_IFunctionFloat
        from marketsim.gen._out.math._atan import Atan_IFunctionFloat as _math_Atan_IFunctionFloat
        from marketsim.gen._out.ops._div import Div_IFunctionFloatIFunctionFloat as _ops_Div_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatIFunctionFloat as _observable_OnEveryDt_FloatIFunctionFloat
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueIFunctionFloat as _orderbook_SafeSidePrice_IOrderQueueIFunctionFloat
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim.gen._out.ops._div import Div_IObservableFloatIFunctionFloat as _ops_Div_IObservableFloatIFunctionFloat
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.strategy._generic import Generic_IOrderGeneratorIEvent as _strategy_Generic_IOrderGeneratorIEvent
        return _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(_strategy_Generic_IOrderGeneratorIEvent(_order_Iceberg_IFunctionFloatIOrderGenerator(_constant_Float(self.volume),_order_FloatingPrice_IObservableFloatFloatIOrderGenerator(_observable_BreaksAtChanges_IObservableFloat(_observable_OnEveryDt_FloatIFunctionFloat(0.9,_ops_Div_IObservableFloatIFunctionFloat(_orderbook_SafeSidePrice_IOrderQueueIFunctionFloat(_orderbook_Asks_IOrderBook(),_constant_Float((100+self.delta))),_math_Exp_IFunctionFloat(_ops_Div_IFunctionFloatIFunctionFloat(_math_Atan_IFunctionFloat(_trader_Position_IAccount()),_constant_Int(1000)))))),_order__curried_price_Limit_SideIFunctionFloat(_side_Sell_(),_constant_Float((self.volume*1000))))),_event_After_IFunctionFloat(_constant_Float(0.0))),_strategy_Generic_IOrderGeneratorIEvent(_order_Iceberg_IFunctionFloatIOrderGenerator(_constant_Float(self.volume),_order_FloatingPrice_IObservableFloatFloatIOrderGenerator(_observable_BreaksAtChanges_IObservableFloat(_observable_OnEveryDt_FloatIFunctionFloat(0.9,_ops_Div_IObservableFloatIFunctionFloat(_orderbook_SafeSidePrice_IOrderQueueIFunctionFloat(_orderbook_Bids_IOrderBook(),_constant_Float((100-self.delta))),_math_Exp_IFunctionFloat(_ops_Div_IFunctionFloatIFunctionFloat(_math_Atan_IFunctionFloat(_trader_Position_IAccount()),_constant_Int(1000)))))),_order__curried_price_Limit_SideIFunctionFloat(_side_Buy_(),_constant_Float((self.volume*1000))))),_event_After_IFunctionFloat(_constant_Float(0.0))))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MarketMaker(delta = None,volume = None): 
    from marketsim import float
    from marketsim import rtti
    if delta is None or rtti.can_be_casted(delta, float):
        if volume is None or rtti.can_be_casted(volume, float):
            return MarketMaker_FloatFloat(delta,volume)
    raise Exception('Cannot find suitable overload for MarketMaker('+str(delta)+','+str(volume)+')')
