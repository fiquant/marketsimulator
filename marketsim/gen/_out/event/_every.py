from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._intrinsic.event import Every_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Event", "Every"])
class Every_Float(IEvent,Every_Impl):
    """ **Event that fires every *intervalFunc* moments of time**
    
    
    Parameters are:
    
    **intervalFunc**
    	 interval of time between two events 
    """ 
    def __init__(self, intervalFunc = None):
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.intervalFunc = intervalFunc if intervalFunc is not None else deref_opt(_math_random_expovariate_Float(1.0))
        rtti.check_fields(self)
        Every_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'intervalFunc' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Every(%(intervalFunc)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.intervalFunc.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Every(intervalFunc = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if intervalFunc is None or rtti.can_be_casted(intervalFunc, IFunctionfloat):
        return Every_Float(intervalFunc)
    raise Exception('Cannot find suitable overload for Every('+str(intervalFunc) +':'+ str(type(intervalFunc))+')')
