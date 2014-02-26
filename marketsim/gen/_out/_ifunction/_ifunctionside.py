from marketsim.gen._out._side import Side
from marketsim import meta
class IFunctionSide(object):
    _types = [meta.function((),Side)]
    @property
    def volume_price_Limit(self):
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit
        return volume_price_Limit(self)
    
    def LiquidityProvider(self, initialValue = None,priceDistr = None,book = None):
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
        return LiquidityProvider(self,initialValue,priceDistr,book)
    
    def Limit(self, price = None,volume = None):
        from marketsim.gen._out.order._limit import Limit
        return Limit(self,price,volume)
    
    def Market(self, volume = None):
        from marketsim.gen._out.order._market import Market
        return Market(self,volume)
    
    @property
    def volume_Market(self):
        from marketsim.gen._out.order._curried._volume_market import volume_Market
        return volume_Market(self)
    
    def FixedBudget(self, budget = None):
        from marketsim.gen._out.order._fixedbudget import FixedBudget
        return FixedBudget(self,budget)
    
    def price_Limit(self, volume = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        return price_Limit(self,volume)
    
    def volume_Limit(self, price = None):
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit
        return volume_Limit(self,price)
    
    pass



