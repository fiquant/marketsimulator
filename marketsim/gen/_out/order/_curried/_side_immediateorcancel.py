# generated with class generator.python.order_factory_on_proto$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
@registry.expose(["Order", "ImmediateOrCancel"])
class side_ImmediateOrCancel_SideIObservableIOrder(IFunctionIObservableIOrder_from_IFunctionSide):
    """ **Factory creating Immediate-Or-Cancel orders**
    
    
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    
    Parameters are:
    
    **proto**
    	 factory for underlying orders 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim import deref_opt
        self.proto = proto if proto is not None else deref_opt(_order__curried_side_Limit_FloatFloat())
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    
    
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.proto.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.proto.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
        rtti.typecheck(IFunctionIObservableIOrder_from_IFunctionSide, self.proto)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.proto.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        side = side if side is not None else deref_opt(_side_Sell_())
        proto = self.proto
        return ImmediateOrCancel(proto(side))
    
def side_ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSide):
        return side_ImmediateOrCancel_SideIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for side_ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
