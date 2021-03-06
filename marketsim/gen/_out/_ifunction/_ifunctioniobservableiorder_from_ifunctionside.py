from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctioniorder_from_ifunctionside import IFunctionIFunctionIOrder_from_IFunctionSide
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionievent_from_ifunctionside import IFunctionIEvent_from_IFunctionSide
#(() => .Side) => .IObservable[.IOrder]
class IFunctionIObservableIOrder_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    _types.append(IFunctionobject_from_IFunctionSide)
    _types.append(IFunctionIFunctionIOrder_from_IFunctionSide)
    _types.append(IFunctionIEvent_from_IFunctionSide)
    def side_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._side_stoploss import side_StopLoss
        return side_StopLoss(self,maxloss)
    
    def side_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._side_withexpiry import side_WithExpiry
        return side_WithExpiry(self,expiry)
    
    @property
    def side_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._side_immediateorcancel import side_ImmediateOrCancel
        return side_ImmediateOrCancel(self)
    
    def side_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._side_iceberg import side_Iceberg
        return side_Iceberg(self,lotSize)
    
    pass



