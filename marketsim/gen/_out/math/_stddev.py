from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ew import EW
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_EW(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._var import Var_EW as _math_Var_EW
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_EW(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._cumulative import Cumulative
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_Cumulative(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._var import Var_Cumulative as _math_Var_Cumulative
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_Cumulative(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._moving import Moving
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_Moving(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._var import Var_Moving as _math_Var_Moving
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_Moving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def StdDev(x = None): 
    from marketsim.gen._out._ew import EW
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return StdDev_EW(x)
    if x is None or rtti.can_be_casted(x, Cumulative):
        return StdDev_Cumulative(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return StdDev_Moving(x)
    raise Exception('Cannot find suitable overload for StdDev('+str(x) +':'+ str(type(x))+')')
