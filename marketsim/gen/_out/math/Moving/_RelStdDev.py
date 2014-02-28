from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_IObservableFloatFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.timeframe = timeframe if timeframe is not None else 100.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "RSD_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
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
        from marketsim import deref_opt
        from marketsim.gen._out.math.moving._stddev import StdDev_IObservableFloatFloat as _math_Moving_StdDev_IObservableFloatFloat
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.math.moving._avg import Avg_IObservableFloatFloat as _math_Moving_Avg_IObservableFloatFloat
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(self.source,deref_opt(_math_Moving_Avg_IObservableFloatFloat(self.source,self.timeframe)))),deref_opt(_math_Moving_StdDev_IObservableFloatFloat(self.source,self.timeframe))))
    
def RelStdDev(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return RelStdDev_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
