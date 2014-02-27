from marketsim.gen._out._ifunction._ifunctionifunctionobjectifunctionfloatifunctionfloat import IFunctionIFunctionobjectIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionieventifunctionfloatifunctionfloat import IFunctionIFunctionIEventIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionifunctioniorderifunctionfloatifunctionfloat import IFunctionIFunctionIFunctionIOrderIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionfloat import IFunctionIObservableIOrderIFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionobjectifunctionfloat import IFunctionobjectIFunctionfloat
#(() => .Float) => ((() => .Float) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]
    _types.append(IFunctionobjectIFunctionfloat)
    _types.append(IFunctionIFunctionobjectIFunctionfloatIFunctionfloat)
    _types.append(IFunctionIFunctionIFunctionIOrderIFunctionfloatIFunctionfloat)
    _types.append(IFunctionIFunctionIEventIFunctionfloatIFunctionfloat)
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



