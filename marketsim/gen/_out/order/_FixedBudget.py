# generated with class generator.python.order_factory$Factory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
@registry.expose(["Order", "FixedBudget"])
class FixedBudget_SideFloat(ObservableIOrder,IObservableIOrder):
    """ **Factory creating fixed budget orders**
    
    
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    
    Parameters are:
    
    **side**
    	 function defining side of orders to create 
    
    **budget**
    	 function defining budget on which it may send orders at one time 
    """ 
    def __init__(self, side = None, budget = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.side = side if side is not None else deref_opt(_side_Sell_())
        self.budget = budget if budget is not None else deref_opt(_constant_Float(1000.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'budget' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "FixedBudget(%(side)s, %(budget)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.side.bind_ex(self._ctx_ex)
        self.budget.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.side.reset_ex(generation)
        self.budget.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.fixed_budget import Order_Impl
        side = self.side()
        if side is None: return None
        
        budget = self.budget()
        if budget is None: return None
        
        return Order_Impl(side, budget)
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
def FixedBudget(side = None,budget = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if budget is None or rtti.can_be_casted(budget, IFunctionfloat):
            return FixedBudget_SideFloat(side,budget)
    raise Exception('Cannot find suitable overload for FixedBudget('+str(side) +':'+ str(type(side))+','+str(budget) +':'+ str(type(budget))+')')
