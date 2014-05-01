# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "WeightedPrice"])
class WeightedPrice_IOrderQueueFloat(IFunctionfloat):
    """ **Returns moving average of trade prices weighted by their volumes**
    
    
    Parameters are:
    
    **queue**
    
    **alpha**
    	 parameter alpha for the moving average  
    """ 
    def __init__(self, queue = None, alpha = None):
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        self.alpha = alpha if alpha is not None else 0.15
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'alpha' : float
    }
    
    
    
    
    def __repr__(self):
        return "Price_{%(alpha)s}^{%(queue)s}" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.queue.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.queue.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.orderbook._lasttradevolume import LastTradeVolume_IOrderQueue as _orderbook_LastTradeVolume_IOrderQueue
        from marketsim.gen._out.orderbook._lasttradeprice import LastTradePrice_IOrderQueue as _orderbook_LastTradePrice_IOrderQueue
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_ops_Mul_IObservableFloatIObservableFloat(deref_opt(_orderbook_LastTradePrice_IOrderQueue(self.queue)),deref_opt(_orderbook_LastTradeVolume_IOrderQueue(self.queue)))),self.alpha)))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_LastTradeVolume_IOrderQueue(self.queue)),self.alpha))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def WeightedPrice(queue = None,alpha = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return WeightedPrice_IOrderQueueFloat(queue,alpha)
    raise Exception('Cannot find suitable overload for WeightedPrice('+str(queue) +':'+ str(type(queue))+','+str(alpha) +':'+ str(type(alpha))+')')
