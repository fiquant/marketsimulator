from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import context
@registry.expose(["Asset", "MidPrice"])
class MidPrice_IOrderBook(Observablefloat):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import event
        Observablefloat.__init__(self)
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "MidPrice(%(book)s)" % self.__dict__
    
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
        from marketsim import deref_opt
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.ops._add import Add_IObservableFloatIObservableFloat as _ops_Add_IObservableFloatIObservableFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Add_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(self.book)))),deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(self.book)))))),deref_opt(_constant_Float(2.0))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def MidPrice(book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return MidPrice_IOrderBook(book)
    raise Exception('Cannot find suitable overload for MidPrice('+str(book) +':'+ str(type(book))+')')
