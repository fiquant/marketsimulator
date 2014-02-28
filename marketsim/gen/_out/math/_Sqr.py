from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Log/Pow", "Sqr"])
class Sqr_IObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_const_Float,1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat
    }
    def __repr__(self):
        return "{%(x)s}^2" % self.__dict__
    
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
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim import call
        return call(_ops_Mul_IObservableFloatIObservableFloat,self.x,self.x)
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context
@registry.expose(["Log/Pow", "Sqr"])
class Sqr_Float(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_constant_Float,1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat
    }
    def __repr__(self):
        return "{%(x)s}^2" % self.__dict__
    
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
        from marketsim.gen._out.ops._mul import Mul_FloatFloat as _ops_Mul_FloatFloat
        from marketsim import call
        return call(_ops_Mul_FloatFloat,self.x,self.x)
    
def Sqr(x = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        return Sqr_IObservableFloat(x)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        return Sqr_Float(x)
    raise Exception('Cannot find suitable overload for Sqr('+str(x) +':'+ str(type(x))+')')
