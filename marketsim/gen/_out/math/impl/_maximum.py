from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._imoving import IMoving
from marketsim import context
@registry.expose(["Statistics", "Maximum"])
class Maximum_IMoving(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._moving import Moving_IObservableFloatFloat as _math_impl_Moving_IObservableFloatFloat
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IMoving
    }
    def __repr__(self):
        return "Maximum(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.moving._max import Max_IObservableFloatFloat as _math_Moving_Max_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._timeframe import Timeframe_IMoving as _math_impl_Timeframe_IMoving
        return deref_opt(_math_Moving_Max_IObservableFloatFloat(deref_opt(_math_impl_Source_IStatDomain(self.x)),deref_opt(_math_impl_Timeframe_IMoving(self.x))))
    
def Maximum(x = None): 
    from marketsim.gen._out._imoving import IMoving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IMoving):
        return Maximum_IMoving(x)
    raise Exception('Cannot find suitable overload for Maximum('+str(x) +':'+ str(type(x))+')')
