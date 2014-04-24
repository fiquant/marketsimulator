# generated with class generator.python.curried$after_typing$Curried
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
@registry.expose(["Strategy", "trader_Score"])
class trader_Score_(IFunctionIFunctionfloat_from_IAccount):
    """ **Calculates how many times efficiency of trader went up and went down**
    
     Returns difference between them.
    
     TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "trader_Score" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._score import Score_IAccount as _strategy_weight_Score_IAccount
        trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        
        return _strategy_weight_Score_IAccount(trader)
    
def trader_Score(): 
    from marketsim import rtti
    return trader_Score_()
    raise Exception('Cannot find suitable overload for trader_Score('++')')
