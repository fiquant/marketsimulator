from marketsim.gen._out._side import Side
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue_IObservableFloatIOrderBook(ObservableSide):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        ObservableSide.__init__(self)
        self.fv = fv if fv is not None else _const_Float(200.0)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IObservablefloat,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "FundamentalValue(%(fv)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._less import Less_IObservableFloatIObservableFloat as _ops_Less_IObservableFloatIObservableFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIObservableFloat as _ops_Greater_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        return _ops_Condition_IObservableBooleanSideIObservableSide(_ops_Greater_IObservableFloatIObservableFloat(_orderbook_BestPrice_IOrderQueue(_orderbook_Bids_IOrderBook(self.book)),self.fv),_side_Sell_(),_ops_Condition_IObservableBooleanSideSide(_ops_Less_IObservableFloatIObservableFloat(_orderbook_BestPrice_IOrderQueue(_orderbook_Asks_IOrderBook(self.book)),self.fv),_side_Buy_(),_side_Nothing_()))
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._side import Side
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue_FloatIOrderBook(ObservableSide):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._side import Side
        from marketsim import event
        ObservableSide.__init__(self)
        self.fv = fv if fv is not None else _constant_Float(200.0)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunctionfloat,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "FundamentalValue(%(fv)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        return _ops_Condition_IObservableBooleanSideIObservableSide(_ops_Greater_IObservableFloatFloat(_orderbook_BestPrice_IOrderQueue(_orderbook_Bids_IOrderBook(self.book)),self.fv),_side_Sell_(),_ops_Condition_IObservableBooleanSideSide(_ops_Less_IObservableFloatFloat(_orderbook_BestPrice_IOrderQueue(_orderbook_Asks_IOrderBook(self.book)),self.fv),_side_Buy_(),_side_Nothing_()))
    
def FundamentalValue(fv = None,book = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if fv is None or rtti.can_be_casted(fv, IObservablefloat):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return FundamentalValue_IObservableFloatIOrderBook(fv,book)
    if fv is None or rtti.can_be_casted(fv, IFunctionfloat):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return FundamentalValue_FloatIOrderBook(fv,book)
    raise Exception('Cannot find suitable overload for FundamentalValue('+str(fv) +':'+ str(type(fv))+','+str(book) +':'+ str(type(book))+')')
