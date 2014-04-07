from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.breaks_at_changes import BreaksAtChanges_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Basic", "BreaksAtChanges"])
class BreaksAtChanges_IObservableFloat(Observablefloat,BreaksAtChanges_Impl):
    """   When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        BreaksAtChanges_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    
    
    def on_source_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'source', value)
    
    def __repr__(self):
        return "BreaksAtChanges(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def BreaksAtChanges(source = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return BreaksAtChanges_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for BreaksAtChanges('+str(source) +':'+ str(type(source))+')')
