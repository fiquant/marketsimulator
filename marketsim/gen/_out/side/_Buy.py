from marketsim import registry
from marketsim import Side
from marketsim import IFunction
from marketsim import context
@registry.expose(["Side", "Buy"])
class Buy_(IFunction[Side]):
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
        return "Buy" % self.__dict__
    
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
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        return _side_observableBuy_()
    
def Buy(): 
    from marketsim import rtti
    return Buy_()
    raise Exception('Cannot find suitable overload for Buy('++')')
