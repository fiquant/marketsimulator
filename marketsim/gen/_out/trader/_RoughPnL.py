from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Trader", "RoughPnL"])
class RoughPnL_IAccount(Observablefloat):
    """   It takes into account only the best price of the order queue
    """ 
    def __init__(self, trader = None):
        from marketsim import deref_opt
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        Observablefloat.__init__(self)
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "RoughPnL(%(trader)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._add import Add_IObservableFloatIObservableFloat as _ops_Add_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._naivecumulativeprice import NaiveCumulativePrice_IOrderBookIObservableFloat as _orderbook_NaiveCumulativePrice_IOrderBookIObservableFloat
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out.trader._balance import Balance_IAccount as _trader_Balance_IAccount
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        return deref_opt(_ops_Add_IObservableFloatIObservableFloat(deref_opt(_trader_Balance_IAccount(self.trader)),deref_opt(_orderbook_NaiveCumulativePrice_IOrderBookIObservableFloat(deref_opt(_orderbook_OfTrader_IAccount(self.trader)),deref_opt(_trader_Position_IAccount(self.trader))))))
    
def RoughPnL(trader = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return RoughPnL_IAccount(trader)
    raise Exception('Cannot find suitable overload for RoughPnL('+str(trader) +':'+ str(type(trader))+')')
