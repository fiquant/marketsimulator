# generated with class generator.python.order_factory_on_proto$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_StopLoss"])
class side_price_StopLoss_SideFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
    """ **Factory creating StopLoss orders**
    
    
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    
    Parameters are:
    
    **proto**
    	 underlying orders to create 
    
    **maxloss**
    	 maximal acceptable loss factor 
    """ 
    def __init__(self, proto = None, maxloss = None):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_side_price_Limit_Float())
        self.maxloss = maxloss if maxloss is not None else deref_opt(_constant_Float(0.1))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide,
        'maxloss' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "price_StopLoss(%(proto)s, %(maxloss)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.proto.bind_ex(self._ctx_ex)
        self.maxloss.bind_ex(self._ctx_ex)
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
        self.maxloss.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        side = side if side is not None else deref_opt(_side_Sell_())
        proto = self.proto
        maxloss = self.maxloss
        return price_StopLoss(proto(side), maxloss)
    
def side_price_StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return side_price_StopLoss_SideFloatIObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for side_price_StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
