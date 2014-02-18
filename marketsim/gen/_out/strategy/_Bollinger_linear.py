from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "Bollinger_linear"])
class Bollinger_linear_FloatIObservableIOrderFloatIObservableFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, orderFactory = None, alpha = None, k = None):
        from marketsim.gen._out.order._curried._signedvolume_marketsigned import signedVolume_MarketSigned_ as _order__curried_signedVolume_MarketSigned_
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_signedVolume_MarketSigned_()
        self.alpha = alpha if alpha is not None else 0.15
        self.k = k if k is not None else _const_Float(0.5)
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
        'k' : IObservablefloat
    }
    def __repr__(self):
        return "Bollinger_linear(%(orderFactory)s, %(alpha)s, %(k)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear_FloatIObservableFloatISingleAssetTrader as _strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader
        return _strategy_Generic_IObservableIOrderIEvent(self.orderFactory(_strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader(self.alpha,self.k)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def Bollinger_linear(orderFactory = None,alpha = None,k = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionfloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            if k is None or rtti.can_be_casted(k, IObservablefloat):
                return Bollinger_linear_FloatIObservableIOrderFloatIObservableFloat(orderFactory,alpha,k)
    raise Exception('Cannot find suitable overload for Bollinger_linear('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(alpha) +':'+ str(type(alpha))+','+str(k) +':'+ str(type(k))+')')
