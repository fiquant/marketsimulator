from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "Iceberg"])
class sidevolume_Iceberg_FloatSideFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit_Float as _order__curried_sidevolume_Limit_Float
        from marketsim import rtti
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit_Float()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._iceberg import Iceberg
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(side,volume))
    
def sidevolume_Iceberg(lotSize = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
            return sidevolume_Iceberg_FloatSideFloatIObservableIOrder(lotSize,proto)
    raise Exception('Cannot find suitable overload for sidevolume_Iceberg('+str(lotSize) +':'+ str(type(lotSize))+','+str(proto) +':'+ str(type(proto))+')')
