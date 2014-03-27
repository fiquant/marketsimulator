from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim import registry
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
@registry.expose(["Order", "Iceberg"])
class Iceberg_IObservableIOrderFloat(ObservableIOrder,IObservableIOrder):
    """ 
      Iceberg order is initialized by an underlying order and a lot size.
      It sends consequently pieces of the underlying order of size equal or less to the lot size
      thus maximum lot size volume is visible at the market at any moment.
    """ 
    def __init__(self, proto = None, lotSize = None):
        from marketsim.gen._out.order._limit import Limit_SideFloatFloat as _order_Limit_SideFloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim.gen._out._iorder import IOrder
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        ObservableIOrder.__init__(self)
        self.proto = proto if proto is not None else deref_opt(_order_Limit_SideFloatFloat())
        event.subscribe(self.proto, self.fire, self)
        self.lotSize = lotSize if lotSize is not None else deref_opt(_constant_Float(10.0))
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservableIOrder,
        'lotSize' : IFunctionfloat
    }
    def __repr__(self):
        return "Iceberg(%(proto)s, %(lotSize)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.iceberg import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        lotSize = self.lotSize()
        if lotSize is None: return None
        
        return Order_Impl(proto, lotSize)
    
def Iceberg(proto = None,lotSize = None): 
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IObservableIOrder):
        if lotSize is None or rtti.can_be_casted(lotSize, IFunctionfloat):
            return Iceberg_IObservableIOrderFloat(proto,lotSize)
    raise Exception('Cannot find suitable overload for Iceberg('+str(proto) +':'+ str(type(proto))+','+str(lotSize) +':'+ str(type(lotSize))+')')
