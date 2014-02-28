from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_IObservableFloatFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'alpha' : float
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}(%(source)s)}" % self.__dict__
    
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
        from marketsim.gen._out.math._sqrt import Sqrt_Float as _math_Sqrt_Float
        from marketsim.gen._out.math.ew._var import Var_IObservableFloatFloat as _math_EW_Var_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_EW_Var_IObservableFloatFloat(self.source,self.alpha))))
    
def StdDev(source = None,alpha = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return StdDev_IObservableFloatFloat(source,alpha)
    raise Exception('Cannot find suitable overload for StdDev('+str(source) +':'+ str(type(source))+','+str(alpha) +':'+ str(type(alpha))+')')
