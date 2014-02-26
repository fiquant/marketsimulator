from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
@registry.expose(["Order", "ImmediateOrCancel"])
class volume_ImmediateOrCancel_FloatIObservableIOrder(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit_SideFloat as _order__curried_volume_Limit_SideFloat
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_Limit_SideFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionfloat
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        return ImmediateOrCancel(proto(volume))
    
def volume_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        return volume_ImmediateOrCancel_FloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for volume_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
