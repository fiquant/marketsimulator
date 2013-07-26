from marketsim import types, _, ops, getLabel
import fold
from _stddev import StdDevRolling, MovingVariance



class RollingEvent(fold.Last, ops.Observable[float]):
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
        # print "at", t, self._t, self._startT, self._x
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

from itertools import takewhile, imap
from collections import OrderedDict

class Rolling(fold.Last, ops.Observable[float]):
    def __init__(self, source, window, wait=True):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self.window = window
        self.wait = wait  # wait for enough values to calculate
        self.values = OrderedDict()
        self.reset()

    _properties = {'window': float}

    def _getLabel(self):
        return "Rolling"

    def reset(self):
        pass

    def at(self, t):
        self.purge(t)
        if t > self.window and self.values:
            return self.actualize(t)
        else:
            return None

    def actualize(self, t):
        return None

    def update(self, t, x):
        self.purge(t)
        if x is not None:
            self.add(t, x)
        # self.fire(self)

    def add(self, t, x):
        pass

    @property
    def start(self):
        return next(iter(self.values)) if self.values else None

    @property
    def end(self):
        return next(reversed(self.values)) if self.values else None

    def purge(self, t=None):
        t = self._scheduler.currentTime if t is None else t
        last_t = t - self.window
        map(self.remove, takewhile(lambda t: t < last_t, iter(self.values)))

    def remove(self, time):
        del self.values[time]


class RollingAvg(Rolling):

    def reset(self):
        self._sum = 0

    def actualize(self, t):
        startT, endT = self.start, self.end
        T = t - self.window
        sum = self.values[startT] * (startT - T) \
              + self._sum \
              + self.values[endT] * (t - endT)
        return sum / self.window

    def add(self, t, x):
        if self.values:
            endT = self.end
            dS = self.values[endT] * (t - endT)
            # we replace the value endX by dS
            self.values[endT] = dS
            self._sum += dS
        self.values[t] = x

    def remove(self, t):
        if len(self.values) > 1:
            # the value at t is dS
            self._sum -= self.values.pop(t)
        else:
            self._sum = 0
            self.values.pop(t)




from math import log


class RollingLogReturns(RollingEvent):

    def __init__(self, source, freq=1):
        RollingEvent.__init__(self, source, window=freq*2)  # window = 2 because we look at the two last values
        self.freq = freq

    def _add(self, t, x):
        # print "add", t, self._startT, self._t
        if t - self._startT == self.freq and self._x:
            self._x = log(x) - self._x
        else:
            self._x = log(x)
            self._startT = t
        self._t = t

    def _getLabel(self):
        return "logreturn" + getLabel(self._source)

    def _remove(self, t, x, params):
        # print "remove", t, self._startT, self._t
        if self._t == self._startT + 1:
            self._x += log(x)
            self._startT = self._t
        self.fire(self)

from _computed import OnEveryDt

def RollingVolatility(source, timeframe):
    return ops.Sqrt(MovingVariance(RollingLogReturns(source), timeframe)*timeframe)

