from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.on_every_dt import OnEveryDt_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Basic", "OnEveryDt"])
class OnEveryDt_FloatFloat(Observablefloat,OnEveryDt_Impl):
    """ **Discretizes function *x* at even time steps *dt***
    
    
    Parameters are:
    
    **x**
    	 function to discretize 
    
    **dt**
    	 time discretization step 
    """ 
    def __init__(self, x = None, dt = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        self.dt = dt if dt is not None else 1.0
        rtti.check_fields(self)
        OnEveryDt_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'dt' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "[%(x)s]_dt=%(dt)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def OnEveryDt(x = None,dt = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if dt is None or rtti.can_be_casted(dt, float):
            return OnEveryDt_FloatFloat(x,dt)
    raise Exception('Cannot find suitable overload for OnEveryDt('+str(x) +':'+ str(type(x))+','+str(dt) +':'+ str(type(dt))+')')
