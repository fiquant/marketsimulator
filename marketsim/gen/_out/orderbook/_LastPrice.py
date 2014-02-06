from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.orderbook.last_price import _LastPrice_Impl
from marketsim import IOrderQueue
from marketsim import registry
from marketsim import Price
@registry.expose(["Asset", "LastPrice"])
class LastPrice_Optional__IOrderQueue_(Observable[Price],_LastPrice_Impl):
    """   Returns None is *queue* has been always empty
    """ 
    def __init__(self, queue = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import event
        Observable[Price].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        rtti.check_fields(self)
        _LastPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastPrice(%(queue)s)" % self.__dict__
    
def LastPrice(queue = None): 
    return LastPrice_Optional__IOrderQueue_(queue)
