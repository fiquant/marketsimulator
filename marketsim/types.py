from marketsim.Side import Tag as Side
from marketsim.constraints import *
from marketsim.meta import *
from marketsim import event

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative

class IOrderBook(object):
    pass

class IStrategy(object):
    pass

class ISingleAssetStrategy(IStrategy):
    pass

class IMultiAssetStrategy(IStrategy):
    pass

class ITrader(object):
    pass

class ISingleAssetTrader(ITrader):
    pass

class IObservable(event.Conditional):
    def __init__(self):
        event.Conditional.__init__(self, self)

IObservable._types = [function((), float)]

class IOrder(object):
    pass

class IGraph(object):
    pass

class ITimeSerie(object):
    pass

class IUpdatableValue(object):    
    """
    Class implementing UpdatableValue concept should obey the following interface
    @property 
    def value(self) # Returns average value at the last update point 
    def at(self, t) # Returns value of the average at some time point t >= last update time
    def derivativeAt(self, t) # Returns derivative of the average at some time point t >= last update time
    def update(self, time, value)# Adds point (time, value) to calculate the average
    """
    pass
