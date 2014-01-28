from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect 

from _function import Function

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
        return self.label

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

Condition = {}

from marketsim.gen._out.math._Condition_Float import Condition_Float
from marketsim.gen._out.math._Condition_Side import Condition_Side

Condition[float] = Condition_Float
Condition[Side] = Condition_Side

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


def constant(x = 1.):
    from marketsim.gen._out._const import const
    return const(x) if type(x) is float\
        else Constant[float](x) if type(x) is int\
        else Constant[Side](x) if x in [Side.Sell, Side.Buy]\
        else Constant[bool](x) if type(x) is bool\
        else None    


@registry.expose(['Arithmetic', 'negate'])
class negate(Function[float]):
    """ Function returning Product of the operands
    """
    
    def __init__(self, arg=None):
        self.arg = arg if arg is not None else constant(1.)
        
    _properties = { "arg" : types.IFunction[float] }
    
    def __call__(self, *args, **kwargs):
        x = self.arg()
        return -x if x is not None else None
    
    def __repr__(self):
        return "-" + repr(self.arg)
    
def subscribe_if_event(source, target):
    if isinstance(source, types.IEvent):
        event.subscribe(source, _(target).fire, target)

@registry.expose(['Basic', 'Identity'])
def identity(x = None):
    return  x if x is not None else constant(1.)

