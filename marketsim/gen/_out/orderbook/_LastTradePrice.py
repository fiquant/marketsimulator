from marketsim.ops._all import Observable
from marketsim import IOrderQueue
from marketsim.gen._intrinsic.orderbook.last_trade import _LastTradePrice_Impl
from marketsim import registry
from marketsim import Price
@registry.expose(["Asset", "LastTradePrice"])
class LastTradePrice_IOrderQueue(Observable[Price],_LastTradePrice_Impl):
    """   Returns None if there haven't been any trades
    """ 
    def __init__(self, queue = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import event
        Observable[Price].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        rtti.check_fields(self)
        _LastTradePrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    def __repr__(self):
        return "LastTradePrice(%(queue)s)" % self.__dict__
    
def LastTradePrice(queue = None): 
    from marketsim import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return LastTradePrice_IOrderQueue(queue)
    raise Exception("Cannot find suitable overload")
