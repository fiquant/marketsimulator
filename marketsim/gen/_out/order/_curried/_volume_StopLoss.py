from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class volume_StopLoss_IFunctionFloatFloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[float]]):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit_IFunctionSideIFunctionFloat as _order__curried_volume_Limit_IFunctionSideIFunctionFloat
        from marketsim import rtti
        self.maxloss = maxloss if maxloss is not None else _constant_Float(0.1)
        self.proto = proto if proto is not None else _order__curried_volume_Limit_IFunctionSideIFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IFunction[float],
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
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
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return volume_StopLoss_IFunctionFloatFloatIOrderGenerator(maxloss,proto)
    raise Exception('Cannot find suitable overload for volume_StopLoss('+str(maxloss)+','+str(proto)+')')
