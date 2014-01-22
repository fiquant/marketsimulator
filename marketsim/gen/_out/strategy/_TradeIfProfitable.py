from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IAccount
from marketsim.gen._out.strategy._Suspendable import Suspendable as _strategy_Suspendable
from marketsim import context
@registry.expose(["Strategy", "TradeIfProfitable"])
class TradeIfProfitable(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, inner = None, account = None, performance = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out.strategy.account.inner._inner_VirtualMarket import inner_VirtualMarket as _strategy_account_inner_inner_VirtualMarket
        from marketsim.gen._out.strategy.weight.trader._trader_EfficiencyTrend import trader_EfficiencyTrend as _strategy_weight_trader_trader_EfficiencyTrend
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.inner = inner if inner is not None else _strategy_Noise()
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_EfficiencyTrend()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'account' : IFunction[IAccount,ISingleAssetStrategy]
        
        ,
        'performance' : IFunction[IFunction[float],IAccount]
        
        
    }
    def __repr__(self):
        return "TradeIfProfitable(%(inner)s, %(account)s, %(performance)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Suspendable(self.inner,self.performance(self.account(self.inner))>=0)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
