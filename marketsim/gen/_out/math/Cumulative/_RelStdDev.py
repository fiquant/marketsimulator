from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_IObservableFloat(Function[float]):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
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
        from marketsim.gen._out.ops._div import Div_IFunctionFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.ops._sub import Sub_IFunctionFloatIFunctionFloat as _ops_Sub
        from marketsim.gen._out.math.Cumulative._avg import Avg_IObservableFloat as _math_Cumulative_Avg
        from marketsim.gen._out.math.Cumulative._stddev import StdDev_IObservableFloat as _math_Cumulative_StdDev
        return _ops_Div(_ops_Sub(self.source,_math_Cumulative_Avg(self.source)),_math_Cumulative_StdDev(self.source))
    
def RelStdDev(source = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        return RelStdDev_IObservableFloat(source)
    raise Exception("Cannot find suitable overload")
