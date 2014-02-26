from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
@registry.expose(["Order", "Peg"])
class Peg_FloatIObservableIOrder(Factory_Impl,IObservableIOrder):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim import rtti
        Factory_Impl.__init__(self)
        self.proto = proto if proto is not None else _order__curried_price_Limit_SideFloat()
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionfloat
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    
def Peg(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        return Peg_FloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto) +':'+ str(type(proto))+')')
