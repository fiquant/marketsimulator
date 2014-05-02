# generated with class generator.python.intrinsic_observable$Import
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.orderbook.queue import BestPrice_Impl
from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl

class BestPriceImpl_orderbookIOrderQueueImpl(Observablefloat,BestPrice_Impl):
    """ 
    """ 
    def __init__(self, queue ):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.queue = queue
        rtti.check_fields(self)
        BestPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueueImpl
    }
    
    
    
    def __repr__(self):
        return "BestPriceImpl(%(queue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.queue.bind_ex(self._ctx_ex)
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
        self.queue.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        BestPrice_Impl.bind_impl(self, ctx)
    
    def reset(self):
        BestPrice_Impl.reset(self)
    
def BestPriceImpl(queue = None): 
    from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueueImpl):
        return BestPriceImpl_orderbookIOrderQueueImpl(queue)
    raise Exception('Cannot find suitable overload for BestPriceImpl('+str(queue) +':'+ str(type(queue))+')')
