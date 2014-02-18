from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
@registry.expose(["Order", "ImmediateOrCancel"])
class side_ImmediateOrCancel_SideIObservableIOrder(IFunctionIObservableIOrderIFunctionSide):
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
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_Limit_FloatFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionSide
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        return ImmediateOrCancel(proto(side))
    
def side_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
        return side_ImmediateOrCancel_SideIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for side_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
