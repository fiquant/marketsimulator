from marketsim import registry
from marketsim import listOf
from marketsim import listOf
from marketsim import IFunction
@registry.expose(["Strategy", "array_ChooseTheBest"])
class array_ChooseTheBest(IFunction[listOf(float), listOf(float)]):
    """ 
    """ 
    def __init__(self):
        pass
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "array_ChooseTheBest" % self.__dict__
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._ChooseTheBest import ChooseTheBest
        array = array if array is not None else []
        
        return ChooseTheBest(array)
    
