from marketsim import registry
from marketsim.gen._intrinsic.orderbook.props import _BestPrice_Impl
from marketsim import IOrderQueue
@registry.expose(["Asset", "BestPrice"])
class BestPrice_Optional__IOrderQueue_(_BestPrice_Impl):
    """   Returns None is *queue* is empty
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        self.queue = queue if queue is not None else _orderbook_Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        rtti.check_fields(self)
        _BestPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "BestPrice(%(queue)s)" % self.__dict__
    
BestPrice = BestPrice_Optional__IOrderQueue_
