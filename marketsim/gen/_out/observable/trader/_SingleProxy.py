from marketsim import registry
from marketsim.gen._intrinsic.trader.proxy import _Single_Impl
@registry.expose(["Trader's", "SingleProxy"])
class SingleProxy(_Single_Impl):
    """ 
    """ 
    def __init__(self):
        
        _Single_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
