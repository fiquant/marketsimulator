from marketsim import (_, event)

from basic import Strategy

class _Suspendable_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.inner.on_order_created, _(self).onOrderCreated, self)

    @property
    def suspended(self):
        return not self.predicate()

    def onOrderCreated(self, order, source):
        if self.predicate():
            self._send(order)
