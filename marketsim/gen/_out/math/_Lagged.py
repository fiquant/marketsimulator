from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.lagged import Lagged_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Basic", "Lagged"])
class Lagged_IObservableFloatFloat(Observablefloat,Lagged_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 10.0
        
        rtti.check_fields(self)
        Lagged_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "Lagged_{%(timeframe)s}(%(source)s)" % self.__dict__
    
def Lagged(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Lagged_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for Lagged('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
