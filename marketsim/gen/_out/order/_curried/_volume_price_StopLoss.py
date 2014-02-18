from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "price_StopLoss"])
class volume_price_StopLoss_FloatFloatFloatIObservableIOrder(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit_Side
        from marketsim import rtti
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit_Side()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IFunctionfloat,
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    }
    def __repr__(self):
        return "price_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        volume = volume if volume is not None else _constant_Float(1.0)
        maxloss = self.maxloss
        proto = self.proto
        return price_StopLoss(maxloss, proto(volume))
    
def volume_price_StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
            return volume_price_StopLoss_FloatFloatFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for volume_price_StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
