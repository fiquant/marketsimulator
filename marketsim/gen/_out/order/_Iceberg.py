from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Iceberg"])
class Iceberg_IFunctionFloatIOrderGenerator(Observable[Order],IOrderGenerator):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.order._Limit import Limit as _order_Limit
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import Order
        Observable[Order].__init__(self)
        self.lotSize = lotSize if lotSize is not None else _constant(10.0)
        if isinstance(lotSize, types.IEvent):
            event.subscribe(self.lotSize, self.fire, self)
        self.proto = proto if proto is not None else _order_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunction[float],
        'proto' : IOrderGenerator
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.iceberg import Order_Impl
        lotSize = self.lotSize()
        if lotSize is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(lotSize, proto)
    
def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IOrderGenerator):
            return Iceberg_IFunctionFloatIOrderGenerator(lotSize,proto)
    raise Exception("Cannot find suitable overload")
