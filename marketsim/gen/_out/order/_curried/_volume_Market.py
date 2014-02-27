from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
@registry.expose(["Order", "Market"])
class volume_Market_Side(IFunctionIObservableIOrder_from_IFunctionfloat):
    """ 
      Market order intructs buy or sell given volume immediately
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
        return "Market(%(side)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._market import Market
        volume = volume if volume is not None else _constant_Float(1.0)
        side = self.side
        return Market(side, volume)
    
def volume_Market(side = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        return volume_Market_Side(side)
    raise Exception('Cannot find suitable overload for volume_Market('+str(side) +':'+ str(type(side))+')')
