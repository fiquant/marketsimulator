from marketsim import registry
from marketsim.gen._out.strategy.price._marketdata import MarketData
@registry.expose(["-", "End"])
class End_strategypriceMarketData(object):
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
        return "End(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.end
    
def End(x = None): 
    from marketsim.gen._out.strategy.price._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketData):
        return End_strategypriceMarketData(x)
    raise Exception('Cannot find suitable overload for End('+str(x) +':'+ str(type(x))+')')
