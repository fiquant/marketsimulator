from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect

from _function import Function

Observable = types.Factory('Observable', '''(types.IObservable[%(T)s], Function[%(T)s], event.Conditional):''', globals())
