from marketsim import ops, event, _

import fold

class Lagged_Impl(fold.Last):

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
