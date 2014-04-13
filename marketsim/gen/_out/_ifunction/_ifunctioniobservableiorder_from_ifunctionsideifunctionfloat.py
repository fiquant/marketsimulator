from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctioniorder_from_ifunctionsideifunctionfloat import IFunctionIFunctionIOrder_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionievent_from_ifunctionsideifunctionfloat import IFunctionIEvent_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
#((() => .Side),(() => .Float)) => .IObservable[.IOrder]
class IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionIOrder_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIEvent_from_IFunctionSideIFunctionfloat)
    def sideprice_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._sideprice_stoploss import sideprice_StopLoss
        return sideprice_StopLoss(self,maxloss)
    
    def Ladder(self, initialSize = None,side = None):
        from marketsim.gen._out.strategy.price._ladder import Ladder
        return Ladder(self,initialSize,side)
    
    def sideprice_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._sideprice_withexpiry import sideprice_WithExpiry
        return sideprice_WithExpiry(self,expiry)
    
    def LadderMM(self, initialSize = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM
        return LadderMM(self,initialSize)
    
    def sideprice_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._sideprice_iceberg import sideprice_Iceberg
        return sideprice_Iceberg(self,lotSize)
    
    @property
    def sideprice_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._sideprice_immediateorcancel import sideprice_ImmediateOrCancel
        return sideprice_ImmediateOrCancel(self)
    
    pass



