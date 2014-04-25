# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
@registry.expose(["Strategy", "TradeIfProfitable"])
class TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(ISingleAssetStrategy):
    """ **Adaptive strategy that evaluates *inner* strategy efficiency**
    
      and if it is considered as good, sends orders
    
    Parameters are:
    
    **inner**
    	 wrapped strategy 
    
    **account**
    	 defines how strategy trades are booked:
    	 actually traded amount or virtual market orders are
    	 used in order to estimate how the strategy would have traded
    	 if all its orders appeared at market 
    
    **performance**
    	 given a trading account tells
    	 should it be considered as effective or not 
    """ 
    def __init__(self, inner = None, account = None, performance = None):
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim import deref_opt
        self.inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        self.account = account if account is not None else deref_opt(_strategy_account_inner_inner_VirtualMarket_())
        self.performance = performance if performance is not None else deref_opt(_strategy_weight_trader_trader_TraderEfficiencyTrend_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'account' : IFunctionIAccount_from_ISingleAssetStrategy,
        'performance' : IFunctionIFunctionfloat_from_IAccount
    }
    
    
    
    
    
    
    def __repr__(self):
        return "TradeIfProfitable(%(inner)s, %(account)s, %(performance)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.inner.bind_ex(self._ctx_ex)
        self.account.bind_ex(self._ctx_ex)
        self.performance.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy._suspendable import Suspendable_ISingleAssetStrategyBoolean as _strategy_Suspendable_ISingleAssetStrategyBoolean
        from marketsim.gen._out.ops._greaterequal import GreaterEqual_FloatFloat as _ops_GreaterEqual_FloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        return deref_opt(_strategy_Suspendable_ISingleAssetStrategyBoolean(self.inner,deref_opt(_ops_GreaterEqual_FloatFloat(deref_opt(self.performance(deref_opt(self.account(self.inner)))),deref_opt(_constant_Int(0))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    @property
    def suspended(self):
        return self.inner.suspended
    
    def set_suspended(self, value):
        self.inner.suspended = value
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def TradeIfProfitable(inner = None,account = None,performance = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if account is None or rtti.can_be_casted(account, IFunctionIAccount_from_ISingleAssetStrategy):
            if performance is None or rtti.can_be_casted(performance, IFunctionIFunctionfloat_from_IAccount):
                return TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(inner,account,performance)
    raise Exception('Cannot find suitable overload for TradeIfProfitable('+str(inner) +':'+ str(type(inner))+','+str(account) +':'+ str(type(account))+','+str(performance) +':'+ str(type(performance))+')')
