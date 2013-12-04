package observable
{
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x = constant()) = x*x

    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x = constant(), y = constant()) = if x < y then x else y

    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x = constant(), y = constant()) = if x > y then x else y
}

@python.function("Basic", "C=%(x)s")
def constant(x = 1.0) : IFunction = const(x)

@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x = 1.0) : IObservable

type IFunction = () => Float
type IObservable : IFunction

package observable
{
    @python.intrinsic.function ("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "observable.ewma.EWMA_Impl")
    def EWMA (source = const (), alpha = 0.015) => Float
}

package trash

package types {
    type T
    type R : T
    type U : T, R
    type T1 = T
}

def A(x = in1.in2.A()) => types.R

package in1
def A(x : () => types.T1 = trash.A()) => types.U

package in2
def A(x = constant(), y = if 3 > x + 2 then x else x*2) => types.T




