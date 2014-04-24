# generated with class generator.python.curried$after_typing$Curried
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat import IFunctionIFunctionlistOffloat_from_listOffloat
@registry.expose(["Strategy", "array_ChooseTheBest"])
class array_ChooseTheBest_(IFunctionIFunctionlistOffloat_from_listOffloat):
    """ **Function returning an array of length *len(array)***
    
      having 1 at the index of the maximal element and 0 are at the rest
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "array_ChooseTheBest" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._choosethebest import ChooseTheBest_ListFloat as _strategy_weight_ChooseTheBest_ListFloat
        array = array if array is not None else []
        
        return _strategy_weight_ChooseTheBest_ListFloat(array)
    
def array_ChooseTheBest(): 
    from marketsim import rtti
    return array_ChooseTheBest_()
    raise Exception('Cannot find suitable overload for array_ChooseTheBest('++')')
