from types import *
import ops

from _impl import mathops 

defs = mathops.defs

@mathops.imported("Log/Pow", "exp", "e^{%(x)s}")
class Exp:
    """ Return e**x """
    
    x = 1.

@mathops.imported("Log/Pow", "log", "log(%(x)s)")
class Log:
    """ return the natural logarithm of x (to base e).
    """
    
    x = 1.

@mathops.imported("Log/Pow", "sqrt", "\sqrt{%(x)s}")
class Sqrt:
    """ Return the square root of x. """

    x = 1.

@mathops.imported("Log/Pow", "pow", "%(base)s^{%(power)s}")
class Pow:
    u""" Return *x* raised to the power *y*. 
    Exceptional cases follow Annex F of the C99 standard as far as possible. 
    In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
    even when *x* is a zero or a NaN. 
    If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then 
    ``pow(x, y)`` is undefined, and raises ``ValueError``. """
    
    base = 1.
    power = 1.
    
@mathops.imported("Trigonometric", "atan", "atan(%(x)s)")
class Atan:
    """ Return the arc tangent of x, in radians. """
    
    x = 0.
    
