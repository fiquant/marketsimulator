from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
@registry.expose(["Order", "price_Limit"])
class volume_price_Limit_Side(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionfloat):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell_()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide
    }
    def __repr__(self):
        return "price_Limit(%(side)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        volume = volume if volume is not None else _constant_Float(1.0)
        side = self.side
        return price_Limit(side, volume)
    
def volume_price_Limit(side = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        return volume_price_Limit_Side(side)
    raise Exception('Cannot find suitable overload for volume_price_Limit('+str(side) +':'+ str(type(side))+')')
