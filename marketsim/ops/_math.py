from marketsim import registry, types, ops
import math
@registry.expose(['Log/Pow', 'Exp'])
class Exp(ops.Observable[float]):
    """  Return e**x 
    """    

    def __init__(self, source = ops.Constant[float](1.0)):
        Observable[float].__init__(self)
        
        self.source = source
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = { 
        'source' : types.IFunction[float]
    }
    
    def __repr__(self):
        return "e^{%(source)s}" % self.__dict__

    def __call__(self, *args, **kwargs):
        source = self.source()
        if source is None: return None
        return math.exp(source)

