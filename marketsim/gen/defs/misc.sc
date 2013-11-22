def min(x = mathops.Exp(), y = const()) = if x < y then x else y
def max(x = const(), y = const()) = if x > y then x else y
def sqr(x = const()) = x*x

def const(x = 1.0) : Float

package thrash

def A(x = in1.in2.B()) : Float

package in1
def C(x = A()) : Float

package in2
def B(x = const(), y = if 3 > x + 2 then x else x*2) : Float



