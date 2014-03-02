from marketsim.gen._out._side import Side
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "FV_Side"])
class FV_Side_strategysideFundamentalValue(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    def __repr__(self):
        return "FV_Side(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._fv import Fv_strategysideFundamentalValue as _strategy_side_Fv_strategysideFundamentalValue
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._book import Book_strategysideFundamentalValue as _strategy_side_Book_strategysideFundamentalValue
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        return deref_opt(_ops_Condition_IObservableBooleanSideIObservableSide(deref_opt(_ops_Greater_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(deref_opt(_strategy_side_Book_strategysideFundamentalValue(self.x)))))),deref_opt(_strategy_side_Fv_strategysideFundamentalValue(self.x)))),deref_opt(_side_Sell_()),deref_opt(_ops_Condition_IObservableBooleanSideSide(deref_opt(_ops_Less_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(deref_opt(_strategy_side_Book_strategysideFundamentalValue(self.x)))))),deref_opt(_strategy_side_Fv_strategysideFundamentalValue(self.x)))),deref_opt(_side_Buy_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def FV_Side(x = None): 
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return FV_Side_strategysideFundamentalValue(x)
    raise Exception('Cannot find suitable overload for FV_Side('+str(x) +':'+ str(type(x))+')')
