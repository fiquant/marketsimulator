from _average import ewma
import rnd
from marketsim import types, registry

class constant(object):
    
    def __init__(self, value=100.):
        self.value = value
        
    def reset(self):
        pass
        
    _properties = {'value' : float}
    _types = [types.function(args=(), rv=float)]
    
    def _casts_to(self, dst):
        if type(dst) is types.function:
            rv = dst.rv
            return rv is float or\
                (type(rv) is types.greater_or_equal and rv._bound <= self.value) or\
                (type(rv) is types.greater_than and rv._bound < self.value) or\
                (type(rv) is types.less_or_equal and rv._bound >= self.value) or\
                (type(rv) is types.less_than and rv._bound > self.value)
        return False 
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"

registry.insert(constant(), "Constant")

class product(object):
    
    def __init__(self, LeftHandSide, RightHandSide):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        return self.LeftHandSide() * self.RightHandSide()
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "*" + repr(self.RightHandSide)
    
registry.insert(product(constant(1), constant(1)), alias="*")
    
class sum(object):
    
    def __init__(self, LeftHandSide, RightHandSide):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        return self.LeftHandSide() + self.RightHandSide()
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "+" + repr(self.RightHandSide)
    
registry.insert(sum(constant(1), constant(1)), alias="+")

class div(object):
    
    def __init__(self, LeftHandSide, RightHandSide):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        return self.LeftHandSide() / self.RightHandSide()
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "/" + repr(self.RightHandSide)
    
registry.insert(div(constant(1), constant(1)), alias="/")
    
class sub(object):
    
    def __init__(self, LeftHandSide, RightHandSide):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        return self.LeftHandSide() + self.RightHandSide()
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "-" + repr(self.RightHandSide)
    
registry.insert(sub(constant(1), constant(1)), alias="-")

    