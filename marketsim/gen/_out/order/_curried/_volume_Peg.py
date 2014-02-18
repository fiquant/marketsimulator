from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
@registry.expose(["Order", "Peg"])
class volume_Peg_FloatFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionfloat):
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
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._peg import Peg
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        return Peg(proto(volume))
    
def volume_Peg(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
        return volume_Peg_FloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for volume_Peg('+str(proto) +':'+ str(type(proto))+')')
