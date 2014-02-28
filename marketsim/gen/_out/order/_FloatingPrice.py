from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
@registry.expose(["Order", "FloatingPrice"])
class FloatingPrice_FloatIObservableIOrderIObservableFloat(Factory_Impl,IObservableIOrder):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim import rtti
        from marketsim import call
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
        from marketsim import event
        Factory_Impl.__init__(self)
        self.proto = proto if proto is not None else call(_order__curried_price_Limit_SideFloat,)
        
        self.floatingPrice = floatingPrice if floatingPrice is not None else call(_const_Float,10.0)
        event.subscribe(self.floatingPrice, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionfloat,
        'floatingPrice' : IObservablefloat
    }
    def __repr__(self):
        return "FloatingPrice(%(proto)s, %(floatingPrice)s)" % self.__dict__
    
    
def FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return FloatingPrice_FloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
