/** Exponent of x
  *
  */
@python.mathops("Log/Pow", "exp", "e^{%(x)s}")
def Exp(x : Float = 1.0)

/** Natural logarithm of x (to base e)
 *
 */
@python.mathops("Log/Pow", "log", "log(%(x)s)")
def Log(x : Float = 1.0)

/** Square root of x
 *
 */
@python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
def Sqrt(x : Float = 1.0)

/** Return *x* raised to the power *y*.
  *
  * Exceptional cases follow Annex F of the C99 standard as far as possible.
  * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
  * even when *x* is a zero or a NaN.
  * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
  * ``pow(x, y)`` is undefined, and raises ``ValueError``.
  */
@python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
def Pow(base : Float = 1.0, power : Float = 1.0)

/** Arc tangent of x, in radians.
 *
 */
@python.mathops("Trigonometric", "atan", "atan(%(x)s)")
def Atan(x : Float = 0.0)
