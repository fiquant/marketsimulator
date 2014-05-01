# generated with class generator.python.order_factory_curried$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "Limit"])
class side_Limit_FloatFloat(IFunctionIObservableIOrder_from_IFunctionSide):
    """ **Factory creating limit orders**
    
    
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    
    Parameters are:
    
    **price**
    	 function defining price of orders to create 
    
    **volume**
    	 function defining volume of orders to create 
    """ 
    def __init__(self, price = None, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.price = price if price is not None else deref_opt(_constant_Float(100.0))
        self.volume = volume if volume is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunctionfloat,
        'volume' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "Limit(%(price)s, %(volume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.price.bind_ex(self._ctx_ex)
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
        
        self.price.reset_ex(generation)
        self.volume.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._limit import Limit
        side = side if side is not None else deref_opt(_side_Sell_())
        price = self.price
        volume = self.volume
        return Limit(side, price, volume)
    
def side_Limit(price = None,volume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunctionfloat):
        if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
            return side_Limit_FloatFloat(price,volume)
    raise Exception('Cannot find suitable overload for side_Limit('+str(price) +':'+ str(type(price))+','+str(volume) +':'+ str(type(volume))+')')
