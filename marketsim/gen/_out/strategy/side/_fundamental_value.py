from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
from marketsim import context
@registry.expose(["Side function", "Fundamental_Value"])
class Fundamental_Value_strategysideMeanReversion(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_Float as _strategy_side_MeanReversion_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    
    
    def __repr__(self):
        return "Fundamental_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideMeanReversion as _strategy_side_Alpha_strategysideMeanReversion
        from marketsim.gen._out.strategy.side._book import book_strategysideMeanReversion as _strategy_side_book_strategysideMeanReversion
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_book_strategysideMeanReversion(self.x)))),deref_opt(_strategy_side_Alpha_strategysideMeanReversion(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
from marketsim import context
@registry.expose(["Side function", "Fundamental_Value"])
class Fundamental_Value_strategysideFundamentalValue(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_Float as _strategy_side_FundamentalValue_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    
    
    def __repr__(self):
        return "Fundamental_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.strategy.side._fv import Fv_strategysideFundamentalValue as _strategy_side_Fv_strategysideFundamentalValue
        from marketsim import deref_opt
        return deref_opt(_strategy_side_Fv_strategysideFundamentalValue(self.x))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
from marketsim import context
@registry.expose(["Side function", "Fundamental_Value"])
class Fundamental_Value_strategysidePairTrading(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloat as _strategy_side_PairTrading_IOrderBookFloat
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloat())
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
        return "Fundamental_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._booktodependon import BookToDependOn_strategysidePairTrading as _strategy_side_BookToDependOn_strategysidePairTrading
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._factor import Factor_strategysidePairTrading as _strategy_side_Factor_strategysidePairTrading
        from marketsim import deref_opt
        return deref_opt(_ops_Mul_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_BookToDependOn_strategysidePairTrading(self.x)))),deref_opt(_constant_Float(deref_opt(_strategy_side_Factor_strategysidePairTrading(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Fundamental_Value(x = None): 
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Fundamental_Value_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Fundamental_Value_strategysideFundamentalValue(x)
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Fundamental_Value_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Fundamental_Value('+str(x) +':'+ str(type(x))+')')
