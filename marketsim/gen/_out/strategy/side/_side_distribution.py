from marketsim import registry
from marketsim.gen._out.strategy.side._noise import Noise
@registry.expose(["-", "Side_distribution"])
class Side_distribution_strategysideNoise(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._noise import Noise_Float as _strategy_side_Noise_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Noise_Float())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Noise
    }
    
    
    def __repr__(self):
        return "Side_distribution(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.side_distribution
    
def Side_distribution(x = None): 
    from marketsim.gen._out.strategy.side._noise import Noise
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Noise):
        return Side_distribution_strategysideNoise(x)
    raise Exception('Cannot find suitable overload for Side_distribution('+str(x) +':'+ str(type(x))+')')
