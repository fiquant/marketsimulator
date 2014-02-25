from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Order", "FloatingPrice"])
class price_FloatingPrice_FloatIObservableIOrderIObservableFloat(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_price_Limit_SideFloat()
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionfloat,
        'floatingPrice' : IObservablefloat
    }
    def __repr__(self):
        return "FloatingPrice(%(proto)s, %(floatingPrice)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        price = price if price is not None else _constant_Float(100.0)
        proto = self.proto
        floatingPrice = self.floatingPrice
        return FloatingPrice(proto(price), floatingPrice)
    
def price_FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return price_FloatingPrice_FloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for price_FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
