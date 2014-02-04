from marketsim import registry
from marketsim.gen._intrinsic.strategy.weight import _ChooseTheBest_Impl
from marketsim import float
from marketsim import listOf
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_Optional_List__Float__(_ChooseTheBest_Impl):
    """   having 1 at the index of the maximal element and 0 are at the rest
    """ 
    def __init__(self, array = None):
        from marketsim import rtti
        self.array = array if array is not None else []
        rtti.check_fields(self)
        _ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    def __repr__(self):
        return "ChooseTheBest(%(array)s)" % self.__dict__
    
ChooseTheBest = ChooseTheBest_Optional_List__Float__
