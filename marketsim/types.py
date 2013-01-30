import collections
import inspect
from marketsim import Side
from marketsim.order._base import Base as Order
from marketsim.orderbook._base import BookBase as OrderBook
from marketsim.constraints import *
from marketsim.trader import SingleAsset as SingleAssetTrader

Price = non_negative
Volume = non_negative
TimeInterval = non_negative

def casts_to(src, dst):
    if src == dst: return True
    if dst == float and src == int: return True
    if dst == int and src == bool: return True
    if inspect.isclass(src) and inspect.isclass(dst):
        if issubclass(src, dst):
            return True
    if '_casts_to' in dir(src):
        return src._casts_to(dst)
    return False

class function(collections.namedtuple("function", ["args", "rv"])):
    
    def _casts_to(self, dst):
        if dst is None:
            return True
        if type(dst) is function:
            for i in range(len(self.args)):
                if i >= len(dst.args):
                    return False
                if not(casts_to(dst.args[i], self.args[i])):
                    return False
            return casts_to(self.rv, dst.rv)
        return False
    
def sig(args, rv, label):
    def inner(f):
        f._types = [function(args, rv)]
        f._casts_to = f._types[0]._casts_to
        f.label = label
        return f
    return inner

class UpdatableValue(object):    
    """
    Class implementing UpdatableValue concept should obey the following interface
    @property 
    def value(self) # Returns average value at the last update point 
    def at(self, t) # Returns value of the average at some time point t >= last update time
    def derivativeAt(self, t) # Returns derivative of the average at some time point t >= last update time
    def update(self, time, value)# Adds point (time, value) to calculate the average
    """
    pass
