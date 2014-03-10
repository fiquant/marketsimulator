from marketsim import registry
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
@registry.expose(["-", "Fv"])
class Fv_strategysideFundamentalValue(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_Float as _strategy_side_FundamentalValue_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_Float())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    def __repr__(self):
        return "Fv(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.fv
    
def Fv(x = None): 
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Fv_strategysideFundamentalValue(x)
    raise Exception('Cannot find suitable overload for Fv('+str(x) +':'+ str(type(x))+')')
