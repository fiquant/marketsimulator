from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.minmax import Max_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "Max"])
class Max_IObservableFloatFloat(Observablefloat,Max_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.source = source if source is not None else call(_const_Float,1.0)
        event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 100.0
        
        rtti.check_fields(self)
        Max_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "Max_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
def Max(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Max_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for Max('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
