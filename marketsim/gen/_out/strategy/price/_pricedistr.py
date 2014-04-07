from marketsim import registry
from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
@registry.expose(["-", "PriceDistr"])
class PriceDistr_strategypriceLiquidityProvider(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider_FloatFloatIOrderBook as _strategy_price_LiquidityProvider_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_price_LiquidityProvider_FloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : LiquidityProvider
    }
    
    
    def __repr__(self):
        return "PriceDistr(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.priceDistr
    
def PriceDistr(x = None): 
    from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, LiquidityProvider):
        return PriceDistr_strategypriceLiquidityProvider(x)
    raise Exception('Cannot find suitable overload for PriceDistr('+str(x) +':'+ str(type(x))+')')
