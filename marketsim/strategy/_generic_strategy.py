from marketsim.types import *
from marketsim import registry, meta, bind, types, Side, mathutils, order, Event, event

from _basic import Strategy

class _GenericStrategy_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        event.subscribe(self.trader.orderBook.on_price_changed, self._wakeUp, self)

    def _wakeUp_impl(self, _):
        print "hello"


exec