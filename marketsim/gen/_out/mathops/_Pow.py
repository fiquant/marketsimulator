from marketsim import registry, types, event
import math
from _all import Observable, Constant


@registry.expose(['Log/Pow', 'Pow'])
class Pow(Observable[float]):

    """ 
     Exceptional cases follow Annex F of the C99 standard as far as possible.
     In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     even when *x* is a zero or a NaN.
     If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     ``pow(x, y)`` is undefined, and raises ``ValueError``.
    """ 
    def __init__(self, base  = const(1.0), power  = const(1.0)):
        Observable[float].__init__(self)
        self.base = base
        if isinstance(base, types.IEvent):
            event.subscribe(self.base, self.fire, self)
        self.power = power
        if isinstance(power, types.IEvent):
            event.subscribe(self.power, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'base' : types.IFunction[float],
        'power' : types.IFunction[float]
    }

    def __repr__(self):
        return "%(base)s^{%(power)s}" % self.__dict__


    def __call__(self, *args, **kwargs):
        base = self.base()
        if base is None: return None
        power = self.power()
        if power is None: return None
        return math.pow(self.base, self.power)


