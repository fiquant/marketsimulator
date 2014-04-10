from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Order", "FloatingPrice"])
class price_FloatingPrice_FloatIObservableIOrderIObservableFloat(IFunctionIObservableIOrder_from_IFunctionfloat):
    """ **Factory creating orders with floating price**
    
    
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    
    Parameters are:
    
    **proto**
    	 underlying orders to create 
    
    **floatingPrice**
    	 observable defining price of orders to create 
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim import deref_opt
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_price_Limit_SideFloat())
        self.floatingPrice = floatingPrice if floatingPrice is not None else deref_opt(_const_Float(10.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionfloat,
        'floatingPrice' : IObservablefloat
    }
    
    
    
    
    def __repr__(self):
        return "FloatingPrice(%(proto)s, %(floatingPrice)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        price = price if price is not None else deref_opt(_constant_Float(100.0))
        proto = self.proto
        floatingPrice = self.floatingPrice
        return FloatingPrice(proto(price), floatingPrice)
    
def price_FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return price_FloatingPrice_FloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for price_FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
