from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_IObservableFloatFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _const(1.0)
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'alpha' : float
    }
    def __repr__(self):
        return "RSD_{\\alpha=%(alpha)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._div import Div_IObservableFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIFunctionFloat as _ops_Sub
        from marketsim.gen._out.math.EW._avg import Avg_IObservableFloatFloat as _math_EW_Avg
        from marketsim.gen._out.math.EW._stddev import StdDev_IObservableFloatFloat as _math_EW_StdDev
        return _ops_Div(_ops_Sub(self.source,_math_EW_Avg(self.source,self.alpha)),_math_EW_StdDev(self.source,self.alpha))
    
def RelStdDev(source = None,alpha = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return RelStdDev_IObservableFloatFloat(source,alpha)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(source)+','+str(alpha)+')')
