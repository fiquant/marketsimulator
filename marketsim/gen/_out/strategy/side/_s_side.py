from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._signal import Signal
from marketsim import context
@registry.expose(["Side function", "S_Side"])
class S_Side_strategysideSignal(IFunctionSide):
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
        return "S_Side(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.side._source import Source_strategysideSignal as _strategy_side_Source_strategysideSignal
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideSignal as _strategy_side_Threshold_strategysideSignal
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._less import Less_FloatFloat as _ops_Less_FloatFloat
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Source_strategysideSignal(self.x)),deref_opt(_constant_Float(deref_opt(_strategy_side_Threshold_strategysideSignal(self.x)))))),deref_opt(_side_Buy_()),deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Less_FloatFloat(deref_opt(_strategy_side_Source_strategysideSignal(self.x)),deref_opt(_constant_Float((0-deref_opt(_strategy_side_Threshold_strategysideSignal(self.x))))))),deref_opt(_side_Sell_()),deref_opt(_side_Nothing_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def S_Side(x = None): 
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Signal):
        return S_Side_strategysideSignal(x)
    raise Exception('Cannot find suitable overload for S_Side('+str(x) +':'+ str(type(x))+')')
