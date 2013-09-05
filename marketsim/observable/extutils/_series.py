from marketsim import types, _, ops, getLabel, event, _, bind
from marketsim.observable import fold
import pandas as pd
import numpy as np

class ObservableHistory(fold.Last, ops.Observable[float]):
    """
    Updates and stores every value from an event source
    """
    # TODO: add buffer

    def __init__(self, source):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self._data = pd.TimeSeries()

    def update(self, t, x):
        if x is not None:
            t = self._scheduler.now
            self._data = self._data.append(pd.TimeSeries([x], [t]), verify_integrity = False)
            self.fire(self)

    def at(self, t):
        t = self._scheduler.now
        return self._data.get(t, None)

    def __getattr__(self, item):
        return getattr(self._data, item)

    def _getLabel(self):
        return self.source.label


class RollingApply(ObservableHistory):
    # TODO: pass all args to func
    def __init__(self, source, window, func=pd.Series.mean):
        if not isinstance(source, ObservableHistory):
            source = ObservableHistory(source)
        ObservableHistory.__init__(self, source)
        self._window = window
        self._slice = slice(-window, None, None)
        self._func = func

    def process(self):
        return self._func(self.source[self._slice])

    def update(self, t, x):
        # TODO: check if we have already calculated the last value
        new = self.process()
        ObservableHistory.update(self, t, new)

