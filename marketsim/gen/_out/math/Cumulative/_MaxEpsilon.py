from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.minmax_eps import MaxEpsilon_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Statistics", "MaxEpsilon"])
class MaxEpsilon_IObservableFloatFloat(Observable[float],MaxEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes greater than the old value plus *epsilon*
    """ 
    def __init__(self, source = None, epsilon = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
        self.epsilon = epsilon if epsilon is not None else _constant_Float(0.01)
        
        rtti.check_fields(self)
        MaxEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'epsilon' : IFunctionfloat
    }
    def __repr__(self):
        return "Max_{\\epsilon}(%(source)s)" % self.__dict__
    
def MaxEpsilon(source = None,epsilon = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MaxEpsilon_IObservableFloatFloat(source,epsilon)
    raise Exception('Cannot find suitable overload for MaxEpsilon('+str(source) +':'+ str(type(source))+','+str(epsilon) +':'+ str(type(epsilon))+')')
