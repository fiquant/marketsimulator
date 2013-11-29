from marketsim import registry, types, _, IObservable
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.observable.ewma import EWMA_Impl
from marketsim.gen._out._const import const

@registry.expose(['Statistics', 'EWMA'])
class EWMA(Function[float], EWMA_Impl):
    """ 
    """ 
    def __init__(self, source = None , alpha = None):
        self._source = source if source is not None else const(1.)
        self._alpha = alpha if alpha is not None else 0.015
        EWMA_Impl.__init__(self)

    @property
    def label(self):
        return repr(self)

    @property
    def source(self):
        return self._source

    @property
    def alpha(self):
        return self._alpha

    _properties = {
        'source' : IObservable,
        'alpha' : float
    }

    def __repr__(self):
        return "Avg_{%alpha}^{%source}" % self.__dict__



