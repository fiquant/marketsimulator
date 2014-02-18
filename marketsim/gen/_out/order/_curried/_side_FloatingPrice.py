from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
@registry.expose(["Order", "FloatingPrice"])
class side_FloatingPrice_IObservableFloatSideFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionSide):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim import rtti
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_side_price_Limit_Float()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservablefloat,
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    }
    def __repr__(self):
        return "FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        side = side if side is not None else _side_Sell_()
        floatingPrice = self.floatingPrice
        proto = self.proto
        return FloatingPrice(floatingPrice, proto(side))
    
def side_FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim import rtti
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
            return side_FloatingPrice_IObservableFloatSideFloatIObservableIOrder(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for side_FloatingPrice('+str(floatingPrice) +':'+ str(type(floatingPrice))+','+str(proto) +':'+ str(type(proto))+')')
