from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctioniorder import IFunctionIOrder
class IObservableIOrder(IEvent, IFunctionIOrder):
    @property
    def ImmediateOrCancel(self):
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        return ImmediateOrCancel(self)
    
    def Strategy(self, eventGen = None):
        from marketsim.gen._out.strategy._generic import Generic
        return Generic(self,eventGen)
    
    def StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._stoploss import StopLoss
        return StopLoss(self,maxloss)
    
    def WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._withexpiry import WithExpiry
        return WithExpiry(self,expiry)
    
    def Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._iceberg import Iceberg
        return Iceberg(self,lotSize)
    
    pass
