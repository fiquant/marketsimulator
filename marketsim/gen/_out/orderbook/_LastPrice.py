from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.orderbook.last_price import _LastPrice_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "LastPrice"])
class LastPrice_IOrderQueue(Observablefloat,_LastPrice_Impl):
    """   Returns None is *queue* has been always empty
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        
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
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return LastPrice_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for LastPrice('+str(queue) +':'+ str(type(queue))+')')
