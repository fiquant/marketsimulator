from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_IObservableFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import call
        from marketsim import rtti
        self.source = source if source is not None else call(_const_Float,1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{cumul}(%(source)s)}" % self.__dict__
    
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
        from marketsim.gen._out.math.cumulative._var import Var_IObservableFloat as _math_Cumulative_Var_IObservableFloat
        from marketsim import call
        return call(_math_Sqrt_Float,call(_math_Cumulative_Var_IObservableFloat,self.source))
    
def StdDev(source = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return StdDev_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for StdDev('+str(source) +':'+ str(type(source))+')')
