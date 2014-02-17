from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "price_Iceberg"])
class volume_price_Iceberg_IFunctionFloatFloatFloatIOrderGenerator(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_IFunctionSide as _order__curried_volume_price_Limit_IFunctionSide
        from marketsim import rtti
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit_IFunctionSide()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunction[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[float]]
    }
    def __repr__(self):
        return "price_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        volume = volume if volume is not None else _constant_Float(1.0)
        lotSize = self.lotSize
        proto = self.proto
        return price_Iceberg(lotSize, proto(volume))
    
def volume_price_Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return volume_price_Iceberg_IFunctionFloatFloatFloatIOrderGenerator(lotSize,proto)
    raise Exception('Cannot find suitable overload for volume_price_Iceberg('+str(lotSize)+','+str(proto)+')')
