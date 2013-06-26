from marketsim import meta, types, registry

from marketsim.types import IFunction

class FloatFunction(IFunction[float]):
    
    def __add__(self, other):
        return sum(self, other)
    
    def __sub__(self, other):
        return sub(self, other)
    
    def __mul__(self, other):
        return product(self, other)
    
    def __div__(self, other):
        return div(self, other)
    
class IntFunction():
    pass

IntFunction._types = [types.function((), int)]

Function = { float : FloatFunction, 
             int   : IntFunction }

@registry.expose(['Constant'])
class constant(Function[float]):
    """ Constant function returning **value**.
    """
    
    def __init__(self, value=100.):
        self.value = value
        
    _properties = {'value' : float}
    
    def _casts_to(self, dst):
        if type(dst) is meta.function:
            rv = dst.rv
            return rv is float or\
                (type(rv) is meta.greater_or_equal and rv._bound <= self.value) or\
                (type(rv) is meta.greater_than and rv._bound < self.value) or\
                (type(rv) is meta.less_or_equal and rv._bound >= self.value) or\
                (type(rv) is meta.less_than and rv._bound > self.value)
        return False 
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    @property
    def label(self):
        return "C=" + str(self.value)
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"

@registry.expose(['Arithmetic', 'negate'])
class negate(Function[float]):
    """ Function returning product of the operands
    """
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        x = self.arg()
        return -x if x is not None else None
    
    def __repr__(self):
        return "-" + repr(self.arg)

@registry.expose(['Arithmetic', 'identity'])
class identity(Function[float]):
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        return self.arg()
    
    def __repr__(self):
        return "id(" + repr(self.arg) + ")"

@registry.expose(['Arithmetic', '*'])
class product(Function[float]):
    """ Function returning product of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1.), RightHandSide=constant(1.)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : IFunction[float], 
                    "RightHandSide" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs * rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.LeftHandSide)+ "*" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '+'])    
class sum(Function[float]):
    """ Function returning sum of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1), RightHandSide=constant(1)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : IFunction[float], 
                    "RightHandSide" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs + rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.LeftHandSide)+ "+" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '/'])
class div(Function[float]):
    """ Function returning division of the operands
    """
    
    def __init__(self, LeftHandSide=constant(1.), RightHandSide=constant(1.)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : IFunction[float], 
                    "RightHandSide" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs / rhs if lhs is not None and rhs is not None and rhs != 0 else None
    
    def __repr__(self):
        return repr(self.LeftHandSide)+ "/" + repr(self.RightHandSide)

@registry.expose(['Arithmetic', '-'])    
class sub(Function[float]):
    """ Function substructing the right operand from the left one
    """
    
    def __init__(self, LeftHandSide=constant(1), RightHandSide=constant(1)):
        self.LeftHandSide = LeftHandSide
        self.RightHandSide = RightHandSide
        
    _properties = { "LeftHandSide" : IFunction[float], 
                    "RightHandSide" : IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs - rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.LeftHandSide)+ "-" + repr(self.RightHandSide)

    