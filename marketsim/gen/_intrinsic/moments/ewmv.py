from marketsim import getLabel, event, _

from marketsim.gen._intrinsic.observable import fold
from marketsim.gen._out.math.EW._Avg import Avg

class EWMV_Impl(fold.Last):

    def __init__(self):
        self._mean = Avg(self.source, self.alpha) # TODO: handle source and alpha change
        self.reset()
        self._event = event.subscribe(self.source, _(self)._update, self)

    _internals = ['_mean']

    def reset(self):
        self._variance = None
        self._lastTime = None
        self._lastValue = None

    def at(self, t):
        x = self._lastValue
        if x is not None:
            if self._variance is None:
                self._variance = 0
                self._lastTime = t
            mean = self._mean()
            delta = x - mean
            # NB! this formula is not verified!!!
            alpha = (1 - (1 - self.alpha)**( t - self._lastTime))
            return (1 - alpha) * (self._variance + delta * delta * alpha)

    def update(self, time, value):
        self._mean.update(time, value)
        if value is not None:
            self._variance = self.at(time)
            self._lastValue = value
            self._lastTime = time
