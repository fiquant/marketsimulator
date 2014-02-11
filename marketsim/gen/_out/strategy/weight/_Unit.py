def unit(): 
    from marketsim.gen._out.strategy.weight.trader._trader_unit import trader_Unit_ as _strategy_weight_trader_trader_Unit
    from marketsim import rtti
    return _strategy_weight_trader_trader_Unit()
    raise Exception('Cannot find suitable overload for unit('++')')
from marketsim import IAccount
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "Unit"])
class Unit_IAccount(Function[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy
        from marketsim import rtti
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Unit(%(trader)s)" % self.__dict__
    
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
        from marketsim.gen._out._constant import constant_Float as _constant
        return _constant(1.0)
    
def Unit(trader = None): 
    from marketsim import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return Unit_IAccount(trader)
    raise Exception('Cannot find suitable overload for Unit('+str(trader)+')')
