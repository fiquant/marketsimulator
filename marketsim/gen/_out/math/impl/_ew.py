from marketsim import registry
from marketsim.gen._out._iew import IEW
from marketsim.gen._intrinsic._constant import _Empty_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "EW"])
class EW_IObservableFloatFloat(IEW,_Empty_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        _Empty_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'alpha' : float
    }
    def __repr__(self):
        return "EW_{%(alpha)s}(%(source)s)" % self.__dict__
    
def EW(source = None,alpha = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return EW_IObservableFloatFloat(source,alpha)
    raise Exception('Cannot find suitable overload for EW('+str(source) +':'+ str(type(source))+','+str(alpha) +':'+ str(type(alpha))+')')
