from marketsim import registry
from marketsim import Volume
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Asset's", "LastTradeVolume"])
class LastTradeVolume(Observable[Volume]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim import Volume
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        from marketsim import _
        from marketsim import event
        Observable[Volume].__init__(self)
        self.book = book if book is not None else _observable_orderbook_OfTrader()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "LastTradeVolume(Ask_{%(book)s})" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume as _observable_orderbook_LastTradeVolume
        from marketsim.gen._out.observable.orderbook._Asks import Asks as _observable_orderbook_Asks
        return _observable_orderbook_LastTradeVolume(_observable_orderbook_Asks(self.book))
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
