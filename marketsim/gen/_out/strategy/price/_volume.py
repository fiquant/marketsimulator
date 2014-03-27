from marketsim import registry
from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
@registry.expose(["-", "Volume"])
class Volume_strategypriceMarketMaker(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.price._marketmaker import MarketMaker_FloatFloat as _strategy_price_MarketMaker_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_price_MarketMaker_FloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketMaker
    }
    
    
    def __repr__(self):
        return "Volume(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    @property
    def dereference(self):
        return self.x.volume
    
from marketsim import registry
from marketsim.gen._out.strategy.price._marketdata import MarketData
@registry.expose(["-", "Volume"])
class Volume_strategypriceMarketData(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.price._marketdata import MarketData_StringStringStringFloatFloat as _strategy_price_MarketData_StringStringStringFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_price_MarketData_StringStringStringFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MarketData
    }
    
    
    def __repr__(self):
        return "Volume(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    @property
    def dereference(self):
        return self.x.volume
    
def Volume(x = None): 
    from marketsim.gen._out.strategy.price._marketmaker import MarketMaker
    from marketsim.gen._out.strategy.price._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketMaker):
        return Volume_strategypriceMarketMaker(x)
    if x is None or rtti.can_be_casted(x, MarketData):
        return Volume_strategypriceMarketData(x)
    raise Exception('Cannot find suitable overload for Volume('+str(x) +':'+ str(type(x))+')')
