from marketsim import registry
from marketsim.gen._out._icumulative import ICumulative
from marketsim.gen._intrinsic._constant import _Empty_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Statistics", "Cumulative"])
class Cumulative_IObservableFloat(ICumulative,_Empty_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        _Empty_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "Cumulative(%(source)s)" % self.__dict__
    
def Cumulative(source = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return Cumulative_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for Cumulative('+str(source) +':'+ str(type(source))+')')
