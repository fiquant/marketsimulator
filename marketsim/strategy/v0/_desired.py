from marketsim import event, _, Side, types
from marketsim.order import ImmediateOrCancel
from marketsim.types import *
from .._basic import Strategy
from .._wrap import wrapper2

class _Desired_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.desiredPosition, _(self)._wakeUp, self)

    def _wakeUp(self, dummy):
        gap = self.desiredPosition() - self._trader.actual
        order = ImmediateOrCancel(gap)
        self._trader.send(order)

exec  wrapper2("Desired",
             """ Generic strategy that tries to keep trader's position equal to *desiredPosition*,

                 Parameters:

                     |desiredPosition|
                         Observable telling desired position for the trader

             """,
              [('desiredPosition',      'None',                'types.IObservable[float]')],
               register=False)