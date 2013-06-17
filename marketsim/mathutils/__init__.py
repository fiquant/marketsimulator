from _average import ewma
from _rsi import rsi
import rnd
from marketsim import types, registry

@registry.expose(['Constant'])
class constant(object):
    """ Constant function returning **value**.
    """
    
    def __init__(self, value=100.):
        self.value = value
        
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
    
    @property
    def label(self):
        return "C=" + str(self.value)
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"

@registry.expose(['Arithmetic', '*'])
class product(object):
    """ Function returning product of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1.), RightHandSide=constant(1.)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs * rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "*" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '+'])    
class sum(object):
    """ Function returning sum of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1), RightHandSide=constant(1)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs + rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "+" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '/'])
class div(object):
    """ Function returning division of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1.), RightHandSide=constant(1.)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs / rhs if lhs is not None and rhs is not None and rhs != 0 else None
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "/" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '-'])    
class sub(object):
    """ Function substructing the right operand from the left one
    """
    
    def __init__(self, LeftHandSide=constant(1), RightHandSide=constant(1)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : types.function((), float), 
                    "RightHandSide" : types.function((), float) }
    
    _types = [types.function((), float)]
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs - rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.RightHandSide)+ "-" + repr(self.RightHandSide)

    