from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Side function", "PairTrading"])
class PairTrading(Observable[Side]):
    """ 
    """ 
    def __init__(self, dependee = None, factor = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.dependee = dependee if dependee is not None else _observable_orderbook_OfTrader()
        self.factor = factor if factor is not None else 1.0
        self.book = book if book is not None else _observable_orderbook_OfTrader()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'dependee' : IOrderBook,
        'factor' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "PairTrading(%(dependee)s, %(factor)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._ObservableSide import ObservableSide as _observable_ObservableSide
        from marketsim.gen._out.observable.sidefunc._FundamentalValue import FundamentalValue as _observable_sidefunc_FundamentalValue
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice as _observable_orderbook_MidPrice
        from marketsim.gen._out._const import const as _const
        return _observable_ObservableSide(_observable_sidefunc_FundamentalValue(_observable_orderbook_MidPrice(self.dependee)*_const(self.factor),self.book))
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
