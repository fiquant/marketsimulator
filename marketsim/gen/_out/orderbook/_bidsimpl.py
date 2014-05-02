# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl
from marketsim.gen._intrinsic.orderbook.local import Bids_Impl
from marketsim.gen._out._iorderbook import IOrderBook

class BidsImpl_FloatIOrderBook(IOrderQueueImpl,Bids_Impl):
    """ 
    """ 
    def __init__(self, tickSize , book ):
        from marketsim import rtti
        self.tickSize = tickSize
        self.book = book
        rtti.check_fields(self)
        Bids_Impl.__init__(self)
    
    
    _properties = {
        'tickSize' : float,
        'book' : IOrderBook
    }
    
    
    
    
    
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
        self.book.bind_ex(self._ctx_ex)
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
        self.book.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Bids_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Bids_Impl.reset(self)
    
def BidsImpl(tickSize = None,book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if tickSize is None or rtti.can_be_casted(tickSize, float):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return BidsImpl_FloatIOrderBook(tickSize,book)
    raise Exception('Cannot find suitable overload for BidsImpl('+str(tickSize) +':'+ str(type(tickSize))+','+str(book) +':'+ str(type(book))+')')
