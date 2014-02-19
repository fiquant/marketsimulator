from marketsim import registry
from marketsim.gen._out._observable import Observablefloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_IObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim.gen._out._observable import Observablefloat
        Observablefloat.__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "RSD_{cumul}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math.Cumulative._avg import Avg_IObservableFloat as _math_Cumulative_Avg_IObservableFloat
        from marketsim.gen._out.math.Cumulative._stddev import StdDev_IObservableFloat as _math_Cumulative_StdDev_IObservableFloat
        return _ops_Div_IObservableFloatFloat(_ops_Sub_IObservableFloatFloat(self.source,_math_Cumulative_Avg_IObservableFloat(self.source)),_math_Cumulative_StdDev_IObservableFloat(self.source))
    
def RelStdDev(source = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return RelStdDev_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(source) +':'+ str(type(source))+')')
