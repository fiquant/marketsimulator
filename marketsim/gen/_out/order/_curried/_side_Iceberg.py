from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Iceberg"])
class side_Iceberg_IFunctionFloatSideIOrderGenerator(IFunction[IOrderGenerator,IFunction[Side]]):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._side_limit import side_Limit_IFunctionFloatIFunctionFloat as _order__curried_side_Limit_IFunctionFloatIFunctionFloat
        from marketsim import rtti
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_side_Limit_IFunctionFloatIFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunction[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side]]
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._iceberg import Iceberg
        side = side if side is not None else _side_Sell_()
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(side))
    
def side_Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
            return side_Iceberg_IFunctionFloatSideIOrderGenerator(lotSize,proto)
    raise Exception('Cannot find suitable overload for side_Iceberg('+str(lotSize)+','+str(proto)+')')
