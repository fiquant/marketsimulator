from marketsim import registry
from marketsim.gen._out import const
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.observable.ewma import EWMA_Impl



@registry.expose(['Statistics', 'EWMA'])
class EWMA(Function[float], EWMA_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        self.source = source if source is not None else const()
        self.alpha = alpha if alpha is not None else 0.015
        EWMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable,
        'alpha' : float
    }
    def __repr__(self):
        return "Avg_{%alpha}^{%source}" % self.__dict__
    
