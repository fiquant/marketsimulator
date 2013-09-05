from marketsim import getLabel, event, _
from collections import OrderedDict, defaultdict


class ObservableDict(OrderedDict):
    def __init__(self, source):
        super(ObservableDict, self).__init__(self)
        event.subscribe(source, _(self).update, self)
        self._source = source

    def bind(self, context):
        self._scheduler = context.world

    def update(self, dummy):
        value = self._source()
        if value is not None:
            self[self._scheduler.now] = self._source()



import pandas as pd

class BufferedSeries(ObservableDict):
    def __init__(self, source):
        super(BufferedSeries, self).__init__(source)
        self._data = pd.TimeSeries()

    def __call__(self):
        if self:
            self._data = self._data.append(
                pd.TimeSeries(self.values(), self.keys()))
            self.clear()
        return self._data


