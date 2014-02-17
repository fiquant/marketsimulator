def efficiency(): 
    from marketsim.gen._out.strategy.weight.trader._trader_efficiency import trader_Efficiency_ as _strategy_weight_trader_trader_Efficiency_
    from marketsim import rtti
    return _strategy_weight_trader_trader_Efficiency_()
    raise Exception('Cannot find suitable overload for efficiency('++')')
from marketsim import IFunction
from marketsim import IAccount
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "Efficiency"])
class Efficiency_IAccount(IFunction[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import rtti
        self.trader = trader if trader is not None else _trader_SingleProxy_()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Efficiency(%(trader)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.trader._efficiency import Efficiency_IAccount as _trader_Efficiency_IAccount
        return _trader_Efficiency_IAccount(self.trader)
    
def Efficiency(trader = None): 
    from marketsim import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return Efficiency_IAccount(trader)
    raise Exception('Cannot find suitable overload for Efficiency('+str(trader)+')')
