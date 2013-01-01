from _average import ewma
import rnd
from marketsim import types

class constant(object):
    
    def __init__(self, value=100.):
        self.value = value
        
    _properties = {'value' : float}
    _types = [types.function(args=(), rv=float)]
    
    def _casts_to(self, dst):
        if type(dst) is types.function:
            rv = dst.rv
            return dst is float or\
                (type(rv) is types.greater_or_equal and rv._bound <= self.value) or\
                (type(rv) is types.greater_than and rv._bound < self.value) or\
                (type(rv) is types.less_or_equal and rv._bound >= self.value) or\
                (type(rv) is types.less_than and rv._bound > self.value)
        return False 
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"
