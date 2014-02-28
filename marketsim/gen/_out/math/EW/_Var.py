from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.moments.ewmv import EWMV_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "Var"])
class Var_IObservableFloatFloat(IFunctionfloat,EWMV_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import call
        from marketsim import rtti
        self.source = source if source is not None else call(_const_Float,1.0)
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        EWMV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'alpha' : float
    }
    def __repr__(self):
        return "\\sigma^2_{\\alpha=%(alpha)s}(%(source)s)" % self.__dict__
    
def Var(source = None,alpha = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return Var_IObservableFloatFloat(source,alpha)
    raise Exception('Cannot find suitable overload for Var('+str(source) +':'+ str(type(source))+','+str(alpha) +':'+ str(type(alpha))+')')
