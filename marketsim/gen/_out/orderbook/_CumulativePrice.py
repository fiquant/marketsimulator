# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.orderbook.cumulative_price import CumulativePrice_Impl
@registry.expose(["Asset", "CumulativePrice"])
class CumulativePrice_IOrderBookFloat(Observablefloat,CumulativePrice_Impl):
    """ **Returns price for best orders of total volume *depth***
    
    
      In other words cumulative price corresponds to trader balance change
      if a market order of volume *depth* is completely matched
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    
    Parameters are:
    
    **book**
    
    **depth**
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        Observablefloat.__init__(self)
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        self.depth = depth if depth is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        CumulativePrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "CumulativePrice(%(book)s, %(depth)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.depth.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
def CumulativePrice(book = None,depth = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IFunctionfloat):
            return CumulativePrice_IOrderBookFloat(book,depth)
    raise Exception('Cannot find suitable overload for CumulativePrice('+str(book) +':'+ str(type(book))+','+str(depth) +':'+ str(type(depth))+')')
