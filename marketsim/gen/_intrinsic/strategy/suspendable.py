from marketsim import (_, event)

from basic import Strategy

from marketsim.gen._out._intrinsic_base.strategy.suspendable import Suspendable_Base

class Suspendable_Impl(Strategy, Suspendable_Base):

    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.inner.on_order_created, _(self).onOrderCreated, self)

    @property
    def suspended(self):
        return not self.predicate()

    def onOrderCreated(self, order, source):
        if self.predicate():
            self._send(order)
