from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "price_Iceberg"])
class sidevolume_price_Iceberg_SideFloatFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, proto = None, lotSize = None):
        from marketsim.gen._out.order._curried._sidevolume_price_limit import sidevolume_price_Limit_ as _order__curried_sidevolume_price_Limit_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit_()
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,
        'lotSize' : IFunctionfloat
    }
    def __repr__(self):
        return "price_Iceberg(%(proto)s, %(lotSize)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        lotSize = self.lotSize
        return price_Iceberg(proto(side,volume), lotSize)
    
def sidevolume_price_Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return sidevolume_price_Iceberg_SideFloatFloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for sidevolume_price_Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
