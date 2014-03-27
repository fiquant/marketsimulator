from marketsim import  event, _

import fold

from marketsim.gen._out._intrinsic_base.observable.lagged import Lagged_Base

class Lagged_Impl(fold.Last, Lagged_Base):

    def __init__(self):
        self.reset()
        self._alias = ['_details', 'Lagged']
        self._event = event.subscribe(self.source, _(self)._update, self)

    def reset(self):
        self._backX = 0

    def at(self, t):
        return self._backX

    def _remove(self, x):
        self._backX = x
        self.fire(self)

    def update(self, t, x):
        self._scheduler.scheduleAfter(self.timeframe, _(self, x)._remove)
