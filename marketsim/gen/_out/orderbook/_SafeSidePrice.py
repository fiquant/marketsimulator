from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderQueue
from marketsim import registry
from marketsim import Price
from marketsim import context
from marketsim import float
@registry.expose(["Asset", "SafeSidePrice"])
class SafeSidePrice_IOrderQueueIFunctionFloat(Observable[Price]):
    """   and *defaultValue* if there haven't been any trades
    """ 
    def __init__(self, queue = None, defaultValue = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._asks import Asks as _orderbook_Asks
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        Observable[Price].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks()
        self.defaultValue = defaultValue if defaultValue is not None else _constant(100.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'defaultValue' : IFunction[float]
    }
    def __repr__(self):
        return "SafeSidePrice(%(queue)s, %(defaultValue)s)" % self.__dict__
    
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
        from marketsim.gen._out.observable._price import Price as _observable_Price
        from marketsim.gen._out._ifdefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._bestprice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out.orderbook._lastprice import LastPrice as _orderbook_LastPrice
        return _observable_Price(_IfDefined(_orderbook_BestPrice(self.queue),_IfDefined(_orderbook_LastPrice(self.queue),self.defaultValue)))
    
def SafeSidePrice(queue = None,defaultValue = None): 
    from marketsim import IOrderQueue
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if defaultValue is None or rtti.can_be_casted(defaultValue, IFunction[float]):
            return SafeSidePrice_IOrderQueueIFunctionFloat(queue,defaultValue)
    raise Exception("Cannot find suitable overload")
