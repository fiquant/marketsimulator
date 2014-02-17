from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
@registry.expose(["Log/Pow", "Sqrt"])
class Sqrt_IFunctionFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "\\sqrt{%(x)s}" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import math
        x = self.x()
        if x is None: return None
        return math.sqrt(x)
    
def Sqrt(x = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        return Sqrt_IFunctionFloat(x)
    raise Exception('Cannot find suitable overload for Sqrt('+str(x)+')')
