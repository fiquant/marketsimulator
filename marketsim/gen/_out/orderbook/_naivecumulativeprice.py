# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim import context
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Asset", "NaiveCumulativePrice"])
class NaiveCumulativePrice_IOrderBookIObservableFloat(Observablefloat):
    """ **Returns naive approximation of price for best orders of total volume *depth***
    
      by taking into account prices only for the best order
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    
    Parameters are:
    
    **book**
    
    **depth**
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        Observablefloat.__init__(self)
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        self.depth = depth if depth is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IObservablefloat
    }
    
    
    
    
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.book.bind_ex(self._ctx_ex)
        self.depth.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self.impl.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableFloatIObservableFloat as _ops_Condition_IObservableBooleanIObservableFloatIObservableFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableFloatFloat as _ops_Condition_IObservableBooleanIObservableFloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanIObservableFloatIObservableFloat(deref_opt(_ops_Less_IObservableFloatFloat(self.depth,deref_opt(_constant_Float(0.0)))),deref_opt(_ops_Mul_IObservableFloatIObservableFloat(self.depth,deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(self.book)))))),deref_opt(_ops_Condition_IObservableBooleanIObservableFloatFloat(deref_opt(_ops_Greater_IObservableFloatFloat(self.depth,deref_opt(_constant_Float(0.0)))),deref_opt(_ops_Mul_IObservableFloatIObservableFloat(self.depth,deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(self.book)))))),deref_opt(_constant_Float(0.0))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim import context
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Asset", "NaiveCumulativePrice"])
class NaiveCumulativePrice_IOrderBookFloat(Observablefloat):
    """ **Returns naive approximation of price for best orders of total volume *depth***
    
      by taking into account prices only for the best order
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    
    Parameters are:
    
    **book**
    
    **depth**
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        Observablefloat.__init__(self)
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        self.depth = depth if depth is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.book.bind_ex(self._ctx_ex)
        self.depth.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self.impl.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._condition import Condition_BooleanIObservableFloatIObservableFloat as _ops_Condition_BooleanIObservableFloatIObservableFloat
        from marketsim.gen._out.ops._mul import Mul_FloatIObservableFloat as _ops_Mul_FloatIObservableFloat
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_BooleanIObservableFloatFloat as _ops_Condition_BooleanIObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanIObservableFloatIObservableFloat(deref_opt(_ops_Less_FloatFloat(self.depth,deref_opt(_constant_Float(0.0)))),deref_opt(_ops_Mul_FloatIObservableFloat(self.depth,deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(self.book)))))),deref_opt(_ops_Condition_BooleanIObservableFloatFloat(deref_opt(_ops_Greater_FloatFloat(self.depth,deref_opt(_constant_Float(0.0)))),deref_opt(_ops_Mul_FloatIObservableFloat(self.depth,deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(self.book)))))),deref_opt(_constant_Float(0.0))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def NaiveCumulativePrice(book = None,depth = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IObservablefloat):
            return NaiveCumulativePrice_IOrderBookIObservableFloat(book,depth)
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IFunctionfloat):
            return NaiveCumulativePrice_IOrderBookFloat(book,depth)
    raise Exception('Cannot find suitable overload for NaiveCumulativePrice('+str(book) +':'+ str(type(book))+','+str(depth) +':'+ str(type(depth))+')')
