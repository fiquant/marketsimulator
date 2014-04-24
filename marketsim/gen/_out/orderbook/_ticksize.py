# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.orderbook.props import TickSize_Impl
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["Asset", "TickSize"])
class TickSize_IOrderBook(IFunctionfloat,TickSize_Impl):
    """ **Returns tick size for the order *book***
    
    
    Parameters are:
    
    **book**
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
        TickSize_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    
    
    def __repr__(self):
        return "TickSize(%(book)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
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
        self.book.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
def TickSize(book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return TickSize_IOrderBook(book)
    raise Exception('Cannot find suitable overload for TickSize('+str(book) +':'+ str(type(book))+')')
