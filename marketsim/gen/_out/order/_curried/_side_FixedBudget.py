from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "FixedBudget"])
class side_FixedBudget(IFunction[IOrderGenerator, IFunction[Side]
]):
    """ 
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
        return "side_FixedBudget(%(budget)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.order._FixedBudget import FixedBudget
        side = side if side is not None else _side_Sell()
        budget = self.budget
        return FixedBudget(side, budget)
    
