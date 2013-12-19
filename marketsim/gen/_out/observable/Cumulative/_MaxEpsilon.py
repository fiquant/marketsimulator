from marketsim import registry
from marketsim.gen._intrinsic.observable.minmax_eps import MaxEpsilon_Impl
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Basic", "MaxEpsilon"])
class MaxEpsilon(MaxEpsilon_Impl):
    """ 
    """ 
    def __init__(self, source = None, epsilon = None):
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.source = source if source is not None else constant()
        self.epsilon = epsilon if epsilon is not None else constant(0.01)
        MaxEpsilon_Impl.__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        if isinstance(epsilon, types.IEvent):
            event.subscribe(self.epsilon, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction,
        'epsilon' : IFunction
    }
    def __repr__(self):
        return "Max_{\\epsilon}(%(source)s)" % self.__dict__
    
