from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._moving import Moving
from marketsim import context
@registry.expose(["Basic", "Minimum"])
class Minimum_Moving(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Minimum(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.moving._min import Min_IObservableFloatFloat as _math_Moving_Min_IObservableFloatFloat
        from marketsim.gen._out._source import Source_Moving as _Source_Moving
        from marketsim import deref_opt
        from marketsim.gen._out._timeframe import Timeframe_Moving as _Timeframe_Moving
        return deref_opt(_math_Moving_Min_IObservableFloatFloat(deref_opt(_Source_Moving(self.x)),deref_opt(_Timeframe_Moving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Minimum(x = None): 
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Minimum_Moving(x)
    raise Exception('Cannot find suitable overload for Minimum('+str(x) +':'+ str(type(x))+')')
