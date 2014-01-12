from marketsim.gen._intrinsic.event import _After_Impl
from marketsim import IFunction
class After(_After_Impl):
    """ 
    """ 
    def __init__(self, delay = None):
        from marketsim.gen._out._constant import constant as _constant
        self.delay = delay if delay is not None else _constant(10.0)
        _After_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'delay' : IFunction[float]
    }
    def __repr__(self):
        return "After(%(delay)s)" % self.__dict__
    
