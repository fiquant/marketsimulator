# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.price._marketdata import MarketData
@registry.expose(["-", "Start"])
class Start_strategypriceMarketData(object):
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
        return "Start(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    @property
    def dereference(self):
        return self.x.start
    
def Start(x = None): 
    from marketsim.gen._out.strategy.price._marketdata import MarketData
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MarketData):
        return Start_strategypriceMarketData(x)
    raise Exception('Cannot find suitable overload for Start('+str(x) +':'+ str(type(x))+')')
