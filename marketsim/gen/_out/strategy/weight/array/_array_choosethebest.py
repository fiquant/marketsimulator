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
        pass
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "array_ChooseTheBest" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._choosethebest import ChooseTheBest_ListFloat as _strategy_weight_ChooseTheBest_ListFloat
        array = array if array is not None else []
        
        return _strategy_weight_ChooseTheBest_ListFloat(array)
    
def array_ChooseTheBest(): 
    from marketsim import rtti
    return array_ChooseTheBest_()
    raise Exception('Cannot find suitable overload for array_ChooseTheBest('++')')
