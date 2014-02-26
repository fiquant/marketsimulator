from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_Iceberg"])
class volume_price_Iceberg_FloatFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, proto = None, lotSize = None):
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit_Side
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit_Side()
        self.lotSize = lotSize if lotSize is not None else _constant_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,
        'lotSize' : IFunctionfloat
    }
    def __repr__(self):
        return "price_Iceberg(%(proto)s, %(lotSize)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        lotSize = self.lotSize
        return price_Iceberg(proto(volume), lotSize)
    
def volume_price_Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return volume_price_Iceberg_FloatFloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for volume_price_Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
