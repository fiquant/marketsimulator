from marketsim.Side import Tag as Side
from marketsim.constraints import *
from marketsim.meta import *
from marketsim import Event

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative

class IOrderBook(object):
    pass

IOrderBook._types = [IOrderBook]

class IStrategy(object):
    pass

IStrategy._types = [IStrategy]

class ISingleAssetTrader(object):
    pass

ISingleAssetTrader._types = [ISingleAssetTrader]

class IObservable(object):
    pass

IObservable._types = [IObservable, function((), float), Event]

class IOrder(object):
    pass

IOrder._types = [IOrder]

class IGraph(object):
    pass

IGraph._types =  [IGraph]

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

IUpdatableValue._types = [IUpdatableValue]
