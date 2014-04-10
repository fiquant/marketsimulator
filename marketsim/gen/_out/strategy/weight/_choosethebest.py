# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionlistoffloat import IFunctionlistOffloat
from marketsim.gen._intrinsic.strategy.weight import ChooseTheBest_Impl
from marketsim import listOf
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListFloat(IFunctionlistOffloat,ChooseTheBest_Impl):
    """ **Function returning an array of length *len(array)***
    
      having 1 at the index of the maximal element and 0 are at the rest
    
    Parameters are:
    
    **array**
    """ 
    def __init__(self, array = None):
        from marketsim import rtti
        self.array = array if array is not None else []
        rtti.check_fields(self)
        ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    
    
    def __repr__(self):
        return "ChooseTheBest(%(array)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def ChooseTheBest(array = None): 
    from marketsim import listOf
    from marketsim import rtti
    if array is None or rtti.can_be_casted(array, listOf(float)):
        return ChooseTheBest_ListFloat(array)
    raise Exception('Cannot find suitable overload for ChooseTheBest('+str(array) +':'+ str(type(array))+')')
def chooseTheBest(): 
    from marketsim.gen._out.strategy.weight.array._array_choosethebest import array_ChooseTheBest_ as _strategy_weight_array_array_ChooseTheBest_
    from marketsim import rtti
    return _strategy_weight_array_array_ChooseTheBest_()
    raise Exception('Cannot find suitable overload for chooseTheBest('++')')
