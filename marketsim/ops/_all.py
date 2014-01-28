from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect 

from _function import Function

Observable = types.Factory('Observable', '''(types.IObservable[%(T)s], Function[%(T)s], event.Conditional):''', globals())

from marketsim.gen._out.ops._Negate import Negate as negate

def subscribe_if_event(source, target):
    if isinstance(source, types.IEvent):
        event.subscribe(source, _(target).fire, target)

@registry.expose(['Basic', 'Identity'])
def identity(x = None):
    from marketsim.gen._out._constant import constant
    return  x if x is not None else constant(1.)

