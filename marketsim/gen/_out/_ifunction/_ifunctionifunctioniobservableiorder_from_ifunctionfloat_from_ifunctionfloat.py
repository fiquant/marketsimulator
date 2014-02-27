from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionifunctionifunctioniorder_from_ifunctionfloat_from_ifunctionfloat import IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat_from_ifunctionfloat import IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionievent_from_ifunctionfloat_from_ifunctionfloat import IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionfloat
#(() => .Float) => ((() => .Float) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrder_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionfloat)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionfloat)
    _types.append(IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionfloat)
    _types.append(IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionfloat)
    def volume_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._volume_price_withexpiry import volume_price_WithExpiry
        return volume_price_WithExpiry(self,expiry)
    
    @property
    def volume_price_Peg(self):
        from marketsim.gen._out.order._curried._volume_price_peg import volume_price_Peg
        return volume_price_Peg(self)
    
    @property
    def volume_Peg(self):
        from marketsim.gen._out.order._curried._volume_peg import volume_Peg
        return volume_Peg(self)
    
    def volume_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._volume_floatingprice import volume_FloatingPrice
        return volume_FloatingPrice(self,floatingPrice)
    
    def volume_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._volume_price_stoploss import volume_price_StopLoss
        return volume_price_StopLoss(self,maxloss)
    
    @property
    def volume_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._volume_price_immediateorcancel import volume_price_ImmediateOrCancel
        return volume_price_ImmediateOrCancel(self)
    
    def volume_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._volume_price_floatingprice import volume_price_FloatingPrice
        return volume_price_FloatingPrice(self,floatingPrice)
    
    def volume_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._volume_price_iceberg import volume_price_Iceberg
        return volume_price_Iceberg(self,lotSize)
    
    pass



