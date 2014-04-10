from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Strategy", "TraderEfficiencyTrend"])
class TraderEfficiencyTrend_IAccountFloat(IFunctionfloat):
    """ **Returns first derivative of a moving average of the trader efficiency**
    
    
    Parameters are:
    
    **trader**
    	 account in question 
    
    **alpha**
    	 parameter alpha for the moving average 
    """ 
    def __init__(self, trader = None, alpha = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim import rtti
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
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
        return "TraderEfficiencyTrend(%(trader)s, %(alpha)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.trader.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim import deref_opt
        return deref_opt(_trader_EfficiencyTrend_IAccountFloat(self.trader,self.alpha))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def TraderEfficiencyTrend(trader = None,alpha = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return TraderEfficiencyTrend_IAccountFloat(trader,alpha)
    raise Exception('Cannot find suitable overload for TraderEfficiencyTrend('+str(trader) +':'+ str(type(trader))+','+str(alpha) +':'+ str(type(alpha))+')')
