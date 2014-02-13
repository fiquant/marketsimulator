from marketsim.gen._intrinsic.observable.minmax_eps import MinEpsilon_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import float
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_IObservableFloatIFunctionFloat(Observable[float],MinEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes less than the old value minus *epsilon*
    """ 
    def __init__(self, source = None, epsilon = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
        self.epsilon = epsilon if epsilon is not None else _constant_Float(0.01)
        
        rtti.check_fields(self)
        MinEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'epsilon' : IFunction[float]
    }
    def __repr__(self):
        return "Min_{\\epsilon}(%(source)s)" % self.__dict__
    
def MinEpsilon(source = None,epsilon = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunction[float]):
            return MinEpsilon_IObservableFloatIFunctionFloat(source,epsilon)
    raise Exception('Cannot find suitable overload for MinEpsilon('+str(source)+','+str(epsilon)+')')
