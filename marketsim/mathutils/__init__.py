from _average import ewma
import rnd

class constant(object):
    
    def __init__(self, x):
        self.value = x
        
    _properties = ['value']
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"
