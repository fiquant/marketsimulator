from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IAccount
from marketsim.gen._out._constant import constant as _constant
from marketsim import context
@registry.expose(["Strategy", "Unit"])
class Unit(Function[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy as _observable_trader_SingleProxy
        self.trader = trader if trader is not None else _observable_trader_SingleProxy()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Unit(%(trader)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _constant(1.0)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
