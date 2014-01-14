from marketsim import ops, observable, event, _

class _Score_Impl(object):

    def __init__(self):
        self._efficiency = observable.Efficiency(self.trader)
        event.subscribe(
                observable.OnEveryDt(1, self._efficiency),
                 _(self)._update, self)
        self._score = 1
        self._last = 0

    def _update(self, dummy):
        e = self._efficiency()
        if e is not None:
            delta = e - self._last
            if delta > 0: self._score += 1
            if delta < 0 and self._score > 1: self._score -= 1

    def __call__(self):
        return self._score
