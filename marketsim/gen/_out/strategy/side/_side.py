# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._noise import Noise
@registry.expose(["Side function", "Side"])
class Side_strategysideNoise(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._noise import Noise_Float as _strategy_side_Noise_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Noise_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Noise
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._side_distribution import Side_distribution_strategysideNoise as _strategy_side_Side_distribution_strategysideNoise
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Side_distribution_strategysideNoise(self.x)),deref_opt(_constant_Float(0.5)))),deref_opt(_side_Buy_()),deref_opt(_side_Sell_())))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
@registry.expose(["Side function", "Side"])
class Side_strategysideMeanReversion(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import rtti
        from marketsim import _
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import event
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_Float as _strategy_side_MeanReversion_Float
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.strategy.side._fundamental_value import Fundamental_Value_strategysideMeanReversion as _strategy_side_Fundamental_Value_strategysideMeanReversion
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.strategy.side._book import book_strategysideMeanReversion as _strategy_side_book_strategysideMeanReversion
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanSideIObservableSide(deref_opt(_ops_Greater_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(deref_opt(_strategy_side_book_strategysideMeanReversion(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysideMeanReversion(self.x)))),deref_opt(_side_Sell_()),deref_opt(_ops_Condition_IObservableBooleanSideSide(deref_opt(_ops_Less_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(deref_opt(_strategy_side_book_strategysideMeanReversion(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysideMeanReversion(self.x)))),deref_opt(_side_Buy_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._rsibis import RSIbis
@registry.expose(["Side function", "Side"])
class Side_strategysideRSIbis(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis_FloatFloatFloat as _strategy_side_RSIbis_FloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_RSIbis_FloatFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSIbis
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideRSIbis as _strategy_side_Threshold_strategysideRSIbis
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value_strategysideRSIbis as _strategy_side_Signal_Value_strategysideRSIbis
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideRSIbis(self.x)),deref_opt(_constant_Float(deref_opt(_strategy_side_Threshold_strategysideRSIbis(self.x)))))),deref_opt(_side_Buy_()),deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Less_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideRSIbis(self.x)),deref_opt(_constant_Float((0-deref_opt(_strategy_side_Threshold_strategysideRSIbis(self.x))))))),deref_opt(_side_Sell_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
@registry.expose(["Side function", "Side"])
class Side_strategysideFundamentalValue(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import rtti
        from marketsim import _
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_Float as _strategy_side_FundamentalValue_Float
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import event
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_Float())
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
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatFloat as _ops_Greater_IObservableFloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.ops._less import Less_IObservableFloatFloat as _ops_Less_IObservableFloatFloat
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.strategy.side._book import book_strategysideFundamentalValue as _strategy_side_book_strategysideFundamentalValue
        from marketsim.gen._out.strategy.side._fundamental_value import Fundamental_Value_strategysideFundamentalValue as _strategy_side_Fundamental_Value_strategysideFundamentalValue
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanSideIObservableSide(deref_opt(_ops_Greater_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(deref_opt(_strategy_side_book_strategysideFundamentalValue(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysideFundamentalValue(self.x)))),deref_opt(_side_Sell_()),deref_opt(_ops_Condition_IObservableBooleanSideSide(deref_opt(_ops_Less_IObservableFloatFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(deref_opt(_strategy_side_book_strategysideFundamentalValue(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysideFundamentalValue(self.x)))),deref_opt(_side_Buy_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
@registry.expose(["Side function", "Side"])
class Side_strategysideTrendFollower(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideTrendFollower as _strategy_side_Threshold_strategysideTrendFollower
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value_strategysideTrendFollower as _strategy_side_Signal_Value_strategysideTrendFollower
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideTrendFollower(self.x)),deref_opt(_constant_Float(deref_opt(_strategy_side_Threshold_strategysideTrendFollower(self.x)))))),deref_opt(_side_Buy_()),deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Less_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideTrendFollower(self.x)),deref_opt(_constant_Float((0-deref_opt(_strategy_side_Threshold_strategysideTrendFollower(self.x))))))),deref_opt(_side_Sell_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
@registry.expose(["Side function", "Side"])
class Side_strategysideCrossingAverages(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value_strategysideCrossingAverages as _strategy_side_Signal_Value_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideCrossingAverages as _strategy_side_Threshold_strategysideCrossingAverages
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideCrossingAverages(self.x)),deref_opt(_constant_Float(deref_opt(_strategy_side_Threshold_strategysideCrossingAverages(self.x)))))),deref_opt(_side_Buy_()),deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Less_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideCrossingAverages(self.x)),deref_opt(_constant_Float((0-deref_opt(_strategy_side_Threshold_strategysideCrossingAverages(self.x))))))),deref_opt(_side_Sell_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._signal import Signal
@registry.expose(["Side function", "Side"])
class Side_strategysideSignal(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal
    }
    
    
    def __repr__(self):
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value_strategysideSignal as _strategy_side_Signal_Value_strategysideSignal
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideSignal as _strategy_side_Threshold_strategysideSignal
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideSignal(self.x)),deref_opt(_constant_Float(deref_opt(_strategy_side_Threshold_strategysideSignal(self.x)))))),deref_opt(_side_Buy_()),deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Less_FloatFloat(deref_opt(_strategy_side_Signal_Value_strategysideSignal(self.x)),deref_opt(_constant_Float((0-deref_opt(_strategy_side_Threshold_strategysideSignal(self.x))))))),deref_opt(_side_Sell_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
@registry.expose(["Side function", "Side"])
class Side_strategysidePairTrading(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloat as _strategy_side_PairTrading_IOrderBookFloat
        from marketsim import rtti
        from marketsim import _
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import event
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
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
        return "Side(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.reset_ex(generation)
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
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideSide as _ops_Condition_IObservableBooleanSideSide
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids_IOrderBook
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.strategy.side._fundamental_value import Fundamental_Value_strategysidePairTrading as _strategy_side_Fundamental_Value_strategysidePairTrading
        from marketsim.gen._out.strategy.side._book import book_strategysidePairTrading as _strategy_side_book_strategysidePairTrading
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._less import Less_IObservableFloatIObservableFloat as _ops_Less_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIObservableFloat as _ops_Greater_IObservableFloatIObservableFloat
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanSideIObservableSide as _ops_Condition_IObservableBooleanSideIObservableSide
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanSideIObservableSide(deref_opt(_ops_Greater_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Bids_IOrderBook(deref_opt(_strategy_side_book_strategysidePairTrading(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysidePairTrading(self.x)))),deref_opt(_side_Sell_()),deref_opt(_ops_Condition_IObservableBooleanSideSide(deref_opt(_ops_Less_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(deref_opt(_orderbook_Asks_IOrderBook(deref_opt(_strategy_side_book_strategysidePairTrading(self.x)))))),deref_opt(_strategy_side_Fundamental_Value_strategysidePairTrading(self.x)))),deref_opt(_side_Buy_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Side(x = None): 
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim import rtti
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim.gen._out.strategy.side._noise import Noise
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    if x is None or rtti.can_be_casted(x, Noise):
        return Side_strategysideNoise(x)
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Side_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Side_strategysideRSIbis(x)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Side_strategysideFundamentalValue(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Side_strategysideTrendFollower(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Side_strategysideCrossingAverages(x)
    if x is None or rtti.can_be_casted(x, Signal):
        return Side_strategysideSignal(x)
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Side_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Side('+str(x) +':'+ str(type(x))+')')
