from marketsim import registry
from marketsim import IFunction
from marketsim import float
@registry.expose(["Strategy", "f_AtanPow"])
class f_AtanPow_Float(IFunction[IFunction[float], IFunction[float]]):
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
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.strategy.weight._atanpow import AtanPow_IFunctionFloatFloat as _strategy_weight_AtanPow
        f = f if f is not None else _constant()
        base = self.base
        return _strategy_weight_AtanPow(f,base)
    
def f_AtanPow(base = None): 
    from marketsim import float
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, float):
        return f_AtanPow_Float(base)
    raise Exception("Cannot find suitable overload")
