from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import registry
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
@registry.expose(["Order", "FixedBudget"])
class FixedBudget_SideFloat(ObservableIOrder,IObservableIOrder):
    """ 
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    """ 
    def __init__(self, side = None, budget = None):
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim.gen._out._iorder import IOrder
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        ObservableIOrder.__init__(self)
        self.side = side if side is not None else call(_side_Sell_,)
        
        self.budget = budget if budget is not None else call(_constant_Float,1000.0)
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'budget' : IFunctionfloat
    }
    def __repr__(self):
        return "FixedBudget(%(side)s, %(budget)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.fixed_budget import Order_Impl
        side = self.side()
        if side is None: return None
        
        budget = self.budget()
        if budget is None: return None
        
        return Order_Impl(side, budget)
    
def FixedBudget(side = None,budget = None): 
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if budget is None or rtti.can_be_casted(budget, IFunctionfloat):
            return FixedBudget_SideFloat(side,budget)
    raise Exception('Cannot find suitable overload for FixedBudget('+str(side) +':'+ str(type(side))+','+str(budget) +':'+ str(type(budget))+')')
