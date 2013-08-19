from marketsim import types, _, ops, getLabel, event, _, bind
import fold
import pandas as pd
import numpy as np
class MetaStore(type):
    def __getitem__(cls, val):
        return cls.getitem(val)

from datetime import datetime

class DataStore:
    """ 
    Class for storing common data
    """
    __metaclass__ = MetaStore
    sources = {}
    events = {}
    data = {}
    
    @staticmethod 
    def addSource(source, label=None):
        label = getLabel(source) if label is None else label
        DataStore.sources[label] = source
        DataStore.events[label] = event.subscribe(source, _(DataStore, label).update, DataStore)
        DataStore.data[label] = pd.TimeSeries()
    
    @staticmethod
    def update(label, timer):

        # t = pd.Timestamp(datetime.fromtimestamp(timer._scheduler.currentTime))
        # pd.SparseTimeSeries()
        x = pd.TimeSeries([DataStore.sources[label]()], [timer._scheduler.currentTime])
        DataStore.data[label] = DataStore.data[label].append(x)
    
    @staticmethod
    def getitem(key):
        return DataStore.data[key]
    
    @staticmethod
    def lastUpdate(key):
        # TODO: convert index to float?
        return DataStore.data[key].index[-1:]
        
        

class ObservableHistory(fold.Last, ops.Observable[float]):
    """
    Updates and stores every value from an event source 
    """
    
    def __init__(self, source):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        self._data = pd.Series()
        
    def update(self, t, x):
        self._data = self._data.append(pd.Series([x], [t]), verify_integrity = False)
        
    def at(self, t):
        return self._data.get(t, None)
    
    def __getitem__(self, key):
        return self._data.__getitem__(key)
    
    def _getLabel(self):
        return self.source.label
    
class RollingApply(ObservableHistory):
    def __init__(self, source, window, func = pd.Series.mean):
        ObservableHistory.__init__(self, source)
        self._window = window
        self._slice = slice(-window, None, None)
        self._func = func
        
    def process(self):
        return self._func(self.source[self._slice])
        
    def update(self, t, x):
        # TODO: check if we have already calculated the last value
        new = self.process()
        # print t, new
        self._data = self._data.append(pd.Series([new], [t]))
    
    def at(self, t):
        self.update(t, None)
        return ObservableHistory.at(self, t)

    @property
    def label(self):
        return self._func.__name__ + "{%s}" % self.source.label

    def _getLabel(self):
        return self.label