from marketsim import types, _, ops, getLabel, event, _
import pandas as pd
import numpy as np

class MetaStore(type):
    def __getitem__(cls, val):
        return cls.getitem(val)

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
    def update(label, source):
        value = DataStore.sources[label]()
        if value is not None:
            x = pd.TimeSeries([value], [source._scheduler.now])
            DataStore.data[label] = DataStore.data[label].append(x)

    @staticmethod
    def getitem(key):
        return DataStore.data[key]
    
    @staticmethod
    def lastUpdate(key):
        # TODO: convert index to float?
        return DataStore.data[key].index[-1:]