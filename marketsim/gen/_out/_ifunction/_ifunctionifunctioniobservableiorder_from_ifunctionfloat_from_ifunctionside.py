from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionfloat import IFunctionIObservableIOrder_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionievent_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSide
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionifunctionifunctioniorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSide
#(() => .Side) => ((() => .Float) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrder_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSide)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSide)
    _types.append(IFunctionIFunctionIFunctionIOrder_from_IFunctionfloat_from_IFunctionSide)
    _types.append(IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSide)
    def side_price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._side_price_stoploss import side_price_StopLoss
        return side_price_StopLoss(self,maxloss)
    
    def sideprice_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._sideprice_floatingprice import sideprice_FloatingPrice
        return sideprice_FloatingPrice(self,floatingPrice)
    
    @property
    def sideprice_Peg(self):
        from marketsim.gen._out.order._curried._sideprice_peg import sideprice_Peg
        return sideprice_Peg(self)
    
    @property
    def side_Peg(self):
        from marketsim.gen._out.order._curried._side_peg import side_Peg
        return side_Peg(self)
    
    def side_price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._side_price_iceberg import side_price_Iceberg
        return side_price_Iceberg(self,lotSize)
    
    @property
    def side_price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._side_price_immediateorcancel import side_price_ImmediateOrCancel
        return side_price_ImmediateOrCancel(self)
    
    def side_price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._side_price_floatingprice import side_price_FloatingPrice
        return side_price_FloatingPrice(self,floatingPrice)
    
    def side_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._side_floatingprice import side_FloatingPrice
        return side_FloatingPrice(self,floatingPrice)
    
    def side_price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._side_price_withexpiry import side_price_WithExpiry
        return side_price_WithExpiry(self,expiry)
    
    @property
    def side_price_Peg(self):
        from marketsim.gen._out.order._curried._side_price_peg import side_price_Peg
        return side_price_Peg(self)
    
    pass



