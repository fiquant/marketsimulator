from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.breaks_at_changes import _BreaksAtChanges_Impl
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Basic", "BreaksAtChanges"])
class BreaksAtChanges_IObservableFloat(Observable[float],_BreaksAtChanges_Impl):
    """   When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
    """ 
    def __init__(self, source = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import rtti
        Observable[float].__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
        rtti.check_fields(self)
        _BreaksAtChanges_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "BreaksAtChanges(%(source)s)" % self.__dict__
    
def BreaksAtChanges(source = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return BreaksAtChanges_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for BreaksAtChanges('+str(source) +':'+ str(type(source))+')')
