from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim import meta
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    pass



from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim import meta
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    def RSI_linear(self, alpha = None,k = None,timeframe = None):
        from marketsim.gen._out.strategy._rsi_linear import RSI_linear
        return RSI_linear(self,alpha,k,timeframe)
    
    def price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        return price_Iceberg(self,lotSize)
    
    def price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        return price_StopLoss(self,maxloss)
    
    @property
    def price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._price_immediateorcancel import price_ImmediateOrCancel
        return price_ImmediateOrCancel(self)
    
    @property
    def price_Peg(self):
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        return price_Peg(self)
    
    def volume_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._volume_stoploss import volume_StopLoss
        return volume_StopLoss(self,maxloss)
    
    def volume_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._volume_withexpiry import volume_WithExpiry
        return volume_WithExpiry(self,expiry)
    
    @property
    def volume_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._volume_immediateorcancel import volume_ImmediateOrCancel
        return volume_ImmediateOrCancel(self)
    
    def volume_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._volume_iceberg import volume_Iceberg
        return volume_Iceberg(self,lotSize)
    
    def price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        return price_FloatingPrice(self,floatingPrice)
    
    def price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry
        return price_WithExpiry(self,expiry)
    
    def FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        return FloatingPrice(self,floatingPrice)
    
    @property
    def Peg(self):
        from marketsim.gen._out.order._peg import Peg
        return Peg(self)
    
    def Bollinger_linear(self, alpha = None,k = None):
        from marketsim.gen._out.strategy._bollinger_linear import Bollinger_linear
        return Bollinger_linear(self,alpha,k)
    
    pass



