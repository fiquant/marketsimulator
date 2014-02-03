from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IObservable
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.source = source if source is not None else _const()
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'alpha' : float
    }
    def __repr__(self):
        return "RSD_{\\alpha=%(alpha)s}(%(source)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.math.EW._StdDev import StdDev as _math_EW_StdDev
        return (self.source-_math_EW_Avg(self.source,self.alpha))/_math_EW_StdDev(self.source,self.alpha)
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
