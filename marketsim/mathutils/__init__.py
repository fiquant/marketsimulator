from _average import ewma
import rnd

class constant(object):
    
    def __init__(self, x):
        self._value = x
        
    def __call__(self, *args, **kwargs):
        return self._value
    
    def __repr__(self):
        return "constant("+self._value+")"
