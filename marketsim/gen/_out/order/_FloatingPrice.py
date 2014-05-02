# generated with class generator.python.order_factory$Factory
from marketsim import registry
from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Order", "FloatingPrice"])
class FloatingPrice_FloatIObservableIOrderIObservableFloat(Factory_Impl,IObservableIOrder):
    """ **Factory creating orders with floating price**
    
    
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    
    Parameters are:
    
    **proto**
    	 underlying orders to create 
    
    **floatingPrice**
    	 observable defining price of orders to create 
    """ 
    def __init__(self, proto = None, floatingPrice = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideFloat as _order__curried_price_Limit_SideFloat
        from marketsim import deref_opt
        Factory_Impl.__init__(self)
        self.proto = proto if proto is not None else deref_opt(_order__curried_price_Limit_SideFloat())
        self.floatingPrice = floatingPrice if floatingPrice is not None else deref_opt(_const_Float(10.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionfloat,
        'floatingPrice' : IObservablefloat
    }
    
    
    
    
    
    def on_floatingPrice_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'floatingPrice', value)
    
    def __repr__(self):
        return "FloatingPrice(%(proto)s, %(floatingPrice)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.proto.bind_ex(self._ctx_ex)
        self.floatingPrice.bind_ex(self._ctx_ex)
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
        self.proto.reset_ex(generation)
        self.floatingPrice.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
def FloatingPrice(proto = None,floatingPrice = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionfloat):
        if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservablefloat):
            return FloatingPrice_FloatIObservableIOrderIObservableFloat(proto,floatingPrice)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(proto) +':'+ str(type(proto))+','+str(floatingPrice) +':'+ str(type(floatingPrice))+')')
