from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Strategy", "f_IdentityF"])
class f_IdentityF(IFunction[IFunction[float], IFunction[float]]):
    """ 
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
        return "f_IdentityF" % self.__dict__
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.strategy.weight._IdentityF import IdentityF
        f = f if f is not None else _constant()
        
        return IdentityF(f)
    
