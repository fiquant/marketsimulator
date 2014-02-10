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
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueIFunctionFloat as _orderbook_SafeSidePrice
        from marketsim.gen._out.ops._div import Div_IFunctionFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids
        from marketsim.gen._out.math._exp import Exp_IFunctionFloat as _math_Exp
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatIFunctionFloat as _observable_OnEveryDt
        from marketsim.gen._out.ops._div import Div_IObservableFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IFunctionFloat as _observable_BreaksAtChanges
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position
        from marketsim.gen._out.event._after import After_IFunctionFloat as _event_After
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit
        from marketsim.gen._out.math._atan import Atan_IFunctionFloat as _math_Atan
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.strategy._generic import Generic_IOrderGeneratorIEvent as _strategy_Generic
        from marketsim.gen._out.order._floatingprice import FloatingPrice_IObservableFloatFloatIOrderGenerator as _order_FloatingPrice
        from marketsim.gen._out.order._iceberg import Iceberg_IFunctionFloatIOrderGenerator as _order_Iceberg
        return _strategy_Combine(_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_observable_OnEveryDt(0.9,_ops_Div(_orderbook_SafeSidePrice(_orderbook_Asks(),_constant((100+self.delta))),_math_Exp(_ops_Div(_math_Atan(_trader_Position()),_constant(1000)))))),_order__curried_price_Limit(_side_Sell(),_constant((self.volume*1000))))),_event_After(_constant(0.0))),_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_observable_OnEveryDt(0.9,_ops_Div(_orderbook_SafeSidePrice(_orderbook_Bids(),_constant((100-self.delta))),_math_Exp(_ops_Div(_math_Atan(_trader_Position()),_constant(1000)))))),_order__curried_price_Limit(_side_Buy(),_constant((self.volume*1000))))),_event_After(_constant(0.0))))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MarketMaker(delta = None,volume = None): 
    from marketsim import float
    from marketsim import rtti
    if delta is None or rtti.can_be_casted(delta, float):
        if volume is None or rtti.can_be_casted(volume, float):
            return MarketMaker_FloatFloat(delta,volume)
    raise Exception("Cannot find suitable overload")
