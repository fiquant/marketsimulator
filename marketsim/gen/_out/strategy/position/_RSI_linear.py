from marketsim import ISingleAssetTrader
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Volume function", "RSI_linear"])
class RSI_linear_FloatIObservableFloatFloatISingleAssetTrader(Observable[float]):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, timeframe = None, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.alpha = alpha if alpha is not None else (1.0/14.0)
        self.k = k if k is not None else _const_Float(-0.04)
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.trader = trader if trader is not None else _trader_SingleProxy_()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservable[float],
        'timeframe' : float,
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "RSI_linear(%(alpha)s, %(k)s, %(timeframe)s, %(trader)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._rsi import RSI_IOrderBookFloatFloat as _math_RSI_IOrderBookFloatFloat
        from marketsim.gen._out.strategy.position._desiredposition import DesiredPosition_IObservableFloatISingleAssetTrader as _strategy_position_DesiredPosition_IObservableFloatISingleAssetTrader
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatIFunctionFloat as _observable_OnEveryDt_FloatIFunctionFloat
        from marketsim.gen._out.ops._mul import Mul_IFunctionFloatIObservableFloat as _ops_Mul_IFunctionFloatIObservableFloat
        from marketsim.gen._out.ops._sub import Sub_IFunctionFloatIFunctionFloat as _ops_Sub_IFunctionFloatIFunctionFloat
        return _strategy_position_DesiredPosition_IObservableFloatISingleAssetTrader(_observable_OnEveryDt_FloatIFunctionFloat(1.0,_ops_Mul_IFunctionFloatIObservableFloat(_ops_Sub_IFunctionFloatIFunctionFloat(_constant_Float(50.0),_math_RSI_IOrderBookFloatFloat(_orderbook_OfTrader_IAccount(self.trader),self.timeframe,self.alpha)),self.k)),self.trader)
    
def RSI_linear(alpha = None,k = None,timeframe = None,trader = None): 
    from marketsim import float
    from marketsim import IObservable
    from marketsim import ISingleAssetTrader
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        if k is None or rtti.can_be_casted(k, IObservable[float]):
            if timeframe is None or rtti.can_be_casted(timeframe, float):
                if trader is None or rtti.can_be_casted(trader, ISingleAssetTrader):
                    return RSI_linear_FloatIObservableFloatFloatISingleAssetTrader(alpha,k,timeframe,trader)
    raise Exception('Cannot find suitable overload for RSI_linear('+str(alpha)+','+str(k)+','+str(timeframe)+','+str(trader)+')')
