from marketsim import registry, types, event
import math
from _all import Observable, Constant
@registry.expose(['Log/Pow', 'Exp'])
class Exp(Observable[float]):
    """  Return e**x 
    """    

    def __init__(self, x = Constant[float](1.0)):
        Observable[float].__init__(self)        
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)


    @property
    def label(self):
        return repr(self)

    _properties = { 
        'x' : types.IFunction[float]
    }

    def __repr__(self):
        return "e^{%(x)s}" % self.__dict__


    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.exp(x)



@registry.expose(['Log/Pow', 'Log'])
class Log(Observable[float]):
    """  return the natural logarithm of x (to base e).
    
    """    

    def __init__(self, x = Constant[float](1.0)):
        Observable[float].__init__(self)        
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)


    @property
    def label(self):
        return repr(self)

    _properties = { 
        'x' : types.IFunction[float]
    }

    def __repr__(self):
        return "log(%(x)s)" % self.__dict__


    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.log(x)



@registry.expose(['Log/Pow', 'Pow'])
class Pow(Observable[float]):
    """  Return *x* raised to the power *y*. 
    Exceptional cases follow Annex F of the C99 standard as far as possible. 
    In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
    even when *x* is a zero or a NaN. 
    If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then 
    ``pow(x, y)`` is undefined, and raises ``ValueError``. 
    """    

    def __init__(self, base = Constant[float](1.0), power = Constant[float](1.0)):
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
        return math.pow(base, power)



@registry.expose(['Trigonometric', 'Atan'])
class Atan(Observable[float]):
    """  Return the arc tangent of x, in radians. 
    """    

    def __init__(self, x = Constant[float](0.0)):
        Observable[float].__init__(self)        
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)


    @property
    def label(self):
        return repr(self)

    _properties = { 
        'x' : types.IFunction[float]
    }

    def __repr__(self):
        return "atan(%(x)s)" % self.__dict__


    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.atan(x)



