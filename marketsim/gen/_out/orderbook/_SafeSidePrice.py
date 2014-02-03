from marketsim import registry
from marketsim import Price
from marketsim import Price
from marketsim.ops._all import Observable
from marketsim import IOrderQueue
from marketsim import IOrderQueue
from marketsim import IFunction
from marketsim import IFunction
from marketsim import context
@registry.expose(["Asset", "SafeSidePrice"])
class SafeSidePrice(Observable[Price]):
    """   and *defaultValue* if there haven't been any trades
    """ 
    def __init__(self, queue = None, defaultValue = None):
        from marketsim import Price
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
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
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Price import Price as _observable_Price
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._BestPrice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out.orderbook._BestPrice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._LastPrice import LastPrice as _orderbook_LastPrice
        from marketsim.gen._out.orderbook._LastPrice import LastPrice as _orderbook_LastPrice
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._LastPrice import LastPrice as _orderbook_LastPrice
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._BestPrice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._LastPrice import LastPrice as _orderbook_LastPrice
        from marketsim.gen._out.observable._Price import Price as _observable_Price
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._BestPrice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out._IfDefined import IfDefined as _IfDefined
        from marketsim.gen._out.orderbook._LastPrice import LastPrice as _orderbook_LastPrice
        return _observable_Price(_IfDefined(_orderbook_BestPrice(self.queue),_IfDefined(_orderbook_LastPrice(self.queue),self.defaultValue)
        )
        
        
        )
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
