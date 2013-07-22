import marketsim
from marketsim import Side
from marketsim.constraints import *
from marketsim.meta import *
from marketsim import event
from marketsim.event import IEvent

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative

class IOrderBook(object):
    pass

class IOrderQueue(object):
    pass

class IOrderFactory(object):
    # should provide method __call__(self) -> Order
    pass 

class ISidePrice_IOrderFactory(object):
    # (Side,Price) -> IOrderFactory
    pass

class ISide_IOrderFactory(object):
    # Side -> IOrderFactory
    pass

class ISignedVolume_IOrderFactory(object):
    # SignedVolume -> IOrderFactory
    pass

class IStrategy(object):
    pass

class ISingleAssetStrategy(IStrategy):
    T = type(None) # just to please wrap.generator
    pass

class IMultiAssetStrategy(IStrategy):
    pass

class ITrader(object):
    pass

class ISingleAssetTrader(ITrader):
    pass

class ICandleStick(object):
    pass

class IVolumeLevels(object):
    pass

class Factory(object):
    
    def __init__(self, name, tmpl, g = None):
        self._types = {}
        self._name = name
        self._tmpl = tmpl
        self._globals = globals() if g is None else g
        
    def __setitem__(self, key, obj):
        assert key not in self._types
        self._types[key] = obj
        
    def __getitem__(self, key):
        if key not in self._types:
            #print key
            M = key.__module__ + '.' if key.__module__ != '__builtin__' else ''
            N = key.__name__
            T = M + N
            tmp= "class " + self._name + '_' + N + \
                 self._tmpl % {'T': T, 'Name' : self._name} +\
                 "pass"
            #print tmp
            exec tmp in self._globals
            self._types[key] = eval(self._name + '_' + N, self._globals)
        return self._types[key]
    
IFunction = Factory('IFunction', """(object):
    _types = [function((), %(T)s)]
""")
        
class IDifferentiable(object):
    pass

class IObservable_object(object):
    pass

IObservable = Factory('IObservable', """(IEvent, IFunction[%(T)s], IObservable_object):""")

IObservable[object] = IObservable_object

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
