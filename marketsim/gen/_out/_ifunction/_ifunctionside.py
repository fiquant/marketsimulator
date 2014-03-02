from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .Side
class IFunctionSide(object):
    _types = [meta.function((),Side)]
    _types.append(IFunctionobject)
    def price_Limit(self, volume = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        return price_Limit(self,volume)
    
    def Limit(self, price = None,volume = None):
        from marketsim.gen._out.order._limit import Limit
        return Limit(self,price,volume)
    
    def Market(self, volume = None):
        from marketsim.gen._out.order._market import Market
        return Market(self,volume)
    
    def FixedBudget(self, budget = None):
        from marketsim.gen._out.order._fixedbudget import FixedBudget
        return FixedBudget(self,budget)
    
    pass



