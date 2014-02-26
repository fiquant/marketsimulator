from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
@registry.expose(["Order", "price_Peg"])
class sidevolume_price_Peg_SideFloatFloatIObservableIOrder(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_price_limit import sidevolume_price_Limit_ as _order__curried_sidevolume_price_Limit_
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit_()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    }
    def __repr__(self):
        return "price_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        return price_Peg(proto(side,volume))
    
def sidevolume_price_Peg(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        return sidevolume_price_Peg_SideFloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for sidevolume_price_Peg('+str(proto) +':'+ str(type(proto))+')')
