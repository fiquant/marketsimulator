package observable
{
    @python.observable("Pow/Log", "{%x}^2")
    def Sqr(x = constant()) = x*x

    @python.observable("Basic", "min{%x, %y}")
    def Min(x = constant(), y = constant()) = if x < y then x else y

    @python.observable("Basic", "max{%x, %y}")
    def Max(x = constant(), y = constant()) = if x > y then x else y
}

def constant(x = 1.0) : Float

package trash

package types {
    type T
    type R : T
    type U : T, R
}

def A(x = in1.in2.A()) : types.R

package in1
def A(x : () => types.T = trash.A()) : types.U

package in2
def A(x = constant(), y = if 3 > x + 2 then x else x*2) : types.T




