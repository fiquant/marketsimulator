from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Trader", "EfficiencyTrend"])
class EfficiencyTrend_IAccountFloat(IFunctionfloat):
    """ 
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
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._avg import Avg_IEW as _math_impl_Avg_IEW
        from marketsim.gen._out.math.impl._ew import EW_IObservableFloatFloat as _math_impl_EW_IObservableFloatFloat
        from marketsim.gen._out.math._derivative import Derivative_IDifferentiable as _math_Derivative_IDifferentiable
        from marketsim.gen._out.trader._efficiency import Efficiency_IAccount as _trader_Efficiency_IAccount
        return deref_opt(_math_Derivative_IDifferentiable(deref_opt(_math_impl_Avg_IEW(deref_opt(_math_impl_EW_IObservableFloatFloat(deref_opt(_trader_Efficiency_IAccount(self.trader)),self.alpha))))))
    
def EfficiencyTrend(trader = None,alpha = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return EfficiencyTrend_IAccountFloat(trader,alpha)
    raise Exception('Cannot find suitable overload for EfficiencyTrend('+str(trader) +':'+ str(type(trader))+','+str(alpha) +':'+ str(type(alpha))+')')
