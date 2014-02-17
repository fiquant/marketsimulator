from marketsim import meta, constraints, Side, types, registry, getLabel, event, _
import marketsim
import math, inspect

Observable = types.Factory('Observable', '''(types.IObservable[%(T)s], event.Conditional_Impl):''', globals())

Observable[int]._types.append(Observable[float])
