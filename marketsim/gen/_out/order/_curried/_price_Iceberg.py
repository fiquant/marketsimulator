from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Iceberg"])
class price_Iceberg_FloatIObservableIOrderFloat(IFunctionIObservableIOrder_from_IFunctionfloat):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, proto = None, lotSize = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_price_Limit_SideFloat())
        self.lotSize = lotSize if lotSize is not None else deref_opt(_constant_Float(10.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionfloat,
        'lotSize' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "Iceberg(%(proto)s, %(lotSize)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.order._iceberg import Iceberg
        price = price if price is not None else deref_opt(_constant_Float(100.0))
        proto = self.proto
        lotSize = self.lotSize
        return Iceberg(proto(price), lotSize)
    
def price_Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionfloat):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return price_Iceberg_FloatIObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for price_Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
