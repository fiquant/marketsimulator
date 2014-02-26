from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "RSI_linear"])
class RSI_linear_FloatIObservableIOrderFloatIObservableFloatFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, orderFactory = None, alpha = None, k = None, timeframe = None):
        from marketsim.gen._out.order._curried._signedvolume_marketsigned import signedVolume_MarketSigned_ as _order__curried_signedVolume_MarketSigned_
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_signedVolume_MarketSigned_()
        self.alpha = alpha if alpha is not None else (1.0/14)
        self.k = k if k is not None else _const_Float(-0.04)
        self.timeframe = timeframe if timeframe is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IFunctionIObservableIOrderIFunctionfloat,
        'alpha' : float,
        'k' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "RSI_linear(%(orderFactory)s, %(alpha)s, %(k)s, %(timeframe)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear_FloatIObservableFloatFloatISingleAssetTrader as _strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader
        return _strategy_Generic_IObservableIOrderIEvent(self.orderFactory(_strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader(self.alpha,self.k,self.timeframe)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def RSI_linear(orderFactory = None,alpha = None,k = None,timeframe = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionfloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            if k is None or rtti.can_be_casted(k, IObservablefloat):
                if timeframe is None or rtti.can_be_casted(timeframe, float):
                    return RSI_linear_FloatIObservableIOrderFloatIObservableFloatFloat(orderFactory,alpha,k,timeframe)
    raise Exception('Cannot find suitable overload for RSI_linear('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(alpha) +':'+ str(type(alpha))+','+str(k) +':'+ str(type(k))+','+str(timeframe) +':'+ str(type(timeframe))+')')
