from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.observable.minmax_eps import MaxEpsilon_Impl
from marketsim import registry
from marketsim import float
@registry.expose(["Statistics", "MaxEpsilon"])
class MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float],MaxEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes greater than the old value plus *epsilon*
    """ 
    def __init__(self, source = None, epsilon = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _constant()
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.epsilon = epsilon if epsilon is not None else _constant(0.01)
        if isinstance(epsilon, types.IEvent):
            event.subscribe(self.epsilon, self.fire, self)
        rtti.check_fields(self)
        MaxEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[float],
        'epsilon' : IFunction[float]
    }
    def __repr__(self):
        return "Max_{\\epsilon}(%(source)s)" % self.__dict__
    
def MaxEpsilon(source = None,epsilon = None): 
    return MaxEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__(source,epsilon)
