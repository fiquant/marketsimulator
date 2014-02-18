from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Order", "price_FloatingPrice"])
class sidevolume_price_FloatingPrice_IObservableFloatSideFloatFloatIObservableIOrder(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim.gen._out.order._curried._sidevolume_price_limit import sidevolume_price_Limit_ as _order__curried_sidevolume_price_Limit_
        from marketsim import rtti
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit_()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservablefloat,
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    }
    def __repr__(self):
        return "price_FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        floatingPrice = self.floatingPrice
        proto = self.proto
        return price_FloatingPrice(floatingPrice, proto(side,volume))
    
def sidevolume_price_FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim import rtti
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
            return sidevolume_price_FloatingPrice_IObservableFloatSideFloatFloatIObservableIOrder(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for sidevolume_price_FloatingPrice('+str(floatingPrice) +':'+ str(type(floatingPrice))+','+str(proto) +':'+ str(type(proto))+')')
