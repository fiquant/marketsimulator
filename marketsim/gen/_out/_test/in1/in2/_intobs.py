from marketsim import registry
from marketsim.gen._out._observable._observableint import Observableint
from marketsim import context
@registry.expose(["internal tests", "IntObs"])
class IntObs_(Observableint):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._observable._observableint import Observableint
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observableint.__init__(self)
        
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "IntObs" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out._const import const_Int as _const_Int
        from marketsim import deref_opt
        return deref_opt(_const_Int(0))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def IntObs(): 
    from marketsim import rtti
    return IntObs_()
    raise Exception('Cannot find suitable overload for IntObs('++')')
