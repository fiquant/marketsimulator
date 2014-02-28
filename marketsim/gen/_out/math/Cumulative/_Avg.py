from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.cma import CMA_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "Avg"])
class Avg_IObservableFloat(IDifferentiable,CMA_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        CMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "Avg_{cumul}(%(source)s)" % self.__dict__
    
def Avg(source = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return Avg_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for Avg('+str(source) +':'+ str(type(source))+')')
