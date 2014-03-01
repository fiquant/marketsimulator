from marketsim import registry
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "IStatDomain"])
class IStatDomain_IObservableFloat(object):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "IStatDomain(%(source)s)" % self.__dict__
    

    @property
    def Source(self):
        from marketsim.gen._out.math._source import Source
        return Source(self)
    
    pass
IStatDomain = IStatDomain_IObservableFloat
