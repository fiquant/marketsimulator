from marketsim import meta, Side, types, registry, getLabel, event, _

import math, inspect 

def convert(other):
    if type(other) in [int, float]:
        other = constant(other)
    return other

class FloatFunction(types.IFunction[float]):
    
    T = float
    
    def __add__(self, other):
        return sum(self, convert(other))
    
    def __sub__(self, other):
        return sub(self, convert(other))
    
    def __mul__(self, other):
        return product(self, convert(other))
    
    def __div__(self, other):
        return div(self, convert(other))
    
    def __lt__(self, other):
        return less(self, convert(other))
    
    def __gt__(self, other):
        return greater(self, convert(other))
    
    def __eq__(self, other):
        return equal(self, convert(other))
    
    def __ne__(self, other):
        return notequal(self, convert(other))
    
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

binary_base_tmpl = """
class _BinaryOp_%(T)s(object):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    _properties = [('lhs', meta.function((), %(T)s)), 
                   ('rhs', meta.function((), %(T)s))]
       
    @property
    def attributes(self):
        return {}

BinaryOp[%(T)s] = _BinaryOp_%(T)s
"""

BinaryOp = {}

for T in ['float']:
    exec binary_base_tmpl % { 'T': T }
    
#---------------------------------------------- Condition 
        
class Condition_Impl(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    def __call__(self):
        c = self.cond()
        return None if c is None else self.ifpart() if c else self.elsepart()

condition_tmpl = """
class Condition%(T)s(Condition_Impl, Function[%(T)s]):

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

class _Conditional_Base(Function[bool]):
    
    def __getitem__(self, (ifpart, elsepart)):
        return Condition[self.BranchType](self, ifpart, elsepart)

# ---------------------------------------------------- Equal

class _Equal_Impl(_Conditional_Base):
    
    def __call__(self):
        lhs = self.lhs()
        rhs = self.rhs()
        return self.lhs() == self.rhs()

_equal_tmpl = """        
class Equal_%(T)s(_BinaryOp_%(T)s, _Equal_Impl):

    BranchType = %(T)s

Equal[%(T)s] = Equal_%(T)s
"""

Equal = {}

for T in ["float"]:
    exec _equal_tmpl % { 'T' : T }

def equal(lhs, rhs):
    if 'T' in dir(lhs):
        if 'T' in dir(rhs):
            assert lhs.T == rhs.T
        return Equal[lhs.T](lhs, rhs)
    if 'T' in dir(rhs):
        return Equal[rhs.T](lhs, rhs)
    raise "Cannot inference T for equal(" + repr(lhs) + ',' + repr(rhs) + ')'
        
# ---------------------------------------------------- NotEqual

class _NotEqual_Impl(_Conditional_Base):
    
    def __call__(self):
        return self.lhs() != self.rhs()

_notequal_tmpl = """        
class NotEqual_%(T)s(_BinaryOp_%(T)s, _NotEqual_Impl):

    BranchType = %(T)s

NotEqual[%(T)s] = NotEqual_%(T)s
"""

NotEqual = {}

for T in ["float"]:
    exec _notequal_tmpl % { 'T' : T }

def notequal(lhs, rhs):
    if 'T' in dir(lhs):
        if 'T' in dir(rhs):
            assert lhs.T == rhs.T
        return NotEqual[lhs.T](lhs, rhs)
    if 'T' in dir(rhs):
        return NotEqual[rhs.T](lhs, rhs)
    raise "Cannot inference T for notequal(" + repr(lhs) + ',' + repr(rhs) + ')'
        
# ---------------------------------------------------- Greater

class _Greater_Impl(_Conditional_Base):
    
    def __call__(self):
        return self.lhs() > self.rhs()

_greater_tmpl = """        
class Greater_%(T)s(_BinaryOp_%(T)s, _Greater_Impl):

    BranchType = %(T)s

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
class Less_%(T)s(_BinaryOp_%(T)s, _Less_Impl):
    
    BranchType = %(T)s

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
class _None_%(T)s(_None_Impl, Function[%(T)s]):
    pass
    
_None[%(T)s] = _None_%(T)s
"""

_None = {}

for T in ["Side", "float"]:
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
        return str(self.value)
    
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
    
@registry.expose(['Arithmetic', 'sqrt'])
class sqrt(Function[float]):
    """ Function returning square root of the operand
    """
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        x = self.arg()
        return math.sqrt(x) if x is not None else None
    
    @property
    def label(self):
        return "\sqrt{" + self.arg.label + "}"
    
    def __repr__(self):
        return "sqrt(" + repr(self.arg) + ")"



@registry.expose(['Arithmetic', 'identity'])
class identity(Function[float]):
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        return self.arg()
    
    def __repr__(self):
        return "id(" + repr(self.arg) + ")"
    
def create_function_or_observable(FuncType, ObsType):
    def inner(lhs, rhs):
        left = types.IObservable[float] in inspect.getmro(type(lhs))
        right = types.IObservable[float] in inspect.getmro(type(lhs))
        if left or right:
            x = ObsType(lhs, rhs)
            if left:
                event.subscribe(lhs, _(x).fire, x)
            if right:
                event.subscribe(rhs, _(x).fire, x)
            return x
        return FuncType(lhs, rhs)
    return inner

@registry.expose(['Arithmetic', '*'], args = (constant(1.), constant(1.)))
class Product(BinaryOp[float], Function[float]):
    """ Function returning product of the operands
    """
    
    def __call__(self, *args, **kwargs):
        lhs = self.lhs()
        rhs = self.rhs()
        return lhs * rhs if lhs is not None and rhs is not None else None
    
    @property
    def label(self):
        return self.lhs.label + ' * ' + self.rhs.label
    
    def __repr__(self):
        return repr(self.lhs)+ "*" + repr(self.rhs)

class ProductEvent(Product, types.Observable):
    
    def __init__(self, lhs, rhs):
        Product.__init__(self, lhs, rhs)
        types.Observable.__init__(self)
            
product = create_function_or_observable(Product, ProductEvent)
    
class Sqr(types.Observable):
    
    def __init__(self, source):
        self._source = source
        types.Observable.__init__(self)
        self._event = event.subscribe(source, _(self).fire, self)
        
    _properties = { 'source' : types.Observable }
    
    @property
    def source(self):
        return self._source
    
    def __call__(self):
        r = self._source()
        return r*r if r is not None else None

@registry.expose(['Arithmetic', '+'], args = (constant(1.), constant(1.)))    
class Sum(BinaryOp[float], Function[float]):
    """ Function returning Sum of the operands
    """
    
    def __call__(self, *args, **kwargs):
        lhs = self.lhs()
        rhs = self.rhs()
        return lhs + rhs if lhs is not None and rhs is not None else None
    
    @property
    def label(self):
        return self.lhs.label + ' + ' + self.rhs.label
    
    def __repr__(self):
        return repr(self.lhs)+ "+" + repr(self.rhs)
    
class SumEvent(Sum, types.Observable):
    
    def __init__(self, lhs, rhs):
        Sum.__init__(self, lhs, rhs)
        types.Observable.__init__(self)
            
sum = create_function_or_observable(Sum, SumEvent)
         

@registry.expose(['Arithmetic', '/'], args = (constant(1.), constant(1.)))
class Div(BinaryOp[float], Function[float]):
    """ Function returning division of the operands
    """
    def __call__(self, *args, **kwargs):
        lhs = self.lhs()
        rhs = self.rhs()
        return lhs / rhs if lhs is not None and rhs is not None and rhs != 0 else None
    
    @property
    def label(self):
        return '\\frac{'+self.lhs.label+'}{'+self.rhs.label+'}'
    
    def __repr__(self):
        return repr(self.lhs)+ "/" + repr(self.rhs)
    
class DivEvent(Div, types.Observable):
    
    def __init__(self, lhs, rhs):
        Div.__init__(self, lhs, rhs)
        types.Observable.__init__(self)
            
div = create_function_or_observable(Div, DivEvent)

@registry.expose(['Arithmetic', '-'], args = (constant(1.), constant(1.)))    
class Sub(BinaryOp[float], Function[float]):
    """ Function substructing the right operand from the left one
    """
    
    def __call__(self, *args, **kwargs):
        lhs = self.lhs()
        rhs = self.rhs()
        return lhs - rhs if lhs is not None and rhs is not None else None
    
    @property
    def label(self):
        return self.lhs.label + ' - ' + self.rhs.label
    
    def __repr__(self):
        return repr(self.lhs)+ "-" + repr(self.rhs)

class SubEvent(Sub, types.Observable):
    
    def __init__(self, lhs, rhs):
        Sub.__init__(self, lhs, rhs)
        types.Observable.__init__(self)
            
sub = create_function_or_observable(Sub, SubEvent)

class Derivative(Function[float]):
    
    def __init__(self, source):
        self.source = source
        
    @property
    def attributes(self):
        return {}
        
    _properties = { 'source' : types.IDifferentiable }
    
    @property
    def label(self):
        return '\\frac{d' + getLabel(self.source) + '}{dt}'
        
    def __call__(self):
        return self.source.derivative()
   
