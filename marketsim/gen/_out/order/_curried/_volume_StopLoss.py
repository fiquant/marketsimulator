from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "StopLoss"])
class volume_StopLoss_FloatFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit_SideFloat as _order__curried_volume_Limit_SideFloat
        from marketsim import rtti
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        self.proto = proto if proto is not None else _order__curried_volume_Limit_SideFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionfloat
    }
    def __repr__(self):
        return "StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._stoploss import StopLoss
        volume = volume if volume is not None else _constant_Float(1.0)
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(volume))
    
def volume_StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
            return volume_StopLoss_FloatFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for volume_StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
