from marketsim.gen._intrinsic.observable import fold
from marketsim import ops, event, _
import math

class Variance_Impl(fold.Last):

    def __init__(self):
        self.reset()
        self._event = event.subscribe(self.source, _(self)._update, self)

    @property
    def source(self):
        return self.x.source


    def reset(self):
        self._x = None
        self._t = 0
        self._startT = 0
        self._avg = 0
        self._avg2 = 0

    def _increments(self, t, ti, mean, x):
        dX = x - mean
        dT = t - ti
        T = t - self._startT
        R = dX * dT / T
        return R, (ti - self._startT) * dX * R


    def _at(self, t):
        dM, dM2 = self._increments(t, self._t, self._avg, self._x)
        return self._avg + dM, self._avg2 + dM2

    def at(self, t):
        if self._x is not None and t > self._startT:
            avg, avg2 = self._at(t)
            return math.sqrt(avg2 / (t - self._startT))
        else:
            return None

    def update(self, t, x):
        if x is not None:
            if self._x is not None and t > self._startT:
                dM, dM2 = self._increments(t, self._t, self._avg, self._x)
                self._avg += dM
                self._avg2 += dM2
            else:
                self._startT = t
            self._t = t
            self._x = x
