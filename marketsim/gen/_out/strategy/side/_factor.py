from marketsim import registry
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
@registry.expose(["-", "Factor"])
class Factor_strategysidePairTrading(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloat as _strategy_side_PairTrading_IOrderBookFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading
    }
    
    
    def __repr__(self):
        return "Factor(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    @property
    def dereference(self):
        return self.x.factor
    
def Factor(x = None): 
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Factor_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Factor('+str(x) +':'+ str(type(x))+')')
