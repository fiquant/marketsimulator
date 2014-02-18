from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim import context
@registry.expose(["Basic", "true"])
class true_(IFunctionbool):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "True" % self.__dict__
    
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
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        return _observableTrue_()
    
def true(): 
    from marketsim import rtti
    return true_()
    raise Exception('Cannot find suitable overload for true('++')')
