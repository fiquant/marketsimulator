from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IAccount
from marketsim.gen._out.trader._Efficiency import Efficiency as _trader_Efficiency
from marketsim import context
@registry.expose(["Strategy", "Efficiency"])
class Efficiency(Function[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        self.trader = trader if trader is not None else _trader_SingleProxy()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Efficiency(%(trader)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _trader_Efficiency(self.trader)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
