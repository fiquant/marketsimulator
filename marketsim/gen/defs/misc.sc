def min(x = mathops.Exp(), y = constant()) = if x < y then x else y
def max(x = constant(), y = constant()) = if x > y then x else y

package observable
{
    @python.observable("Pow/Log", "{%s}^2")
    def Sqr(x = constant()) = x*x
}

def constant(x = 1.0) : Float

package thrash

def A(x = in1.in2.B()) : Float

package in1
def C(x = A()) : Float

package in2
def B(x = constant(), y = if 3 > x + 2 then x else x*2) : Float



