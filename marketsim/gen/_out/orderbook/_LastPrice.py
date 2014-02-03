from marketsim import registry
from marketsim.gen._intrinsic.orderbook.last_price import _LastPrice_Impl
from marketsim import IOrderQueue
@registry.expose(["Asset", "LastPrice"])
class LastPrice(_LastPrice_Impl):
    """   Returns None is *queue* has been always empty
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        self.queue = queue if queue is not None else _orderbook_Asks()
        rtti.check_fields(self)
        _LastPrice_Impl.__init__(self)
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastPrice(%(queue)s)" % self.__dict__
    
