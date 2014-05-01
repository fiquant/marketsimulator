# generated with class generator.python.order_factory_curried$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "FixedBudget"])
class side_FixedBudget_Float(IFunctionIObservableIOrder_from_IFunctionSide):
    """ **Factory creating fixed budget orders**
    
    
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    
    Parameters are:
    
    **budget**
    	 function defining budget on which it may send orders at one time 
    """ 
    def __init__(self, budget = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.budget = budget if budget is not None else deref_opt(_constant_Float(1000.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'budget' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "FixedBudget(%(budget)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.budget.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.budget.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._fixedbudget import FixedBudget
        side = side if side is not None else deref_opt(_side_Sell_())
        budget = self.budget
        return FixedBudget(side, budget)
    
def side_FixedBudget(budget = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if budget is None or rtti.can_be_casted(budget, IFunctionfloat):
        return side_FixedBudget_Float(budget)
    raise Exception('Cannot find suitable overload for side_FixedBudget('+str(budget) +':'+ str(type(budget))+')')
