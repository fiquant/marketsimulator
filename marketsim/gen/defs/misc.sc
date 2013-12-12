package observable
{
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x = constant()) = x*x

    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x = constant(), y = constant()) = if x < y then x else y

    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x = constant(), y = constant()) = if x > y then x else y

    @python.intrinsic.observable ("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt = 1.0, x = constant()) : IObservable
}

@python.function("Basic", "C=%(x)s")
def constant(x = 1.0) : IFunction = const(x)

@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x = 1.0) : IObservable


type IOrderQueue
type IOrderBook

type ISingleAssetTrader

package observable
{
    package trader
    {
        @python.intrinsic.function ("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
    }
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




