from _average import ewma
import rnd
from marketsim import types

class constant(object):
    
    def __init__(self, value=100.):
        self.value = value
        
    _properties = {'value' : float}
    _types = [types.function(args=(), rv=float)]
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"
