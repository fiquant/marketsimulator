from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Market"])
class side_Market_Float(IFunctionIObservableIOrderIFunctionSide):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.volume = volume if volume is not None else _constant_Float(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'volume' : IFunctionfloat
    }
    def __repr__(self):
        return "Market(%(volume)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._market import Market
        side = side if side is not None else _side_Sell_()
        volume = self.volume
        return Market(side, volume)
    
def side_Market(volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
        return side_Market_Float(volume)
    raise Exception('Cannot find suitable overload for side_Market('+str(volume) +':'+ str(type(volume))+')')
