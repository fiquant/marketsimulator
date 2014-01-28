from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect 

from _function import Function

Observable = types.Factory('Observable', '''(types.IObservable[%(T)s], Function[%(T)s], event.Conditional):''', globals())

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


from marketsim.gen._out.ops._Negate import Negate as negate

def subscribe_if_event(source, target):
    if isinstance(source, types.IEvent):
        event.subscribe(source, _(target).fire, target)

@registry.expose(['Basic', 'Identity'])
def identity(x = None):
    return  x if x is not None else constant(1.)

