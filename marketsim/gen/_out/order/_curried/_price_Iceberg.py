from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "Iceberg"])
class price_Iceberg_FloatFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim import rtti
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_price_Limit_SideFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionfloat
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._iceberg import Iceberg
        price = price if price is not None else _constant_Float(100.0)
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(price))
    
def price_Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
            return price_Iceberg_FloatFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for price_Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
