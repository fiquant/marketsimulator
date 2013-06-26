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

class IScalarFunction(object):
    pass

class IFloatFunction(IScalarFunction):
    pass

IFloatFunction._types = [function((), float)]

IFunction = { float : IFloatFunction }

class IObservable(event.IEvent, IFunction[float]):
    pass

class Observable(IObservable, event.Conditional):
    pass

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
