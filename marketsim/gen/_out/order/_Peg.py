from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Peg"])
class Peg_FloatIOrderGenerator(Factory_Impl,IOrderGenerator):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit_SideIFunctionFloat
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else _order__curried_price_Limit_SideIFunctionFloat()
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    
def Peg(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
        return Peg_FloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
