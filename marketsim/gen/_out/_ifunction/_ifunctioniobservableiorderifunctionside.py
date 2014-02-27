from marketsim.gen._out._ifunction._ifunctionobjectifunctionside import IFunctionobjectIFunctionSide
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionieventifunctionside import IFunctionIEventIFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctioniorderifunctionside import IFunctionIFunctionIOrderIFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
#(() => .Side) => .IObservable[.IOrder]
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    _types.append(IFunctionobjectIFunctionSide)
    _types.append(IFunctionIFunctionIOrderIFunctionSide)
    _types.append(IFunctionIEventIFunctionSide)
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



