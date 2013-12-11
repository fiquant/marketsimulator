from marketsim import registry
from marketsim.gen._intrinsic.orderbook.props import _BestPrice_Impl
from marketsim import IOrderQueue
@registry.expose(["Orderbook", "BestPrice"])
class BestPrice(_BestPrice_Impl):
    """ 
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        from marketsim import event
        from marketsim import types
        self.queue = queue if queue is not None else Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        _BestPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "Price(%(queue)s)" % self.__dict__
    
