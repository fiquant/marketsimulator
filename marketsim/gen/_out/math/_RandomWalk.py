from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.randomwalk import _RandomWalk_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Basic", "RandomWalk"])
class RandomWalk_FloatFloatFloatString(Observable[float],_RandomWalk_Impl):
    """ 
    """ 
    def __init__(self, initialValue = None, deltaDistr = None, intervalDistr = None, name = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out.math.random._normalvariate import normalvariate_FloatFloat as _math_random_normalvariate_FloatFloat
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.initialValue = initialValue if initialValue is not None else 0.0
        
        self.deltaDistr = deltaDistr if deltaDistr is not None else _math_random_normalvariate_FloatFloat(0.0,1.0)
        
        self.intervalDistr = intervalDistr if intervalDistr is not None else _math_random_expovariate_Float(1.0)
        
        self.name = name if name is not None else "-random-"
        
        rtti.check_fields(self)
        _RandomWalk_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'initialValue' : float,
        'deltaDistr' : IFunctionfloat,
        'intervalDistr' : IFunctionfloat,
        'name' : str
    }
    def __repr__(self):
        return "%(name)s" % self.__dict__
    
def RandomWalk(initialValue = None,deltaDistr = None,intervalDistr = None,name = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if initialValue is None or rtti.can_be_casted(initialValue, float):
        if deltaDistr is None or rtti.can_be_casted(deltaDistr, IFunctionfloat):
            if intervalDistr is None or rtti.can_be_casted(intervalDistr, IFunctionfloat):
                if name is None or rtti.can_be_casted(name, str):
                    return RandomWalk_FloatFloatFloatString(initialValue,deltaDistr,intervalDistr,name)
    raise Exception('Cannot find suitable overload for RandomWalk('+str(initialValue) +':'+ str(type(initialValue))+','+str(deltaDistr) +':'+ str(type(deltaDistr))+','+str(intervalDistr) +':'+ str(type(intervalDistr))+','+str(name) +':'+ str(type(name))+')')
