from marketsim import registry
from marketsim import Side
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.side import _Sell_Impl
@registry.expose(["Side", "Sell"])
class Sell_(Function[Side],_Sell_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _Sell_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Sell" % self.__dict__
    
def Sell(): 
    return Sell_()
