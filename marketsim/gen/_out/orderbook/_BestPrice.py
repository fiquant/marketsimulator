# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.orderbook.props import BestPrice_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "BestPrice"])
class BestPrice_IOrderQueue(Observablefloat,BestPrice_Impl):
    """ **Returns best order price of *queue***
    
      Returns None is *queue* is empty
    
    Parameters are:
    
    **queue**
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        rtti.check_fields(self)
        BestPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    
    
    
    def __repr__(self):
        return "BestPrice(%(queue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        self.queue.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def BestPrice(queue = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return BestPrice_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for BestPrice('+str(queue) +':'+ str(type(queue))+')')
