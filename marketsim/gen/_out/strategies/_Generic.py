from marketsim import registry
from marketsim.gen._intrinsic.strategy.generic import _Generic_Impl
from marketsim import IOrderGenerator
from marketsim import IEvent
@registry.expose(["Strategy", "Generic"])
class Generic(_Generic_Impl):
    """   creates an order via *orderFactory* and sends the order to the market using its trader
    """ 
    def __init__(self, orderFactory = None, eventGen = None):
        from marketsim.gen._out.order._Limit import Limit as _order_Limit
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        self.orderFactory = orderFactory if orderFactory is not None else _order_Limit()
        self.eventGen = eventGen if eventGen is not None else _observable_OnEveryDt()
        _Generic_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IOrderGenerator,
        'eventGen' : IEvent
    }
    def __repr__(self):
        return "Generic(%(orderFactory)s, %(eventGen)s)" % self.__dict__
    
