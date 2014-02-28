from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
@registry.expose(["Order", "price_ImmediateOrCancel"])
class side_price_ImmediateOrCancel_SideFloatIObservableIOrder(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim import call
        from marketsim import rtti
        self.proto = proto if proto is not None else call(_order__curried_side_price_Limit_Float,)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
    }
    def __repr__(self):
        return "price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import call
        from marketsim.gen._out.order._curried._price_immediateorcancel import price_ImmediateOrCancel
        side = side if side is not None else call(_side_Sell_,)
        proto = self.proto
        return price_ImmediateOrCancel(proto(side))
    
def side_price_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
        return side_price_ImmediateOrCancel_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for side_price_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
