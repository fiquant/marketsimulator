from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim.gen._intrinsic.observable.breaks_at_changes import _BreaksAtChanges_Impl
from marketsim import float
@registry.expose(["Basic", "BreaksAtChanges"])
class BreaksAtChanges_Optional__IFunction__Float__(Observable[float],_BreaksAtChanges_Impl):
    """   When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
    """ 
    def __init__(self, source = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _constant(1.0)
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        rtti.check_fields(self)
        _BreaksAtChanges_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[float]
    }
    def __repr__(self):
        return "BreaksAtChanges(%(source)s)" % self.__dict__
    
def BreaksAtChanges(source = None): 
    return BreaksAtChanges_Optional__IFunction__Float__(source)
