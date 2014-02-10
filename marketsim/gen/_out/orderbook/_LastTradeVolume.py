from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.orderbook.last_trade import _LastTradeVolume_Impl
from marketsim import IOrderQueue
from marketsim import Volume
from marketsim import registry
@registry.expose(["Asset", "LastTradeVolume"])
class LastTradeVolume_IOrderQueue(Observable[Volume],_LastTradeVolume_Impl):
    """   Returns None if there haven't been any trades
    """ 
    def __init__(self, queue = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks
        from marketsim import Volume
        from marketsim import event
        Observable[Volume].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        rtti.check_fields(self)
        _LastTradeVolume_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastTradeVolume(%(queue)s)" % self.__dict__
    
def LastTradeVolume(queue = None): 
    from marketsim import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return LastTradeVolume_IOrderQueue(queue)
    raise Exception("Cannot find suitable overload")
