from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_Limit"])
class side_price_Limit_Float(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.volume = volume if volume is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'volume' : IFunctionfloat
    }
    def __repr__(self):
        return "price_Limit(%(volume)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        side = side if side is not None else deref_opt(_side_Sell_())
        volume = self.volume
        return price_Limit(side, volume)
    
def side_price_Limit(volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
        return side_price_Limit_Float(volume)
    raise Exception('Cannot find suitable overload for side_price_Limit('+str(volume) +':'+ str(type(volume))+')')
