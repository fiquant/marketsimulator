from marketsim import registry
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
@registry.expose(["Order", "StopLoss"])
class StopLoss_IObservableIOrderFloat(ObservableIOrder,IObservableIOrder):
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
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out.order._limit import Limit_SideFloatFloat as _order_Limit_SideFloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.proto = proto if proto is not None else deref_opt(_order_Limit_SideFloatFloat())
        self.maxloss = maxloss if maxloss is not None else deref_opt(_constant_Float(0.1))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservableIOrder,
        'maxloss' : IFunctionfloat
    }
    
    
    def on_proto_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'proto', value)
    
    
    
    
    def __repr__(self):
        return "StopLoss(%(proto)s, %(maxloss)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.stoploss import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        maxloss = self.maxloss()
        if maxloss is None: return None
        
        return Order_Impl(proto, maxloss)
    
def StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IObservableIOrder):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return StopLoss_IObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
