from marketsim.gen._out.strategy.side._pairtrading import PairTrading
from marketsim.gen._out._side import Side
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Side"])
class Side_strategysidePairTrading(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloatIOrderBook as _strategy_side_PairTrading_IOrderBookFloatIOrderBook
        from marketsim import event
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._factor import Factor_strategysidePairTrading as _strategy_side_Factor_strategysidePairTrading
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_IObservableFloatIOrderBook as _strategy_side_FundamentalValue_IObservableFloatIOrderBook
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._book import Book_strategysidePairTrading as _strategy_side_Book_strategysidePairTrading
        from marketsim.gen._out.strategy.side._booktodependon import BookToDependOn_strategysidePairTrading as _strategy_side_BookToDependOn_strategysidePairTrading
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        return deref_opt(_strategy_side_FundamentalValue_IObservableFloatIOrderBook(deref_opt(_ops_Mul_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_BookToDependOn_strategysidePairTrading(self.x)))),deref_opt(_constant_Float(deref_opt(_strategy_side_Factor_strategysidePairTrading(self.x)))))),deref_opt(_strategy_side_Book_strategysidePairTrading(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Side(x = None): 
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Side_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Side('+str(x) +':'+ str(type(x))+')')
