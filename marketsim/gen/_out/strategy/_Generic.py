from marketsim import registry
from marketsim.gen._intrinsic.strategy.generic import _Generic_Impl
from marketsim import IOrderGenerator
from marketsim import IEvent
@registry.expose(["Strategy", "Generic"])
class Generic_IOrderGeneratorIEvent(_Generic_Impl):
    """   creates an order via *orderFactory* and sends the order to the market using its trader
    """ 
    def __init__(self, orderFactory = None, eventGen = None):
        from marketsim.gen._out.order._limit import Limit_IFunctionSideIFunctionFloatIFunctionFloat as _order_Limit_IFunctionSideIFunctionFloatIFunctionFloat
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim import rtti
        self.orderFactory = orderFactory if orderFactory is not None else _order_Limit_IFunctionSideIFunctionFloatIFunctionFloat()
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float()
        rtti.check_fields(self)
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
    
def Generic(orderFactory = None,eventGen = None): 
    from marketsim import IOrderGenerator
    from marketsim import IEvent
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IOrderGenerator):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            return Generic_IOrderGeneratorIEvent(orderFactory,eventGen)
    raise Exception('Cannot find suitable overload for Generic('+str(orderFactory)+','+str(eventGen)+')')
