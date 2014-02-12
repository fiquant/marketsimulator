from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "price_Peg"])
class volume_price_Peg_FloatFloatIOrderGenerator(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit_Side
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit_Side()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[float]]
    }
    def __repr__(self):
        return "price_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        return price_Peg(proto(volume))
    
def volume_price_Peg(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
        return volume_price_Peg_FloatFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for volume_price_Peg('+str(proto)+')')
