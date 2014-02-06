from marketsim import ISingleAssetTrader
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Volume
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Volume function", "RSI_linear"])
class RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_(Observable[Volume]):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, timeframe = None, trader = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import Volume
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import event
        Observable[Volume].__init__(self)
        self.alpha = alpha if alpha is not None else (1.0/14.0)
        self.k = k if k is not None else _const(-0.04)
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.trader = trader if trader is not None else _trader_SingleProxy()
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
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.strategy.position._DesiredPosition import DesiredPosition as _strategy_position_DesiredPosition
        from marketsim.gen._out.ops._Mul import Mul as _ops_Mul
        from marketsim.gen._out.math._RSI import RSI as _math_RSI
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        return _strategy_position_DesiredPosition(_observable_OnEveryDt(1.0,_ops_Mul(_ops_Sub(_const(50.0),_math_RSI(_orderbook_OfTrader(self.trader),self.timeframe,self.alpha)),self.k)),self.trader)
    
RSI_linear = RSI_linear_Optional__Float___Optional__IObservable__Float____Optional__Float___Optional__ISingleAssetTrader_
