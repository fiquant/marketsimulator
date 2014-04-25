# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iaccount import IAccount
@registry.expose(["Trader", "EfficiencyTrend"])
class EfficiencyTrend_IAccountFloat(IFunctionfloat):
    """ **Returns first derivative of a moving average of the trader efficiency**
    
    
    Parameters are:
    
    **trader**
    
    **alpha**
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
        return "EfficiencyTrend(%(trader)s, %(alpha)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.trader.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.trader._efficiency import Efficiency_IAccount as _trader_Efficiency_IAccount
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.math._derivative import Derivative_IDifferentiable as _math_Derivative_IDifferentiable
        from marketsim import deref_opt
        return deref_opt(_math_Derivative_IDifferentiable(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_trader_Efficiency_IAccount(self.trader)),self.alpha))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def EfficiencyTrend(trader = None,alpha = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return EfficiencyTrend_IAccountFloat(trader,alpha)
    raise Exception('Cannot find suitable overload for EfficiencyTrend('+str(trader) +':'+ str(type(trader))+','+str(alpha) +':'+ str(type(alpha))+')')
