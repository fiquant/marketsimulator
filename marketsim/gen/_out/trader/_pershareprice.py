# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Trader", "PerSharePrice"])
class PerSharePrice_IAccount(Observablefloat):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    
    
    def __repr__(self):
        return "PerSharePrice(%(trader)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.trader.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self.impl.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
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
        from marketsim.gen._out.ops._div import Div_IObservableFloatIObservableFloat as _ops_Div_IObservableFloatIObservableFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim.gen._out.trader._balance import Balance_IAccount as _trader_Balance_IAccount
        from marketsim.gen._out.ops._sub import Sub_FloatIObservableFloat as _ops_Sub_FloatIObservableFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Sub_FloatIObservableFloat(deref_opt(_constant_Int(0)),deref_opt(_ops_Div_IObservableFloatIObservableFloat(deref_opt(_trader_Balance_IAccount(self.trader)),deref_opt(_trader_Position_IAccount(self.trader))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def PerSharePrice(trader = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return PerSharePrice_IAccount(trader)
    raise Exception('Cannot find suitable overload for PerSharePrice('+str(trader) +':'+ str(type(trader))+')')
