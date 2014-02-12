from marketsim.ops._all import Observable
from marketsim import IOrderQueue
from marketsim import registry
from marketsim.gen._intrinsic.orderbook.props import _BestPrice_Impl
from marketsim import Price
@registry.expose(["Asset", "BestPrice"])
class BestPrice_IOrderQueue(Observable[Price],_BestPrice_Impl):
    """   Returns None is *queue* is empty
    """ 
    def __init__(self, queue = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        Observable[Price].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks_IOrderBook()
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
    
def BestPrice(queue = None): 
    from marketsim import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return BestPrice_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for BestPrice('+str(queue)+')')
