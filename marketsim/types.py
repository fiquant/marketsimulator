import marketsim
from marketsim import Side, bind
from marketsim.constraints import *
from marketsim.meta import *

Price = float #non_negative
Volume = float #non_negative
TimeInterval = float #non_negative

class IEvent(object):
    pass

class IOrderGenerator(object):
    # should provide method __call__(self) -> Order
    pass 

# creates orders that can be cancelled
class IPersistentOrderGenerator(IOrderGenerator):
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
            def correct(key):
                if key.__name__ in self._globals:
                    M = ""
                else:
                    M = key.__module__ + '.' if key.__module__ not in ['__builtin__'] else ''
                N = key.__name__
                return M + N, N
            if type(key) is not tuple:
                T,N = correct(key)
                R = ""
            else:
                T,N = correct(key[0])
                R = ""
                for e in key[1:]:
                    t, n = correct(e)
                    N += '_' + n
                    if R != "": R += ','
                    R += t
                if len(key) == 2:
                    R += ","
            tmp= "class " + self._name + '_' + N + \
                 self._tmpl % {'T': T, 'R' : R, 'Name' : self._name} +\
                 "pass"
            #print tmp
            exec tmp in self._globals
            self._types[key] = eval(self._name + '_' + N, self._globals)
        return self._types[key]

class SidePriceVolume(object):
    pass

class SideVolume(object):
    pass

class PriceVolume(object):
    pass

class SignedVolume(object):
    pass

class SidePrice(object):
    pass

class SideBudget(object):
    pass


IFunction = Factory('IFunction', """(object):
    _types = [function((%(R)s), %(T)s)]
""")

Construct = Factory('Construct', """(bind.Construct, IFunction[%(T)s, %(R)s]):""")
        
class IOrder(object):
    pass

class IRequest(object):
    pass

class IOrderBook(object):
    pass

class IOrderQueue(object):
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

class IAccount(object):
    # PnL
    # amount
    pass

class ISingleAssetTrader(ITrader, IAccount):
    pass

class ICandleStick(object):
    pass

class IVolumeLevels(object):
    pass

    
class IDifferentiable(object):
    pass

class IObservable_object(object):
    pass

IObservable = Factory('IObservable', """(IEvent, IFunction[%(T)s], IObservable_object):""")

IObservable[object] = IObservable_object

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
