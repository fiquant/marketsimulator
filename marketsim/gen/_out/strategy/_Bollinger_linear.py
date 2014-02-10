from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "Bollinger_linear"])
class Bollinger_linear_FloatIOrderGeneratorFloatIObservableFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, orderFactory = None, alpha = None, k = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._signedvolume_marketsigned import signedVolume_MarketSigned as _order__curried_signedVolume_MarketSigned
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_signedVolume_MarketSigned()
        self.alpha = alpha if alpha is not None else 0.15
        self.k = k if k is not None else _const(0.5)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IFunction[IOrderGenerator,IFunction[float]],
        'alpha' : float,
        'k' : IObservable[float]
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
        from marketsim.gen._out.strategy._generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear as _strategy_position_Bollinger_linear
        return _strategy_Generic(self.orderFactory(_strategy_position_Bollinger_linear(self.alpha,self.k)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def Bollinger_linear(orderFactory = None,alpha = None,k = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[float]]):
        if alpha is None or rtti.can_be_casted(alpha, float):
            if k is None or rtti.can_be_casted(k, IObservable[float]):
                return Bollinger_linear_FloatIOrderGeneratorFloatIObservableFloat(orderFactory,alpha,k)
    raise Exception("Cannot find suitable overload")
