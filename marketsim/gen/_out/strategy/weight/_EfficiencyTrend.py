from marketsim import IAccount
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "EfficiencyTrend"])
class EfficiencyTrend_IAccountFloat(Function[float]):
    """ 
    """ 
    def __init__(self, trader = None, alpha = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import rtti
        self.trader = trader if trader is not None else _trader_SingleProxy()
        self.alpha = alpha if alpha is not None else 0.15
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount,
        'alpha' : float
    }
    def __repr__(self):
        return "EfficiencyTrend(%(trader)s, %(alpha)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._Derivative import Derivative as _math_Derivative
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.trader._Efficiency import Efficiency as _trader_Efficiency
        return _math_Derivative(_math_EW_Avg(_trader_Efficiency(self.trader),self.alpha))
    
def EfficiencyTrend(trader = None,alpha = None): 
    from marketsim import IAccount
    from marketsim import float
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return EfficiencyTrend_IAccountFloat(trader,alpha)
    raise Exception("Cannot find suitable overload")
