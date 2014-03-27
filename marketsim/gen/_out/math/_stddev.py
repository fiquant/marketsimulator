from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._cumulative import Cumulative
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_mathCumulative(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    
    
    def __repr__(self):
        return "StdDev(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.math._var import Var_mathCumulative as _math_Var_mathCumulative
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_mathCumulative(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._ew import EW
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_mathEW(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    
    
    def __repr__(self):
        return "StdDev(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.math._var import Var_mathEW as _math_Var_mathEW
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_mathEW(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._moving import Moving
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_mathMoving(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    
    
    def __repr__(self):
        return "StdDev(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.math._var import Var_mathMoving as _math_Var_mathMoving
        from marketsim import deref_opt
        return deref_opt(_math_Sqrt_Float(deref_opt(_math_Var_mathMoving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def StdDev(x = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out.math._ew import EW
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        return StdDev_mathCumulative(x)
    if x is None or rtti.can_be_casted(x, EW):
        return StdDev_mathEW(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return StdDev_mathMoving(x)
    raise Exception('Cannot find suitable overload for StdDev('+str(x) +':'+ str(type(x))+')')
