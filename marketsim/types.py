from marketsim.Side import Tag as Side
from marketsim.constraints import *
from marketsim.meta import *
from marketsim import event

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative

class IOrderBook(object):
    pass

class IOrderQueue(object):
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

class Factory(object):
    
    def __init__(self, name, tmpl):
        self._types = {}
        self._name = name
        self._tmpl = tmpl
        
    def __getitem__(self, key):
        if key not in self._types:
            T = key.__name__
            exec self._tmpl % {'T': T, 'Name' : self._name} in globals()
            self._types[key] = eval(self._name + '_' + T)
        return self._types[key]
    
IFunction = Factory('IFunction', """
class %(Name)s_%(T)s(object):
    
    _types = [function((), %(T)s)]
""")
        
class IDifferentiable(object):
    pass

IObservable = Factory('IObservable', """
class %(Name)s_%(T)s(event.IEvent, IFunction[%(T)s]):
    pass
""")

Observable = Factory('Observable', '''
class %(Name)s_%(T)s(IObservable[%(T)s], event.Conditional):
    pass
''')

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
