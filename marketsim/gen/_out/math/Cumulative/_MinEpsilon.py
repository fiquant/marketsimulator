from marketsim.gen._intrinsic.observable.minmax_eps import MinEpsilon_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import float
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float],MinEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes less than the old value minus *epsilon*
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
        MinEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[float],
        'epsilon' : IFunction[float]
    }
    def __repr__(self):
        return "Min_{\\epsilon}(%(source)s)" % self.__dict__
    
MinEpsilon = MinEpsilon_Optional__IFunction__Float____Optional__IFunction__Float__
