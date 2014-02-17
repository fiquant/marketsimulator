from marketsim import str
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "MarketData"])
class MarketData_StringStringStringFloatFloat(ISingleAssetStrategy):
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
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIFunctionFloat as _ops_Sub_IObservableFloatIFunctionFloat
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.event._after import After_IFunctionFloat as _event_After_IFunctionFloat
        from marketsim.gen._out.order._iceberg import Iceberg_IFunctionFloatIOrderGenerator as _order_Iceberg_IFunctionFloatIOrderGenerator
        from marketsim.gen._out.order._floatingprice import FloatingPrice_IObservableFloatFloatIOrderGenerator as _order_FloatingPrice_IObservableFloatFloatIOrderGenerator
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._add import Add_IObservableFloatIFunctionFloat as _ops_Add_IObservableFloatIFunctionFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_IFunctionSideIFunctionFloat as _order__curried_price_Limit_IFunctionSideIFunctionFloat
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.strategy._generic import Generic_IOrderGeneratorIEvent as _strategy_Generic_IOrderGeneratorIEvent
        return _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(_strategy_Generic_IOrderGeneratorIEvent(_order_Iceberg_IFunctionFloatIOrderGenerator(_constant_Float(self.volume),_order_FloatingPrice_IObservableFloatFloatIOrderGenerator(_observable_BreaksAtChanges_IObservableFloat(_ops_Add_IObservableFloatIFunctionFloat(_observable_Quote_StringStringString(self.ticker,self.start,self.end),_constant_Float(self.delta))),_order__curried_price_Limit_IFunctionSideIFunctionFloat(_side_Sell_(),_constant_Float((self.volume*1000))))),_event_After_IFunctionFloat(_constant_Float(0.0))),_strategy_Generic_IOrderGeneratorIEvent(_order_Iceberg_IFunctionFloatIOrderGenerator(_constant_Float(self.volume),_order_FloatingPrice_IObservableFloatFloatIOrderGenerator(_observable_BreaksAtChanges_IObservableFloat(_ops_Sub_IObservableFloatIFunctionFloat(_observable_Quote_StringStringString(self.ticker,self.start,self.end),_constant_Float(self.delta))),_order__curried_price_Limit_IFunctionSideIFunctionFloat(_side_Buy_(),_constant_Float((self.volume*1000))))),_event_After_IFunctionFloat(_constant_Float(0.0))))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MarketData(ticker = None,start = None,end = None,delta = None,volume = None): 
    from marketsim import str
    from marketsim import float
    from marketsim import rtti
    if ticker is None or rtti.can_be_casted(ticker, str):
        if start is None or rtti.can_be_casted(start, str):
            if end is None or rtti.can_be_casted(end, str):
                if delta is None or rtti.can_be_casted(delta, float):
                    if volume is None or rtti.can_be_casted(volume, float):
                        return MarketData_StringStringStringFloatFloat(ticker,start,end,delta,volume)
    raise Exception('Cannot find suitable overload for MarketData('+str(ticker)+','+str(start)+','+str(end)+','+str(delta)+','+str(volume)+')')
