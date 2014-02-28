from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import context
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
        from marketsim import deref_opt
        from marketsim.gen._out.ops._add import Add_IObservableFloatFloat as _ops_Add_IObservableFloatFloat
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.order._floatingprice import FloatingPrice_FloatIObservableIOrderIObservableFloat as _order_FloatingPrice_FloatIObservableIOrderIObservableFloat
        from marketsim.gen._out.observable._quote import Quote_StringStringString as _observable_Quote_StringStringString
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges_IObservableFloat as _observable_BreaksAtChanges_IObservableFloat
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.event._after import After_Float as _event_After_Float
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.order._iceberg import Iceberg_IObservableIOrderFloat as _order_Iceberg_IObservableIOrderFloat
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(deref_opt(_side_Sell_()),deref_opt(_constant_Float((self.volume*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Add_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(self.ticker,self.start,self.end)),deref_opt(_constant_Float(self.delta)))))))),deref_opt(_constant_Float(self.volume)))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0)))))),deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(_order_Iceberg_IObservableIOrderFloat(deref_opt(_order_FloatingPrice_FloatIObservableIOrderIObservableFloat(deref_opt(_order__curried_price_Limit_SideFloat(deref_opt(_side_Buy_()),deref_opt(_constant_Float((self.volume*1000))))),deref_opt(_observable_BreaksAtChanges_IObservableFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_observable_Quote_StringStringString(self.ticker,self.start,self.end)),deref_opt(_constant_Float(self.delta)))))))),deref_opt(_constant_Float(self.volume)))),deref_opt(_event_After_Float(deref_opt(_constant_Float(0.0))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MarketData(ticker = None,start = None,end = None,delta = None,volume = None): 
    from marketsim import rtti
    if ticker is None or rtti.can_be_casted(ticker, str):
        if start is None or rtti.can_be_casted(start, str):
            if end is None or rtti.can_be_casted(end, str):
                if delta is None or rtti.can_be_casted(delta, float):
                    if volume is None or rtti.can_be_casted(volume, float):
                        return MarketData_StringStringStringFloatFloat(ticker,start,end,delta,volume)
    raise Exception('Cannot find suitable overload for MarketData('+str(ticker) +':'+ str(type(ticker))+','+str(start) +':'+ str(type(start))+','+str(end) +':'+ str(type(end))+','+str(delta) +':'+ str(type(delta))+','+str(volume) +':'+ str(type(volume))+')')
