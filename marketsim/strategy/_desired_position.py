from marketsim import event, _, Side, order, types, observable, trader, registry, signal
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2
from _periodic import Generic

class _DesiredPosition_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.desiredPosition, _(self)._wakeUp, self)
        
    def bind(self, ctx):    
        self._pendingVolume = observable.PendingVolume(ctx.trader)
        self._tradedVolume = observable.VolumeTraded(ctx.trader)
        
    def _wakeUp(self, dummy):
        desired = self.desiredPosition()
        if desired is not None:
            desired = int(desired)
            actual = self._tradedVolume() + self._pendingVolume()
            gap = desired - actual
            side = Side.Buy if gap > 0 else (Side.Sell if gap < 0 else None)
            if side is not None:
                order = self.orderFactory(side)(abs(gap))
                self._trader.send(order)
                        
exec  wrapper2("DesiredPosition", 
             """ Generic strategy that tries to keep trader's position equal to *desiredPosition*, 
             
                 Parameters:
                 
                     |desiredPosition|
                         Observable telling desired position for the trader
                         
                     |orderFactory|
                         order factory function (default: order.Limit.T)
                         
             """,
              [('desiredPosition',      'None',                'types.IObservable[float]'), 
               ('orderFactory',         'order.MarketFactory', 'Side -> Volume -> IOrder'),], 
               register=False)

class DesiredPosition2(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        pending = observable.PendingVolume(trader.SingleProxy())
        actual = observable.VolumeTraded(trader.SingleProxy())
        
        return {
            'signedVolume' : self.desiredPosition - pending - actual
        }
    
    def getImpl(self):
        return Generic(self.orderFactory(_.signedVolume), self.desiredPosition)

import _wrap
    
_wrap.strategy(DesiredPosition2, ['Desired position', 'Base'],
         """ 
         """,
          [
           ('desiredPosition',      'signal.RandomWalk()',                 'types.IObservable[float]'), 
           ('orderFactory',         'order.factory.SignedVolume_Market()', 'ISignedVolume_IOrderFactory')
          ], globals())
                
