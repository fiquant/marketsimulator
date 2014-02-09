from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Market"])
class Market_SideIFunctionFloat(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]]):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Market" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._Market import Market
        side = side if side is not None else _side_Sell()
        volume = volume if volume is not None else _constant(1.0)
        
        return Market(side, volume)
    
def sidevolume_Market(): 
    from marketsim import rtti
    return Market_SideIFunctionFloat()
    raise Exception("Cannot find suitable overload")
