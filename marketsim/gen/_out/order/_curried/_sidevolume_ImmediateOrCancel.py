from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "ImmediateOrCancel"])
class sidevolume_ImmediateOrCancel_SideFloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit_IFunctionFloat as _order__curried_sidevolume_Limit_IFunctionFloat
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit_IFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        return ImmediateOrCancel(proto(side,volume))
    
def sidevolume_ImmediateOrCancel(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]
    ,IFunction[float]]):
        return sidevolume_ImmediateOrCancel_SideFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for sidevolume_ImmediateOrCancel('+str(proto)+')')
