from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect 

def convert(other):
    if type(other) in [int, float]:
        other = constant(other)
    return other


class Function_impl(object):
    
    def __add__(self, other):
        return Sum(self, convert(other))
    
    def __sub__(self, other):
        return Sub(self, convert(other))
    
    def __mul__(self, other):
        return Product(self, convert(other))
    
    def __div__(self, other):
        return Div(self, convert(other))
    
    def __lt__(self, other):
        return less(self, convert(other))
    
    def __gt__(self, other):
        return greater(self, convert(other))
    
    def __ge__(self, other):
        return greater_equal(self, convert(other))
    
    def __eq__(self, other):
        return equal(self, convert(other))
    
    def __ne__(self, other):
        return notequal(self, convert(other))

Function = types.Factory("Function", """(Function_impl, types.IFunction[%(T)s]):
    T = %(T)s
""", globals())   

Observable = types.Factory('Observable', '''(types.IObservable[%(T)s], Function[%(T)s], event.Conditional):''', globals())

class BinaryOp_Impl(object):
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs 
        if types.IEvent in inspect.getmro(type(lhs)):
            event.subscribe(lhs, _(self).fire, self)
        if types.IEvent in inspect.getmro(type(rhs)):
            event.subscribe(rhs, _(self).fire, self)
            
    def __call__(self):
        lhs = self.lhs()
        rhs = self.rhs()
        return self._call(lhs, rhs) if lhs is not None and rhs is not None else None

    @property
    def label(self):
        return '(' + self.lhs.label + self.sign + self.rhs.label + ')'
    
    def __repr__(self):
        return '(' + repr(self.lhs) + self.sign + repr(self.rhs) + ')'

BinaryOp = types.Factory("BinaryOp", """(BinaryOp_Impl, Observable[%(T)s]):
    def __init__(self, lhs, rhs):
        BinaryOp_Impl.__init__(self, lhs, rhs)
        Observable[%(T)s].__init__(self)

    _properties = [('lhs', meta.function((), %(T)s)), 
                   ('rhs', meta.function((), %(T)s))]
       
    @property
    def attributes(self):
        return {}
""", globals())
    
#---------------------------------------------- Condition 
        
class Condition_Impl(object):
    
    def __init__(self, cond, ifpart, elsepart):
        self.cond = cond
        self.ifpart = ifpart
        self.elsepart = elsepart
        
    def __call__(self):
        c = self.cond()
        assert c is not None
        return self.ifpart() if c else self.elsepart()
    
    def __repr__(self):
        return 'if ' + repr(self.cond) + ' then ' + repr(self.ifpart) + ' else ' + repr(self.elsepart)

Condition = types.Factory("Condition", """(Condition_Impl, Function[%(T)s]):

    def __init__(self, cond, ifpart, elsepart):
        Condition_Impl.__init__(self, cond, ifpart, elsepart)
        self._alias = self.classAlias
        
    _types = [meta.function((), %(T)s)]
        
    _properties = [('cond', meta.function((), bool)), 
                   ('ifpart', meta.function((), %(T)s)), 
                   ('elsepart', meta.function((), %(T)s))]
""", globals())


Condition[Side]
Condition[float]

Condition[Side].classAlias = ['Basic',"Condition[Side]"]
Condition[float].classAlias = ['Basic',"Condition[float]"]

class _Conditional_Base(Function[bool]):
    
    def __call__(self):
        lhs = self.lhs()
        rhs = self.rhs()
        return self._call(lhs, rhs)

    def __getitem__(self, (ifpart, elsepart)):
        T = getattr(ifpart, 'T', getattr(elsepart, 'T', None))
        if T is None:
            print "cannot infer expression type from ", ifpart, ' and ', elsepart
        return Condition[T](self, ifpart, elsepart)

# ---------------------------------------------------- Equal

class _Equal_Impl(_Conditional_Base):
    
    sign = "=="
    
    def _call(self, lhs, rhs):
        return lhs == rhs

Equal = types.Factory("Equal", """(_Equal_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '==']
""", globals())

def logic_op(T):
    def inner(lhs, rhs):
        if 'T' in dir(lhs):
            if 'T' in dir(rhs):
                assert lhs.T == rhs.T
            return T[lhs.T](lhs, rhs)
        if 'T' in dir(rhs):
            return T[rhs.T](lhs, rhs)
        raise "Cannot inference T for " + repr(lhs) + ' ' + T.sign + ' ' + repr(rhs)
    return inner

equal = logic_op(Equal)

Equal[float]   
# ---------------------------------------------------- NotEqual

class _NotEqual_Impl(_Conditional_Base):
    
    sign = "!="
    
    def _call(self, lhs, rhs):
        return lhs != rhs

NotEqual = types.Factory("NotEqual", """(_NotEqual_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '!=']
""", globals())

notequal = logic_op(NotEqual)

NotEqual[float]        
# ---------------------------------------------------- Greater

class _Greater_Impl(_Conditional_Base):
    
    sign = ">"
    
    def _call(self, lhs, rhs):
        return lhs > rhs

Greater = types.Factory("Greater", """(_Greater_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '>']
""", globals())

greater = logic_op(Greater)
    
Greater[float]
# ---------------------------------------------------- GreaterEqual

class _GreaterEqual_Impl(_Conditional_Base):
    
    sign = ">="
    
    def _call(self, lhs, rhs):
        return lhs >= rhs

GreaterEqual = types.Factory("GreaterEqual", """(_GreaterEqual_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '>=']
""", globals())

greater_equal = logic_op(GreaterEqual)
    
GreaterEqual[float]
# ---------------------------------------------------- Less

class _Less_Impl(_Conditional_Base):
    
    sign = "<"
    
    def _call(self, lhs, rhs):
        return lhs < rhs

Less = types.Factory("Less", """(_Less_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '<']
""", globals())

less = logic_op(Less)
    
Less[float]
# ---------------------------------------------------- LessEqual

class _LessEqual_Impl(_Conditional_Base):
    
    sign = "<="
    
    def _call(self, lhs, rhs):
        return lhs <= rhs

LessEqual = types.Factory("LessEqual", """(_LessEqual_Impl, BinaryOp[%(T)s]):
    BranchType = %(T)s
    def __init__(self, lhs, rhs):
        BinaryOp[%(T)s].__init__(self, lhs, rhs)
        self._alias = ['Logic', '<=']
""", globals())

less_equal = logic_op(LessEqual)
    
LessEqual[float]
# ---------------------------------------------------- Constant

# NB! _None is a special case of Constant but we don't use the latter 
# since we don't want to show Nones in the web-interface and in the object graph

class _None_Impl(object):
    
    def __call__(self):
        return None
    
    def __repr__(self):
        return 'None'

_None = types.Factory('_None', """(_None_Impl, Function[%(T)s]):
    def __init__(self):
        self._alias = ['Basic', 'None']
""", globals())

_None[Side]
_None[float]

# ---------------------------------------------------- Constant

class _Constant_Impl(object):
    """ Constant function returning **value**.
    """
    
    def _casts_to(self, dst):
        if type(dst) is meta.function:
            rv = dst.rv
            return rv is float or\
                (type(rv) is constraints.greater_or_equal and rv._bound <= self.value) or\
                (type(rv) is constraints.greater_than and rv._bound < self.value) or\
                (type(rv) is constraints.less_or_equal and rv._bound >= self.value) or\
                (type(rv) is constraints.less_than and rv._bound > self.value)
        return False 
        
    def __call__(self, *args, **kwargs):
        return self.value
    
    @property
    def label(self):
        return str(self.value)
    
    def __repr__(self):
        return "constant("+repr(self.value)+")"
    
_defaults = { float: 100, Side : Side.Sell, bool : True }

Constant = types.Factory('Constant', """(_Constant_Impl, Function[%(T)s], types.IObservable[%(T)s]):
    \""" Constant function returning **value**.
    \"""
    def __init__(self, value = _defaults[%(T)s]):
        self.value = value
        self._alias = ['Basic', 'Constant']
        
    def __iadd__(self, listener): 
        return self
        
    def __isub__(self, listener): 
        return self
    
    _properties = {'value' : %(T)s}
""", globals())

def constant(x):
    return Constant[float](x) if type(x) is float\
        else Constant[float](x) if type(x) is int\
        else Constant[Side](x) if x in [Side.Sell, Side.Buy]\
        else Constant[bool](x) if type(x) is bool\
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
    
def subscribe_if_event(source, target):
    if isinstance(source, types.IEvent):
        event.subscribe(source, _(target).fire, target)
    
@registry.expose(['Pow/Log', 'sqrt'])
class Sqrt(Observable[float]):
    def __init__(self, source = constant(1.)):
        self._source = source
        Observable[float].__init__(self)
        subscribe_if_event(source, self)        

    _properties = {'source': types.IFunction[float]}

    @property
    def source(self):
        return self._source

    @property
    def label(self):
        return "\sqrt{" + self._source.label + "}"

    def __repr__(self):
        return "sqrt(" + repr(self.arg) + ")"

    def __call__(self):
        r = self._source()
        return math.sqrt(r) if r is not None else None
    
sqrt = Sqrt

@registry.expose(['Pow/Log', 'ln'])
class Log(Observable[float]):
    def __init__(self, source = constant(1.)):
        self._source = source
        Observable[float].__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(source, _(self).fire, self)

    _properties = {'source': types.IFunction[float]}

    @property
    def source(self):
        return self._source

    @property
    def label(self):
        return "ln" + self._source.label + ""

    def __call__(self):
        r = self._source()
        return math.log(r) if r is not None and r > 0 else None

@registry.expose(['Pow/Log', 'exp'])
class Exp(Observable[float]):
    def __init__(self, source = constant(1.)):
        self._source = source
        Observable[float].__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(source, _(self).fire, self)

    _properties = {'source': types.IFunction[float]}

    @property
    def source(self):
        return self._source

    @property
    def label(self):
        return "e^{" + self._source.label + "}"

    def __call__(self):
        r = self._source()
        return math.exp(r) if r is not None else None

@registry.expose(['Trigonometric', 'atan'])
class Atan(Observable[float]):
    def __init__(self, source = constant(0.)):
        self._source = source
        Observable[float].__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(source, _(self).fire, self)

    _properties = {'source': types.IFunction[float]}

    @property
    def source(self):
        return self._source

    @property
    def label(self):
        return "atan(" + self._source.label + ")"

    def __call__(self):
        r = self._source()
        return math.atan(r) if r is not None else None

@registry.expose(['Pow/Log', 'pow'])
class Pow(Observable[float]):
    def __init__(self, base = constant(1.), power = constant(1.)):
        self._base = base
        self._power = power
        Observable[float].__init__(self)
        if isinstance(base, types.IEvent):
            event.subscribe(base, _(self).fire, self)
        if isinstance(power, types.IEvent):
            event.subscribe(power, _(self).fire, self)

    _properties = {
        'base' : types.IFunction[float], 
        'power': types.IFunction[float], 
    }

    @property
    def base(self):
        return self._base

    @property
    def power(self):
        return self._power

    @property
    def label(self):
        return self._base.label + "^{" + self._power.label + "}"

    def __call__(self):
        b = self._base()
        p = self._power()
        return math.pow(b,p) if b is not None and p is not None else None


@registry.expose(['Basic', 'Identity'])
class identity(Function[float]):
    
    def __init__(self, arg=constant(1.)):
        self.arg = arg
        
    _properties = { "arg" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        return self.arg()
    
    def __repr__(self):
        return "id(" + repr(self.arg) + ")"

@registry.expose(['Basic', 'Max'], args = (constant(1.), constant(1.)))
class Max(BinaryOp[float]):
    """ Function max of the operands
    """
    
    sign = ' max '
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs if lhs > rhs else rhs
    
@registry.expose(['Arithmetic', '*'], args = (constant(1.), constant(1.)))
class Product(BinaryOp[float]):
    """ Function returning product of the operands
    """
    
    sign = '*'
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs * rhs
    
@registry.expose(['Pow/Log', 'sqr'])
class Sqr(Observable[float]):
    
    def __init__(self, source = constant(1.)):
        self._source = source
        Observable[float].__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(source, _(self).fire, self)
        
    _properties = { 'source' : types.IFunction[float] }
    
    @property
    def source(self):
        return self._source
    
    def __call__(self):
        r = self._source()
        return r*r if r is not None else None

@registry.expose(['Arithmetic', '+'], args = (constant(1.), constant(1.)))    
class Sum(BinaryOp[float]):
    """ Function returning Sum of the operands
    """
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs + rhs

    sign = '+'         

@registry.expose(['Arithmetic', '/'], args = (constant(1.), constant(1.)))
class Div(BinaryOp[float]):
    """ Function returning division of the operands
    """
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs / rhs if rhs != 0 else None
    
    sign = '/'
    
    @property
    def label(self):
        return '\\frac{'+self.lhs.label+'}{'+self.rhs.label+'}'

@registry.expose(['Arithmetic', '-'], args = (constant(1.), constant(1.)))    
class Sub(BinaryOp[float]):
    """ Function substructing the right operand from the left one
    """
    
    def __init__(self, lhs, rhs):
        BinaryOp[float].__init__(self, lhs, rhs)
    
    def _call(self, lhs, rhs):
        return lhs - rhs
    
    sign = '-'

class Derivative(Function[float]):
    
    def __init__(self, source):
        self.source = source
        self._alias = ['Basic', 'Derivative']
        
    @property
    def attributes(self):
        return {}
        
    _properties = { 'source' : types.IDifferentiable }
    
    @property
    def label(self):
        return '\\frac{d' + getLabel(self.source) + '}{dt}'
        
    def __call__(self):
        return self.source.derivative()

