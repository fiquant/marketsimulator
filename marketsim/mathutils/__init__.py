from _average import ewma
import rnd

class constant(object):
    
    def __init__(self, value=100.):
        self.value = value
        
    _properties = {'value' : float}
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"
