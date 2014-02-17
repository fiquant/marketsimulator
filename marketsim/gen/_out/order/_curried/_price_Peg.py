from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class price_Peg_FloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[float]]):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit_IFunctionSideIFunctionFloat as _order__curried_price_Limit_IFunctionSideIFunctionFloat
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_price_Limit_IFunctionSideIFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._peg import Peg
        price = price if price is not None else _constant_Float(100.0)
        proto = self.proto
        return Peg(proto(price))
    
def price_Peg(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
        return price_Peg_FloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for price_Peg('+str(proto)+')')
