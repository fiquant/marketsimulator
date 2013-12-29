from marketsim import registry
from marketsim.gen._intrinsic.orderbook.props import _BestPrice_Impl
from marketsim import IOrderQueue
@registry.expose(["Asset's", "BestPrice"])
class BestPrice(_BestPrice_Impl):
    """ 
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        from marketsim import event
        from marketsim import types
        self.queue = queue if queue is not None else Asks()
        _BestPrice_Impl.__init__(self)
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "BestPrice(%(queue)s)" % self.__dict__
    
