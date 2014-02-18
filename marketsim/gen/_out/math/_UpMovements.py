from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import context
@registry.expose(["Basic", "UpMovements"])
class UpMovements_IObservableFloatFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        self.timeframe = timeframe if timeframe is not None else 10.0
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
        return "Ups_{%(timeframe)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._max import Max_FloatIObservableFloat as _math_Max_FloatIObservableFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIObservableFloat as _ops_Sub_IObservableFloatIObservableFloat
        from marketsim.gen._out.math._lagged import Lagged_IObservableFloatFloat as _math_Lagged_IObservableFloatFloat
        return _math_Max_FloatIObservableFloat(_constant_Float(0.0),_ops_Sub_IObservableFloatIObservableFloat(self.source,_math_Lagged_IObservableFloatFloat(self.source,self.timeframe)))
    
def UpMovements(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return UpMovements_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for UpMovements('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
