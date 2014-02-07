from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "DownMovements"])
class DownMovements_IObservableFloatFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 10.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Downs_{%(timeframe)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.math._Max import Max as _math_Max
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.observable._Float import Float as _observable_Float
        from marketsim.gen._out.math._Lagged import Lagged as _math_Lagged
        return _observable_Float(_math_Max(_const(0.0),_ops_Sub(_math_Lagged(self.source,self.timeframe),self.source)))
    
def DownMovements(source = None,timeframe = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return DownMovements_IObservableFloatFloat(source,timeframe)
    raise Exception("Cannot find suitable overload")
