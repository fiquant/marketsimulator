from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionifunctioniorder_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionievent_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
#((() => .Side),(() => .Float)) => ((() => .Float) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrder_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSideIFunctionfloat)
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



