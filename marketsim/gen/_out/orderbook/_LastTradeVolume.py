from marketsim import registry
from marketsim.gen._out._observable._observableint import Observableint
from marketsim.gen._intrinsic.orderbook.last_trade import LastTradeVolume_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "LastTradeVolume"])
class LastTradeVolume_IOrderQueue(Observableint,LastTradeVolume_Impl):
    """   Returns None if there haven't been any trades
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out._observable._observableint import Observableint
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        Observableint.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        
        rtti.check_fields(self)
        LastTradeVolume_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastTradeVolume(%(queue)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def LastTradeVolume(queue = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return LastTradeVolume_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for LastTradeVolume('+str(queue) +':'+ str(type(queue))+')')
