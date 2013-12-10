from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.trader.proxy import _Single_Impl
@registry.expose(["Proxies", "SingleProxy"])
class SingleProxy(Function[float], _Single_Impl):
    """ 
    """ 
    def __init__(self):
        
        _Single_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "$(Trader)" % self.__dict__
    
