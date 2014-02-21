from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._ifunction import IFunctionIAccountISingleAssetStrategy
from marketsim import registry
from marketsim import context
from marketsim.gen._out._ifunction import IFunctionIFunctionfloatIAccount
@registry.expose(["Strategy", "TradeIfProfitable"])
class TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, inner = None, account = None, performance = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIObservableIOrder as _strategy_Noise_IEventSideIObservableIOrder
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim import event
        self.inner = inner if inner is not None else _strategy_Noise_IEventSideIObservableIOrder()
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket_()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_TraderEfficiencyTrend_Float()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'account' : IFunctionIAccountISingleAssetStrategy,
        'performance' : IFunctionIFunctionfloatIAccount
    }
    def __repr__(self):
        return "TradeIfProfitable(%(inner)s, %(account)s, %(performance)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._suspendable import Suspendable_ISingleAssetStrategyBoolean as _strategy_Suspendable_ISingleAssetStrategyBoolean
        from marketsim.gen._out.ops._greaterequal import GreaterEqual_FloatFloat as _ops_GreaterEqual_FloatFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        return _strategy_Suspendable_ISingleAssetStrategyBoolean(self.inner,_ops_GreaterEqual_FloatFloat(self.performance(self.account(self.inner)),_constant_Int(0)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def TradeIfProfitable(inner = None,account = None,performance = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim.gen._out._ifunction import IFunctionIAccountISingleAssetStrategy
    from marketsim.gen._out._ifunction import IFunctionIFunctionfloatIAccount
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if account is None or rtti.can_be_casted(account, IFunctionIAccountISingleAssetStrategy):
            if performance is None or rtti.can_be_casted(performance, IFunctionIFunctionfloatIAccount):
                return TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(inner,account,performance)
    raise Exception('Cannot find suitable overload for TradeIfProfitable('+str(inner) +':'+ str(type(inner))+','+str(account) +':'+ str(type(account))+','+str(performance) +':'+ str(type(performance))+')')
