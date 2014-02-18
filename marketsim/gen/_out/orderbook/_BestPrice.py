from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.orderbook.props import _BestPrice_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "BestPrice"])
class BestPrice_IOrderQueue(Observable[float],_BestPrice_Impl):
    """   Returns None is *queue* is empty
    """ 
    def __init__(self, queue = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import rtti
        Observable[float].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks_IOrderBook()
        
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
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return BestPrice_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for BestPrice('+str(queue) +':'+ str(type(queue))+')')
