from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Peg"])
class Peg(Factory_Impl,IOrderGenerator):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
        from marketsim import Order
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else _order__curried_price_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    
