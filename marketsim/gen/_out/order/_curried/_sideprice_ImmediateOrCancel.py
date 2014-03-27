from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
@registry.expose(["Order", "ImmediateOrCancel"])
class sideprice_ImmediateOrCancel_SideFloatIObservableIOrder(IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        side = side if side is not None else deref_opt(_side_Sell_())
        price = price if price is not None else deref_opt(_constant_Float(100.0))
        proto = self.proto
        return ImmediateOrCancel(proto(side,price))
    
def sideprice_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
        return sideprice_ImmediateOrCancel_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for sideprice_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
