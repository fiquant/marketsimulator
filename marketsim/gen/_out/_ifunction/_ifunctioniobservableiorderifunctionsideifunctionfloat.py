from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
#((() => .Side),(() => .Float)) => .IObservable[.IOrder]
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    
    def sidevolume_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sidevolume_iceberg import sidevolume_Iceberg
        return sidevolume_Iceberg(self,lotSize)
    
    def sidevolume_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sidevolume_withexpiry import sidevolume_WithExpiry
        return sidevolume_WithExpiry(self,expiry)
    
    def sideprice_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sideprice_stoploss import sideprice_StopLoss
        return sideprice_StopLoss(self,maxloss)
    
    @property
    def sidevolume_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sidevolume_immediateorcancel import sidevolume_ImmediateOrCancel
        return sidevolume_ImmediateOrCancel(self)
    
    def sidevolume_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sidevolume_stoploss import sidevolume_StopLoss
        return sidevolume_StopLoss(self,maxloss)
    
    def sideprice_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sideprice_withexpiry import sideprice_WithExpiry
        return sideprice_WithExpiry(self,expiry)
    
    def sideprice_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sideprice_iceberg import sideprice_Iceberg
        return sideprice_Iceberg(self,lotSize)
    
    @property
    def sideprice_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sideprice_immediateorcancel import sideprice_ImmediateOrCancel
        return sideprice_ImmediateOrCancel(self)
    
    pass



