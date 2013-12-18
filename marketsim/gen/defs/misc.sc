@category = "Basic"
package observable
{
    @python.observable
    @category = "Pow/Log"
    @label = "{%(x)s}^2"
    def Sqr(x = constant()) = x*x

    @python.observable
    @label = "min{%(x)s, %(y)s}"
    def Min(x = constant(), y = constant()) = if x < y then x else y

    @python.observable
    @label = "max{%(x)s, %(y)s}"
    def Max(x = constant(), y = constant()) = if x > y then x else y

    @python.intrinsic.observable ("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    def OnEveryDt(dt = 1.0, x = constant()) : IObservable
}

@python.function
@label = "C=%(x)s"
@category = "Basic"
def constant(x = 1.0) : IFunction = const(x)

@python.intrinsic.function("_constant._Constant_Impl")
@category = "Basic"
@label = "C=%(x)s"
def const(x = 1.0) : IObservable

@python.intrinsic.function("_constant._Null_Impl")
@category = "Basic"
@label = "Null"
def null() => Float

@python.observable
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
def IfDefined(x = constant(), elsePart = constant()) =
    if x <> null() then x else elsePart


type Side

@category = "Side"
package side
{
    @python.intrinsic.function("side._Sell_Impl")
    @label = "Sell"
    def Sell() => Side

    @python.intrinsic.function("side._Buy_Impl")
    @label = "Buy"
    def Buy() => Side

    @python.intrinsic.function("side._Buy_Impl")
    @label = "NoneSide"
    def Nothing() => Side
}


type IOrderQueue
type IOrderBook

type ISingleAssetTrader

type IDifferentiable : IFunction

@python.intrinsic.function ("observable.derivative._Derivative_Impl")
@category = "Basic"
@label = "\\frac{d%(x)s}{dt}"
def Derivative(x : IDifferentiable = observable.EW.Avg()) => Float

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




