from marketsim import types, _, ops, getLabel
import fold
from _stddev import StdDevRolling, MovingVariance



class Rolling(fold.Last, ops.Observable[float]):
    def __init__(self, source, window, wait=True):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self.window = window
        self.wait = wait # wait for enough values to calculate
        self.reset()

    _properties = {'window': float}

    def reset(self):
        self._x = None
        self._t = -1
        self._startT = -1

    def at(self, t):
        print "at", t, self._t, self._startT, self._x
        return self._x if self._t - self._startT == 1 else None

    def update(self, t, x):
        if x is not None:
            params = self.determineParams(t, x)
            self._scheduler.scheduleAfter(self.window, _(self, t, x, params)._remove)
            self._add(t, x)
        self.fire(self)

    def _add(self, t, x):
        self._x = x
        self._t = t

    def _remove(self, t, x, params):
        pass

    def determineParams(self, t, x):
        return {}


from math import log


class RollingLogReturns(Rolling):

    def __init__(self, source):
        Rolling.__init__(self, source, window=2)  # window = 2 because we look at the two last values

    def _add(self, t, x):
        print "add", t, self._startT, self._t
        if t - self._startT == self.window - 1 and self._x:
            self._x = log(x) - self._x
        else:
            self._x = log(x)
            self._startT = t
        self._t = t

    def _getLabel(self):
        return "logreturn" + getLabel(self._source)

    def _remove(self, t, x, params):
        print "remove", t, self._startT, self._t
        if self._t == self._startT + 1:
            self._x += log(x)
            self._startT = self._t
        self.fire(self)

from _computed import OnEveryDt

def RollingVolatility(source, timeframe):
    return OnEveryDt(1, ops.sqrt(OnEveryDt(1, MovingVariance(RollingLogReturns(source), timeframe))*ops.constant(timeframe)))

from collections import OrderedDict
