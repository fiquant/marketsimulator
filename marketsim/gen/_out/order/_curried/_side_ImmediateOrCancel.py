from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
@registry.expose(["Order", "ImmediateOrCancel"])
class side_ImmediateOrCancel_SideIObservableIOrder(IFunctionIObservableIOrder_from_IFunctionSide):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_side_Limit_FloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        side = side if side is not None else deref_opt(_side_Sell_())
        proto = self.proto
        return ImmediateOrCancel(proto(side))
    
def side_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSide):
        return side_ImmediateOrCancel_SideIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for side_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
