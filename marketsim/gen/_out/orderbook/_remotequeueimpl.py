# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl
from marketsim.gen._intrinsic.orderbook.remote import Queue_Impl
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ilink import ILink

class RemoteQueueImpl_orderbookIOrderQueueImplIOrderBookILink(IOrderQueueImpl,Queue_Impl):
    """ 
    """ 
    def __init__(self, queue , book , link ):
        self.queue = queue
        self.book = book
        self.link = link
        Queue_Impl.__init__(self)
    
    
    _properties = {
        'queue' : IOrderQueueImpl,
        'book' : IOrderBook,
        'link' : ILink
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
        self.queue.bind_ex(self._ctx_ex)
        self.book.bind_ex(self._ctx_ex)
        self.link.bind_ex(self._ctx_ex)
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
        self.book.reset_ex(generation)
        self.link.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl
        from marketsim.gen._out._iorderbook import IOrderBook
        from marketsim.gen._out._ilink import ILink
        rtti.typecheck(IOrderQueueImpl, self.queue)
        rtti.typecheck(IOrderBook, self.book)
        rtti.typecheck(ILink, self.link)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.queue.registerIn(registry)
        self.book.registerIn(registry)
        self.link.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Queue_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Queue_Impl.reset(self)
    
def RemoteQueueImpl(queue = None,book = None,link = None): 
    from marketsim.gen._out.orderbook._iorderqueueimpl import IOrderQueueImpl
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ilink import ILink
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueueImpl):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            if link is None or rtti.can_be_casted(link, ILink):
                return RemoteQueueImpl_orderbookIOrderQueueImplIOrderBookILink(queue,book,link)
    raise Exception('Cannot find suitable overload for RemoteQueueImpl('+str(queue) +':'+ str(type(queue))+','+str(book) +':'+ str(type(book))+','+str(link) +':'+ str(type(link))+')')
