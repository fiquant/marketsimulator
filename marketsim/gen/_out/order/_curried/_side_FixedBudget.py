from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "FixedBudget"])
class side_FixedBudget_IFunctionFloat(IFunction[IOrderGenerator, IFunction[Side]]):
    """ 
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    """ 
    def __init__(self, budget = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.budget = budget if budget is not None else _constant_Float(1000.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'budget' : IFunction[float]
    }
    def __repr__(self):
        return "FixedBudget(%(budget)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._fixedbudget import FixedBudget
        side = side if side is not None else _side_Sell_()
        budget = self.budget
        return FixedBudget(side, budget)
    
def side_FixedBudget(budget = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if budget is None or rtti.can_be_casted(budget, IFunction[float]):
        return side_FixedBudget_IFunctionFloat(budget)
    raise Exception('Cannot find suitable overload for side_FixedBudget('+str(budget)+')')
