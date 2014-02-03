from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import str
from marketsim import str
from marketsim import str
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Strategy", "MarketData"])
class MarketData(ISingleAssetStrategy):
    """   by creating large volume orders for the given price.
    
      Every time step of 1 in the simulation corresponds to a 1 day in the market data.
    
      At each time step the previous Limit Buy/Sell orders are cancelled and new ones
      are created based on the next price of the market data.
    """ 
    def __init__(self, ticker = None, start = None, end = None, delta = None, volume = None):
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.ticker = ticker if ticker is not None else "^GSPC"
        self.start = start if start is not None else "2001-1-1"
        self.end = end if end is not None else "2010-1-1"
        self.delta = delta if delta is not None else 1.0
        self.volume = volume if volume is not None else 1000.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'ticker' : str,
        'start' : str,
        'end' : str,
        'delta' : float,
        'volume' : float
    }
    def __repr__(self):
        return "MarketData(%(ticker)s, %(start)s, %(end)s, %(delta)s, %(volume)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.strategy._Combine import Combine as _strategy_Combine
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.order._Iceberg import Iceberg as _order_Iceberg
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._FloatingPrice import FloatingPrice as _order_FloatingPrice
        from marketsim.gen._out.observable._BreaksAtChanges import BreaksAtChanges as _observable_BreaksAtChanges
        from marketsim.gen._out.ops._Add import Add as _ops_Add
        from marketsim.gen._out.observable._Quote import Quote as _observable_Quote
        from marketsim.gen._out._const import const as _const
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
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.observable._Quote import Quote as _observable_Quote
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
        from marketsim.gen._out.side._Buy import Buy as _side_Buy
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.event._After import After as _event_After
        from marketsim.gen._out._constant import constant as _constant
        return _strategy_Combine(_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_ops_Add(_observable_Quote(self.ticker,self.start,self.end),_const(self.delta))),_order__curried_price_Limit(_side_Sell(),_constant((self.volume*1000))))),_event_After(_constant(0.0))),_strategy_Generic(_order_Iceberg(_constant(self.volume),_order_FloatingPrice(_observable_BreaksAtChanges(_ops_Sub(_observable_Quote(self.ticker,self.start,self.end),_const(self.delta))),_order__curried_price_Limit(_side_Buy(),_constant((self.volume*1000))))),_event_After(_constant(0.0))))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
