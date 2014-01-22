from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim.gen._out.strategy._Combine import Combine as _strategy_Combine
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.order._Iceberg import Iceberg as _order_Iceberg
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.order._FloatingPrice import FloatingPrice as _order_FloatingPrice
from marketsim.gen._out.observable._BreaksAtChanges import BreaksAtChanges as _observable_BreaksAtChanges
from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
from marketsim.gen._out.orderbook._SafeSidePrice import SafeSidePrice as _orderbook_SafeSidePrice
from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.math._Exp import Exp as _math_Exp
from marketsim.gen._out.math._Atan import Atan as _math_Atan
from marketsim.gen._out.trader._Position import Position as _trader_Position
from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
from marketsim.gen._out.side._Sell import Sell as _side_Sell
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.event._After import After as _event_After
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.order._Iceberg import Iceberg as _order_Iceberg
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.order._FloatingPrice import FloatingPrice as _order_FloatingPrice
from marketsim.gen._out.observable._BreaksAtChanges import BreaksAtChanges as _observable_BreaksAtChanges
from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
from marketsim.gen._out.orderbook._SafeSidePrice import SafeSidePrice as _orderbook_SafeSidePrice
from marketsim.gen._out.orderbook._Bids import Bids as _orderbook_Bids
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.math._Exp import Exp as _math_Exp
from marketsim.gen._out.math._Atan import Atan as _math_Atan
from marketsim.gen._out.trader._Position import Position as _trader_Position
from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
from marketsim.gen._out.side._Buy import Buy as _side_Buy
from marketsim.gen._out._constant import constant as _constant
from marketsim.gen._out.event._After import After as _event_After
from marketsim.gen._out._constant import constant as _constant
from marketsim import context
@registry.expose(["Strategy", "MarketMaker"])
class MarketMaker(ISingleAssetStrategy):
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
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Combine(_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_observable_OnEveryDt(0.9,_orderbook_SafeSidePrice(_orderbook_Asks(),_constant(100+self.delta))/_math_Exp(_math_Atan(_trader_Position())/1000))),_order__curried_price_Limit(_side_Sell(),_constant(self.volume*1000)))),_event_After(_constant(0.0))),_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_observable_OnEveryDt(0.9,_orderbook_SafeSidePrice(_orderbook_Bids(),_constant(100-self.delta))/_math_Exp(_math_Atan(_trader_Position())/1000))),_order__curried_price_Limit(_side_Buy(),_constant(self.volume*1000)))),_event_After(_constant(0.0))))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
