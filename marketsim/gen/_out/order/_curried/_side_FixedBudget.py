from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "FixedBudget"])
class side_FixedBudget(IFunction[IOrderGenerator, IFunction[Side]]):
    """ 
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    """ 
    def __init__(self, budget = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.budget = budget if budget is not None else _constant(1000.0)
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
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.order._FixedBudget import FixedBudget
        side = side if side is not None else _side_Sell()
        budget = self.budget
        return FixedBudget(side, budget)
    
side_FixedBudget = side_FixedBudget
