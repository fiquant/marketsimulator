import collections
from marketsim import Side
from marketsim.order import _base
from marketsim.constraints import *

Order = _base.Base
Price = float   # non_negative
Volume = float  # non_negative
TimeInterval = float # non_negative

def casts_to(src, dst):
    if src == dst: return True
    if dst == float and src == int: return True
    if dst == int and src == bool: return True
    return False

class function(collections.namedtuple("function", ["args", "rv"])):
    
    def _accepts(self, typ):
        if 'args' in dir(typ):
            for i in range(len(self.args)):
                if i >= len(typ.args):
                    return True
                if not casts_to(self.args[i], typ.args[i]):  # TODO: we should check here covariance
                    return False
            return casts_to(typ.rv, self.rv) # TODO: we should check here contrevariance
            
    def __call__(self, obj):
        assert '_types' in dir(obj)
        for typ in obj._types:
            if self._accepts(typ):
                return obj
        assert False, "cannot convert " + str(obj) + " to " + str(self)
        
def sig(args, rv):
    def inner(f):
        f._types = [function(args, rv)]
        return f
    return inner
    