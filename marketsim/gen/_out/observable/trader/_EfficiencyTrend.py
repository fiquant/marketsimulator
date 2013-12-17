from marketsim import registry
from marketsim.ops._function import Function
from marketsim import ISingleAssetTrader
from marketsim.gen._out._Derivative import Derivative
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.trader._Efficiency import Efficiency
from marketsim import context
@registry.expose(["Trader's", "EfficiencyTrend"])
class EfficiencyTrend(Function[float]):
    """ 
    """ 
    def __init__(self, trader = None, alpha = None):
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        self.trader = trader if trader is not None else SingleProxy()
        self.alpha = alpha if alpha is not None else 0.15
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : ISingleAssetTrader,
        'alpha' : float
    }
    def __repr__(self):
        return "EfficiencyTrend_{%(trader)s}" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        return Derivative(Avg(Efficiency(self.trader),self.alpha))
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
