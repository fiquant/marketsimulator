from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_IObservableFloatFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
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
        from marketsim import deref_opt
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math.ew._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        from marketsim.gen._out.math.ew._stddev import StdDev_IObservableFloatFloat as _math_EW_StdDev_IObservableFloatFloat
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(self.source,deref_opt(_math_EW_Avg_IObservableFloatFloat(self.source,self.alpha)))),deref_opt(_math_EW_StdDev_IObservableFloatFloat(self.source,self.alpha))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def RelStdDev(source = None,alpha = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return RelStdDev_IObservableFloatFloat(source,alpha)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(source) +':'+ str(type(source))+','+str(alpha) +':'+ str(type(alpha))+')')
