from marketsim import meta, Side, types, registry

class FloatFunction(types.IFunction[float]):
    
    T = float
    
    def __add__(self, other):
        return Sum(self, other)
    
    def __sub__(self, other):
        return Sub(self, other)
    
    def __mul__(self, other):
        return Product(self, other)
    
    def __div__(self, other):
        return Div(self, other)
    
    def __lt__(self, other):
        return less(self, other)
    
    def __gt__(self, other):
        return greater(self, other)
    
class IntFunction(object):
    T = int
    

class BoolFunction(object):
    T = bool
    

class SideFunction(object):
    T = Side
    
    

IntFunction._types = [types.function((), int)]
BoolFunction._types = [types.function((), bool)]
SideFunction._types = [types.function((), Side)]

Function = { float : FloatFunction, 
             int   : IntFunction, 
             bool  : BoolFunction,
             Side  : SideFunction }

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
                   
Condition[%(T)s] = Condition%(T)s
"""  

Condition = {}

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
    
class _BinaryOp_Base(object):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
class _Conditional_Base(_BinaryOp_Base, Function[bool]):
    
    def __getitem__(self, (ifpart, elsepart)):
        return Condition[self.BranchType](self, ifpart, elsepart)
        
# ---------------------------------------------------- Greater

class _Greater_Impl(_Conditional_Base):
    
    def __call__(self):
        return self.lhs() > self.rhs()

_greater_tmpl = """        
class Greater_%(T)s(_Greater_Impl):

    BranchType = %(T)s
    
    _properties = [('lhs', types.IFunction[%(T)s]), 
                   ('rhs', types.IFunction[%(T)s])]

Greater[%(T)s] = Greater_%(T)s
"""

Greater = {}

for T in ["float"]:
    exec _greater_tmpl % { 'T' : T }

def greater(lhs, rhs):
    if 'T' in dir(lhs):
        if 'T' in dir(rhs):
            assert lhs.T == rhs.T
        return Greater[lhs.T](lhs, rhs)
    if 'T' in dir(rhs):
        return Greater[rhs.T](lhs, rhs)
    raise "Cannot inference T for greater(" + repr(lhs) + ',' + repr(rhs) + ')'
    
# ---------------------------------------------------- Less

class _Less_Impl(_Conditional_Base):
    
    def __call__(self):
        return self.lhs() < self.rhs()

_less_tmpl = """        
class Less_%(T)s(_Less_Impl):
    
    BranchType = %(T)s
    
    _properties = [('lhs', types.IFunction[%(T)s]), 
                   ('rhs', types.IFunction[%(T)s])]

Less[%(T)s] = Less_%(T)s
"""

Less = {}

for T in ["float"]:
    exec _less_tmpl % { 'T' : T }

def less(lhs, rhs):
    if 'T' in dir(lhs):
        if 'T' in dir(rhs):
            assert lhs.T == rhs.T
        return Less[lhs.T](lhs, rhs)
    if 'T' in dir(rhs):
        return Less[rhs.T](lhs, rhs)
    raise "Cannot inference T for less(" + repr(lhs) + ',' + repr(rhs) + ')'
    
# ---------------------------------------------------- Constant

class _None_Impl(object):
    
    def __call__(self):
        return None

_none_tmpl = """
class _None_Side(_None_Impl, Function[%(T)s]):
    pass
    
_None[%(T)s] = _None_%(T)s
"""

_None = {}

for T in ["Side"]:
    exec _none_tmpl % { 'T' : T }
    
# ---------------------------------------------------- Constant

class _Constant_Impl(object):
    """ Constant function returning **value**.
    """
    
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

_constant_tmpl = """    
@registry.expose(['Constant[%(T)s]'])
class Constant_%(T)s(_Constant_Impl, Function[%(T)s]):
    \""" Constant function returning **value**.
    \"""
    
    def __init__(self, value=%(defvalue)s):
        self.value = value
        
    _properties = {'value' : %(T)s}
    
Constant[%(T)s] = Constant_%(T)s
"""

Constant = {}
for T,defvalue in {'float'  : '100.', 
                   'int'    : '100', 
                   'Side'   : 'Side.Sell'  
                  }.iteritems():
    exec _constant_tmpl % { 'T' : T, 'defvalue' : defvalue }

def constant(x):
    return Constant_float(x) if type(x) is float\
        else Constant_float(x) if type(x) is int\
        else Constant_Side(x) if x is Side.Sell or x is Side.Buy\
        else None    


@registry.expose(['Arithmetic', 'negate'])
class negate(Function[float]):
    """ Function returning Product of the operands
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
class Product(Function[float]):
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
class Sum(Function[float]):
    """ Function returning Sum of the operands
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
class Div(Function[float]):
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
class Sub(Function[float]):
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

   
