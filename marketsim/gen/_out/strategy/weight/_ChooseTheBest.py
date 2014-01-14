from marketsim import registry
from marketsim.gen._intrinsic.strategy.weight import _ChooseTheBest_Impl
from marketsim import listOf
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest(_ChooseTheBest_Impl):
    """ 
    """ 
    def __init__(self, array = None):
        self.array = array if array is not None else []
        _ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    def __repr__(self):
        return "ChooseTheBest(%(array)s)" % self.__dict__
    
