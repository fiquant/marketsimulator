from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._intrinsic.event import After_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Event", "After"])
class After_Float(IEvent,After_Impl):
    """ **Event that once at *delay***
    
    
    Parameters are:
    
    **delay**
    	 when the event should be fired 
    """ 
    def __init__(self, delay = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.delay = delay if delay is not None else deref_opt(_constant_Float(10.0))
        rtti.check_fields(self)
        After_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'delay' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "After(%(delay)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.delay.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def After(delay = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if delay is None or rtti.can_be_casted(delay, IFunctionfloat):
        return After_Float(delay)
    raise Exception('Cannot find suitable overload for After('+str(delay) +':'+ str(type(delay))+')')
