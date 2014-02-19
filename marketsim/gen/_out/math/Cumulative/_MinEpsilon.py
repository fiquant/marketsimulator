from marketsim.gen._intrinsic.observable.minmax_eps import MinEpsilon_Impl
from marketsim.gen._out._observable import Observablefloat
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_IObservableFloatFloat(Observablefloat,MinEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes less than the old value minus *epsilon*
    """ 
    def __init__(self, source = None, epsilon = None):
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim.gen._out._observable import Observablefloat
        Observablefloat.__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        event.subscribe(self.source, self.fire, self)
        self.epsilon = epsilon if epsilon is not None else _constant_Float(0.01)
        
        rtti.check_fields(self)
        MinEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'epsilon' : IFunctionfloat
    }
    def __repr__(self):
        return "Min_{\\epsilon}(%(source)s)" % self.__dict__
    
def MinEpsilon(source = None,epsilon = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MinEpsilon_IObservableFloatFloat(source,epsilon)
    raise Exception('Cannot find suitable overload for MinEpsilon('+str(source) +':'+ str(type(source))+','+str(epsilon) +':'+ str(type(epsilon))+')')
