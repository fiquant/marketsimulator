from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["RSI", "Raw"])
class Raw_Optional__IObservable__Float____Optional__Float___Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None, alpha = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float,
        'alpha' : float
    }
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.math._UpMovements import UpMovements as _math_UpMovements
        from marketsim.gen._out.math._DownMovements import DownMovements as _math_DownMovements
        return _ops_Div(_math_EW_Avg(_math_UpMovements(self.source,self.timeframe),self.alpha),_math_EW_Avg(_math_DownMovements(self.source,self.timeframe),self.alpha))
    
Raw = Raw_Optional__IObservable__Float____Optional__Float___Optional__Float_
