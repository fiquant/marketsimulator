from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_strategypositionRSI_linear(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear_FloatIObservableFloatFloatISingleAssetTrader as _strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI_linear
    }
    def __repr__(self):
        return "DesiredPosition(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.strategy.position._trader import Trader_strategypositionRSI_linear as _strategy_position_Trader_strategypositionRSI_linear
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.position._k import K_strategypositionRSI_linear as _strategy_position_K_strategypositionRSI_linear
        from marketsim.gen._out.strategy.position._alpha import Alpha_strategypositionRSI_linear as _strategy_position_Alpha_strategypositionRSI_linear
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._sub import Sub_FloatIObservableFloat as _ops_Sub_FloatIObservableFloat
        from marketsim.gen._out.strategy.position._timeframe import Timeframe_strategypositionRSI_linear as _strategy_position_Timeframe_strategypositionRSI_linear
        from marketsim.gen._out.math._value import Value_mathRSI as _math_Value_mathRSI
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        return deref_opt(_ops_Mul_IObservableFloatIObservableFloat(deref_opt(_ops_Sub_FloatIObservableFloat(deref_opt(_constant_Float(50.0)),deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_math_Value_mathRSI(deref_opt(_math_RSI_IObservableFloatFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_orderbook_OfTrader_IAccount(deref_opt(_strategy_position_Trader_strategypositionRSI_linear(self.x)))))),deref_opt(_strategy_position_Timeframe_strategypositionRSI_linear(self.x)),deref_opt(_strategy_position_Alpha_strategypositionRSI_linear(self.x)))))),1.0)))),deref_opt(_strategy_position_K_strategypositionRSI_linear(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_strategypositionBollinger_linear(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear_FloatIObservableFloatISingleAssetTrader as _strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Bollinger_linear
    }
    def __repr__(self):
        return "DesiredPosition(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out.strategy.position._trader import Trader_strategypositionBollinger_linear as _strategy_position_Trader_strategypositionBollinger_linear
        from marketsim.gen._out.strategy.position._alpha import Alpha_strategypositionBollinger_linear as _strategy_position_Alpha_strategypositionBollinger_linear
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out.math._relstddev import RelStdDev_mathEW as _math_RelStdDev_mathEW
        from marketsim.gen._out.strategy.position._k import K_strategypositionBollinger_linear as _strategy_position_K_strategypositionBollinger_linear
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        return deref_opt(_ops_Mul_IObservableFloatIObservableFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_math_RelStdDev_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_orderbook_OfTrader_IAccount(deref_opt(_strategy_position_Trader_strategypositionBollinger_linear(self.x)))))),deref_opt(_strategy_position_Alpha_strategypositionBollinger_linear(self.x)))))),1.0)),deref_opt(_strategy_position_K_strategypositionBollinger_linear(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def DesiredPosition(x = None): 
    from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
    from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSI_linear):
        return DesiredPosition_strategypositionRSI_linear(x)
    if x is None or rtti.can_be_casted(x, Bollinger_linear):
        return DesiredPosition_strategypositionBollinger_linear(x)
    raise Exception('Cannot find suitable overload for DesiredPosition('+str(x) +':'+ str(type(x))+')')
