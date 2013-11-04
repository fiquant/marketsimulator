
from marketsim import registry, types, event
import math
from _all import Observable, Constant
            
@registry.expose(['Log/Pow', 'Exp'])
class Exp(Observable[float]):
    """ 
    """ 
    def __init__(self, x = 1.0):
        Observable[float].__init__(self)
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : float
    }

    def __repr__(self):
        return "Some(e^{%(x)s})" % self.__dict__

    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.exp(self.x)


@registry.expose(['Log/Pow', 'Log'])
class Log(Observable[float]):
    """ 
    """ 
    def __init__(self, x = 1.0):
        Observable[float].__init__(self)
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : float
    }

    def __repr__(self):
        return "Some(log(%(x)s))" % self.__dict__

    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.log(self.x)


@registry.expose(['Log/Pow', 'Sqrt'])
class Sqrt(Observable[float]):
    """ 
    """ 
    def __init__(self, x = 1.0):
        Observable[float].__init__(self)
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : float
    }

    def __repr__(self):
        return "Some(\\sqrt{%(x)s})" % self.__dict__

    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.sqrt(self.x)


@registry.expose(['Log/Pow', 'Pow'])
class Pow(Observable[float]):
    """ 
     Exceptional cases follow Annex F of the C99 standard as far as possible.
     In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     even when *x* is a zero or a NaN.
     If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     ``pow(x, y)`` is undefined, and raises ``ValueError``.
    """ 
    def __init__(self, base = 1.0, power = 1.0):
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
        'base' : float,
        'power' : float
    }

    def __repr__(self):
        return "Some(%(base)s^{%(power)s})" % self.__dict__

    def __call__(self, *args, **kwargs):
        base = self.base()
        if base is None: return None
        power = self.power()
        if power is None: return None
        return math.pow(self.base, self.power)


@registry.expose(['Trigonometric', 'Atan'])
class Atan(Observable[float]):
    """ 
    """ 
    def __init__(self, x = 0.0):
        Observable[float].__init__(self)
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : float
    }

    def __repr__(self):
        return "Some(atan(%(x)s))" % self.__dict__

    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.atan(self.x)

