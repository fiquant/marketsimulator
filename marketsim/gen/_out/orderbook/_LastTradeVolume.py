from marketsim import registry
from marketsim.gen._intrinsic.orderbook.last_trade import _LastTradeVolume_Impl
from marketsim import IOrderQueue
@registry.expose(["Asset", "LastTradeVolume"])
class LastTradeVolume_Optional__IOrderQueue_(_LastTradeVolume_Impl):
    """   Returns None if there haven't been any trades
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
        _LastTradeVolume_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastTradeVolume(%(queue)s)" % self.__dict__
    
LastTradeVolume = LastTradeVolume_Optional__IOrderQueue_
