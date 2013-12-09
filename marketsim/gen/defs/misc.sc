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


type IOrderQueue
type IOrderBook

type ISingleAssetTrader

package observable
{
    @python.intrinsic.function ("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "observable.ewma.EWMA_Impl")
    def EWMA (source = const (), alpha = 0.015) => Float

    package trader
    {
        @python.intrinsic.function ("Proxies", "$(Trader)", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
    }

    package orderbook
    {
        @python.intrinsic.function ("Proxies", "$(TraderAsset)", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader = trader.SingleProxy()) : IOrderBook

        @python.intrinsic.function ("-", "Asks", "orderbook.queue._Asks_Impl")
        def Asks(book = OfTrader()) : IOrderQueue
        @python.intrinsic.function ("-", "Bids", "orderbook.queue._Bids_Impl")
        def Bids(book = OfTrader()) : IOrderQueue

        def BestPrice(queue = Asks()) : IObservable
        def LastPrice(queue = Asks()) : IObservable
        def LastTradePrice (queue = Asks()) : IObservable
        def LastTradeVolume(queue = Asks()) : IObservable
        def PriceAtVolume(queue = Asks(), volume = 100.0) => Float

        def WeightedPrice(queue = Asks(), alpha = 0.015) =
            EWMA(LastTradePrice(queue)*LastTradeVolume(queue), alpha) / EWMA(LastTradeVolume(queue), alpha)

        def TickSize(book = OfTrader()) => Float

        def AskPrice(book = OfTrader()) = BestPrice(Asks(book))
        def BidPrice(book = OfTrader()) = BestPrice(Bids(book))

        def Spread(book = OfTrader()) = AskPrice(book) - BidPrice(book)
        def MidPrice(book = OfTrader()) = (AskPrice(book) + BidPrice(book)) / 2

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




