from marketsim import event, _

from marketsim.gen._out.trader._efficiency import Efficiency
from marketsim.gen._out.observable._oneverydt import OnEveryDt

from marketsim.gen._out._intrinsic_base.strategy.weight import Score_Base, ChooseTheBest_Base, Identity_Base

class Score_Impl(Score_Base):

    def __init__(self):
        self._efficiency = Efficiency(self.trader)
        event.subscribe(
                OnEveryDt(self._efficiency, 1),
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

class ChooseTheBest_Impl(ChooseTheBest_Base):

    def __call__(self):
        mw = max(self.array)
        # index of the strategy with the highest (positive) efficiency
        max_idx = self.array.index(mw)
        weights = [0] * len(self.array)

        if mw > 0:
            weights[max_idx] = 1

        return weights

class Identity_Impl(Identity_Base):

    def __call__(self):
        return self.array
