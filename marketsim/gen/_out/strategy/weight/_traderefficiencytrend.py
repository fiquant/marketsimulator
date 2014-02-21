from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Strategy", "TraderEfficiencyTrend"])
class TraderEfficiencyTrend_IAccountFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, trader = None, alpha = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import rtti
        self.trader = trader if trader is not None else _trader_SingleProxy_()
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
        return "TraderEfficiencyTrend(%(trader)s, %(alpha)s)" % self.__dict__
    
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
        from marketsim.gen._out.trader._efficiencytrend import EfficiencyTrend_IAccountFloat as _trader_EfficiencyTrend_IAccountFloat
        return _trader_EfficiencyTrend_IAccountFloat(self.trader,self.alpha)
    
def TraderEfficiencyTrend(trader = None,alpha = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return TraderEfficiencyTrend_IAccountFloat(trader,alpha)
    raise Exception('Cannot find suitable overload for TraderEfficiencyTrend('+str(trader) +':'+ str(type(trader))+','+str(alpha) +':'+ str(type(alpha))+')')
