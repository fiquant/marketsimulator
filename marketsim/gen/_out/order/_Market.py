# generated with class generator.python.order_factory$Factory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
@registry.expose(["Order", "Market"])
class Market_SideFloat(ObservableIOrder,IObservableIOrder):
    """ **Factory creating market orders**
    
    
      Market order intructs buy or sell given volume immediately
    
    Parameters are:
    
    **side**
    	 function defining side of orders to create 
    
    **volume**
    	 function defining volume of orders to create 
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.side = side if side is not None else deref_opt(_side_Sell_())
        self.volume = volume if volume is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'volume' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Market(%(side)s, %(volume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.side.bind_ex(self._ctx_ex)
        self.volume.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.side.reset_ex(generation)
        self.volume.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.market import Order_Impl
        side = self.side()
        if side is None: return None
        
        volume = self.volume()
        if volume is None: return None
        if abs(volume) < 1: return None
        volume = int(volume)
        return Order_Impl(side, volume)
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
def Market(side = None,volume = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
            return Market_SideFloat(side,volume)
    raise Exception('Cannot find suitable overload for Market('+str(side) +':'+ str(type(side))+','+str(volume) +':'+ str(type(volume))+')')
