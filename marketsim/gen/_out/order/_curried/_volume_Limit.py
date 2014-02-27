from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Limit"])
class volume_Limit_SideFloat(IFunctionIObservableIOrder_from_IFunctionfloat):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, price = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell_()
        self.price = price if price is not None else _constant_Float(100.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'price' : IFunctionfloat
    }
    def __repr__(self):
        return "Limit(%(side)s, %(price)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._limit import Limit
        volume = volume if volume is not None else _constant_Float(1.0)
        side = self.side
        price = self.price
        return Limit(side, price, volume)
    
def volume_Limit(side = None,price = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if price is None or rtti.can_be_casted(price, IFunctionfloat):
            return volume_Limit_SideFloat(side,price)
    raise Exception('Cannot find suitable overload for volume_Limit('+str(side) +':'+ str(type(side))+','+str(price) +':'+ str(type(price))+')')
