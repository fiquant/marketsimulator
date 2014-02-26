from marketsim.gen._out._ifunction import IFunctionSide
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim import meta
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
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



from marketsim.gen._out._ifunction import IFunctionSide
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim import meta
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]
    pass



