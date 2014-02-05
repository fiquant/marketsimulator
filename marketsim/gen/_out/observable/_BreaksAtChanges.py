from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.breaks_at_changes import _BreaksAtChanges_Impl
from marketsim import IFunction
from marketsim import float
@registry.expose(["Basic", "BreaksAtChanges"])
class BreaksAtChanges_Optional__IFunction__Float__(Observable[float],_BreaksAtChanges_Impl):
    """   When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
    """ 
    def __init__(self, source = None):
        from marketsim import float
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
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
    
BreaksAtChanges = BreaksAtChanges_Optional__IFunction__Float__
