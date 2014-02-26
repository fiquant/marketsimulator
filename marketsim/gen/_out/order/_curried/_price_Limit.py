from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Limit"])
class price_Limit_SideFloat(IFunctionIObservableIOrderIFunctionfloat):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell_()
        self.volume = volume if volume is not None else _constant_Float(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'volume' : IFunctionfloat
    }
    def __repr__(self):
        return "Limit(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._limit import Limit
        price = price if price is not None else _constant_Float(100.0)
        side = self.side
        volume = self.volume
        return Limit(side, price, volume)
    
def price_Limit(side = None,volume = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
            return price_Limit_SideFloat(side,volume)
    raise Exception('Cannot find suitable overload for price_Limit('+str(side) +':'+ str(type(side))+','+str(volume) +':'+ str(type(volume))+')')
