# generated with class generator.python.order_factory_curried$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Market"])
class side_Market_Float(IFunctionIObservableIOrder_from_IFunctionSide):
    """ **Factory creating market orders**
    
    
      Market order intructs buy or sell given volume immediately
    
    Parameters are:
    
    **volume**
    	 function defining volume of orders to create 
    """ 
    def __init__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        self.volume = volume if volume is not None else deref_opt(_constant_Float(1.0))
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'volume' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Market(%(volume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.volume.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.volume.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.volume)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.volume.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._market import Market
        side = side if side is not None else deref_opt(_side_Sell_())
        volume = self.volume
        return Market(side, volume)
    
def side_Market(volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
        return side_Market_Float(volume)
    raise Exception('Cannot find suitable overload for side_Market('+str(volume) +':'+ str(type(volume))+')')
