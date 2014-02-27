from marketsim.gen._out._ifunction._ifunctionobjectifunctionsideifunctionfloat import IFunctionobjectIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionieventifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIEventIFunctionfloatIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobjectifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionobjectIFunctionfloatIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionifunctioniorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIFunctionIOrderIFunctionfloatIFunctionSideIFunctionfloat
#((() => .Side),(() => .Float)) => ((() => .Float) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    _types.append(IFunctionobjectIFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionobjectIFunctionfloatIFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionIFunctionIOrderIFunctionfloatIFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionIEventIFunctionfloatIFunctionSideIFunctionfloat)
    def sidevolume_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sidevolume_price_withexpiry import sidevolume_price_WithExpiry
        return sidevolume_price_WithExpiry(self,expiry)
    
    @property
    def sidevolume_Peg(self):
        from marketsim.gen._out.order._curried._sidevolume_peg import sidevolume_Peg
        return sidevolume_Peg(self)
    
    def sidevolume_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sidevolume_price_stoploss import sidevolume_price_StopLoss
        return sidevolume_price_StopLoss(self,maxloss)
    
    def sidevolume_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice
        return sidevolume_FloatingPrice(self,floatingPrice)
    
    def sidevolume_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sidevolume_price_floatingprice import sidevolume_price_FloatingPrice
        return sidevolume_price_FloatingPrice(self,floatingPrice)
    
    @property
    def sidevolume_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sidevolume_price_immediateorcancel import sidevolume_price_ImmediateOrCancel
        return sidevolume_price_ImmediateOrCancel(self)
    
    @property
    def sidevolume_price_Peg(self):
        from marketsim.gen._out.order._curried._sidevolume_price_peg import sidevolume_price_Peg
        return sidevolume_price_Peg(self)
    
    def sidevolume_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sidevolume_price_iceberg import sidevolume_price_Iceberg
        return sidevolume_price_Iceberg(self,lotSize)
    
    pass



