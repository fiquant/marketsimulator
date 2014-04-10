from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.lagged import Lagged_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Basic", "Lagged"])
class Lagged_IObservableFloatFloat(Observablefloat,Lagged_Impl):
    """ **Observable that adds a lag to an observable data source**
    
      so Lagged(x, dt)(t0+dt) == x(t0)
    
    Parameters are:
    
    **source**
    	 observable data source 
    
    **timeframe**
    	 lag size 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
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
    
    
    def on_source_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'source', value)
    
    
    
    
    def __repr__(self):
        return "Lagged_{%(timeframe)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.source.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Lagged(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Lagged_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for Lagged('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
