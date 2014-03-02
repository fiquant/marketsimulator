from marketsim import registry
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
@registry.expose(["-", "Alpha"])
class Alpha_strategysideMeanReversion(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_FloatIOrderBook as _strategy_side_MeanReversion_FloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_FloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    def __repr__(self):
        return "Alpha(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.alpha
    
from marketsim import registry
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
@registry.expose(["-", "Alpha"])
class Alpha_strategysideTrendFollower(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    def __repr__(self):
        return "Alpha(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.alpha
    
def Alpha(x = None): 
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Alpha_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Alpha_strategysideTrendFollower(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
