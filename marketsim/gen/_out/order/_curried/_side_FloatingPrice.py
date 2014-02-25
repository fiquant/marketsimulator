from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Order", "FloatingPrice"])
class side_FloatingPrice_SideFloatIObservableIOrderIObservableFloat(IFunctionIObservableIOrderIFunctionSide):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_price_Limit_Float()
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,
        'floatingPrice' : IObservablefloat
    }
    def __repr__(self):
        return "FloatingPrice(%(proto)s, %(floatingPrice)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        floatingPrice = self.floatingPrice
        return FloatingPrice(proto(side), floatingPrice)
    
def side_FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return side_FloatingPrice_SideFloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for side_FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
