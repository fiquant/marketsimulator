from marketsim import registry
from marketsim.gen._intrinsic.strategy.weight import _ChooseTheBest_Impl
from marketsim import float
from marketsim import listOf
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListFloat(_ChooseTheBest_Impl):
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
    
def ChooseTheBest(array = None): 
    from marketsim import float
    from marketsim import listOf
    from marketsim import rtti
    if array is None or rtti.can_be_casted(array, listOf(float)):
        return ChooseTheBest_ListFloat(array)
    raise Exception("Cannot find suitable overload")
def chooseTheBest(): 
    from marketsim.gen._out.strategy.weight.array._array_choosethebest import array_ChooseTheBest_ as _strategy_weight_array_array_ChooseTheBest
    from marketsim import rtti
    return _strategy_weight_array_array_ChooseTheBest()
    raise Exception("Cannot find suitable overload")
