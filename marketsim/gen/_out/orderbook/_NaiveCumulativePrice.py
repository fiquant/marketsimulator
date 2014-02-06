from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import context
from marketsim import float
@registry.expose(["Asset", "NaiveCumulativePrice"])
class NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__(Observable[Price]):
    """   by taking into account prices only for the best order
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out._constant import constant as _constant
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader()
        self.depth = depth if depth is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction[float]
    }
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
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
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.orderbook.ask._Price import Price as _orderbook_ask_Price
        from marketsim.gen._out.ops._Mul import Mul as _ops_Mul
        from marketsim.gen._out.ops._Less import Less as _ops_Less
        from marketsim.gen._out.orderbook.bid._Price import Price as _orderbook_bid_Price
        from marketsim.gen._out.ops._Condition_Float import Condition_Float as _ops_Condition_Float
        from marketsim.gen._out.observable._Price import Price as _observable_Price
        from marketsim.gen._out.ops._Greater import Greater as _ops_Greater
        return _observable_Price(_ops_Condition_Float(_ops_Less(self.depth,_const(0.0)),_ops_Mul(self.depth,_orderbook_ask_Price(self.book)),_ops_Condition_Float(_ops_Greater(self.depth,_const(0.0)),_ops_Mul(self.depth,_orderbook_bid_Price(self.book)),_const(0.0))))
    
def NaiveCumulativePrice(book = None,depth = None): 
    return NaiveCumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__(book,depth)
