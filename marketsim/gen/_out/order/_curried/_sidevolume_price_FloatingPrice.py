from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Order", "price_FloatingPrice"])
class sidevolume_price_FloatingPrice_SideFloatFloatIObservableIOrderIObservableFloat(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim.gen._out.order._curried._sidevolume_price_limit import sidevolume_price_Limit_ as _order__curried_sidevolume_price_Limit_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit_()
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat,
        'floatingPrice' : IObservablefloat
    }
    def __repr__(self):
        return "price_FloatingPrice(%(proto)s, %(floatingPrice)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        floatingPrice = self.floatingPrice
        return price_FloatingPrice(proto(side,volume), floatingPrice)
    
def sidevolume_price_FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return sidevolume_price_FloatingPrice_SideFloatFloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for sidevolume_price_FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
