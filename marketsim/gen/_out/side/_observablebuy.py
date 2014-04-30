# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._intrinsic.side import Buy_Impl
@registry.expose(["Side", "observableBuy"])
class observableBuy_(ObservableSide,Buy_Impl):
    """ **Observable always equal to Buy side**
    
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
        rtti.check_fields(self)
        Buy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "observableBuy" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def observableBuy(): 
    from marketsim import rtti
    return observableBuy_()
    raise Exception('Cannot find suitable overload for observableBuy('++')')
