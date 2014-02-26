from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionside import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
@registry.expose(["Order", "Peg"])
class side_Peg_SideFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionSide):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_price_Limit_Float()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._peg import Peg
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        return Peg(proto(side))
    
def side_Peg(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionside import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        return side_Peg_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for side_Peg('+str(proto) +':'+ str(type(proto))+')')
