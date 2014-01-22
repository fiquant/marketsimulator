from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Strategy", "f_AtanPow"])
class f_AtanPow(IFunction[IFunction[float], IFunction[float]]):
    """ 
    """ 
    def __init__(self, base = None):
        from marketsim import rtti
        self.base = base if base is not None else 1.002
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'base' : float
    }
    def __repr__(self):
        return "f_AtanPow(%(base)s)" % self.__dict__
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.strategy.weight._AtanPow import AtanPow
        f = f if f is not None else _constant()
        base = self.base
        return AtanPow(f,base)
    
