from marketsim import meta, Side, types, registry

class FloatFunction(types.IFunction[float]):
    
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

class ConstantSide(object):
    """ Constant function always returning given *side*. 
    
    Note: We need it since our type system doesn't support for the moment generic
    Constant: () -> 'a
    """
    
    def __init__(self, side = Side.Sell):
        self.side = side
        self._alias = ['Constant side']
        
    _properties = { 'side' : Side }
    _types = [ meta.function((), Side) ]
        
    def __call__(self):
        return self.side
    
class Condition_Impl(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

condition_tmpl = """
class Condition%(T)s(Condition_Impl):

    def __init__(self, cond, ifpart, elsepart):
        Condition_Impl.__init__(self, cond, ifpart, elsepart)
        self._alias = ['Condition[%(T)s]']
        
    _types = [meta.function((), %(T)s)]
        
    _properties = [('cond', meta.function((), bool)), 
                   ('ifpart', meta.function((), %(T)s)), 
                   ('elsepart', meta.function((), %(T)s))]
"""  

for t in ['Side', 'float']:
    exec condition_tmpl % { 'T' : t }   
    
class NotNoneFloat(Function[float]):
    
    def __init__(self, source, ifnone):
        self.source = source
        self.ifnone = ifnone
    
    _properties = { 'source' : types.IFunction[float], 
                    'ifnone' : types.IFunction[float]}
        
    def __call__(self):
        v = self.source()
        return v if v is not None else self.ifnone()
    
class less_float(Function[float]):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    _types = [meta.function((), bool)]
    
    _properties = [('lhs', types.IFunction[float]), 
                   ('rhs', types.IFunction[float])]
    
    def __call__(self):
        return self.lhs() < self.rhs()
    
class none_side(object):
    
    def __call__(self):
        return None
    
    _types = [meta.function((), Side)]
    
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
        
    _properties = { "arg" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        x = self.arg()
        return -x if x is not None else None
    
    def __repr__(self):
        return "-" + repr(self.arg)

@registry.expose(['Arithmetic', 'identity'])
class identity(Function[float]):
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : types.IFunction[float] }
    
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
        
    _properties = { "LeftHandSide" : types.IFunction[float], 
                    "RightHandSide" : types.IFunction[float] }
    
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
        
    _properties = { "LeftHandSide" : types.IFunction[float], 
                    "RightHandSide" : types.IFunction[float] }
    
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
        
    _properties = { "LeftHandSide" : types.IFunction[float], 
                    "RightHandSide" : types.IFunction[float] }
    
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
        
    _properties = { "LeftHandSide" : types.IFunction[float], 
                    "RightHandSide" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        lhs = self.LeftHandSide()
        rhs = self.RightHandSide()
        return lhs - rhs if lhs is not None and rhs is not None else None
    
    def __repr__(self):
        return repr(self.LeftHandSide)+ "-" + repr(self.RightHandSide)

   
