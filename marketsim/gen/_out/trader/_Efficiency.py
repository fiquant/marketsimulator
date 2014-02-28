from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import context
@registry.expose(["Trader", "Efficiency"])
class Efficiency_IAccount(Observablefloat):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import call
        from marketsim import event
        Observablefloat.__init__(self)
        self.trader = trader if trader is not None else call(_trader_SingleProxy_,)
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
        return "Efficiency(%(trader)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._add import Add_IObservableFloatIObservableFloat as _ops_Add_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._cumulativeprice import CumulativePrice_IOrderBookFloat as _orderbook_CumulativePrice_IOrderBookFloat
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import call
        from marketsim.gen._out.trader._balance import Balance_IAccount as _trader_Balance_IAccount
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        return call(_ops_Add_IObservableFloatIObservableFloat,call(_trader_Balance_IAccount,self.trader),call(_orderbook_CumulativePrice_IOrderBookFloat,call(_orderbook_OfTrader_IAccount,self.trader),call(_trader_Position_IAccount,self.trader)))
    
def Efficiency(trader = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return Efficiency_IAccount(trader)
    raise Exception('Cannot find suitable overload for Efficiency('+str(trader) +':'+ str(type(trader))+')')
