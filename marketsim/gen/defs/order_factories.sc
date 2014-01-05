@category = "Order"
package order
{
    @python.order.factory("order.market.Order_Impl")
    def Market(side = side.Sell(), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.limit.Order_Impl")
    def Limit(side = side.Sell(), price = constant(100.), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(side = side.Sell(), budget = constant(1000.)) : IObservable[Order]

    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(proto = Limit()) : IObservable[Order]

    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(maxloss = const(0.1), proto = Limit()) : IObservable[Order]

    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(expiry = const(10.), proto = Limit()) : IObservable[Order]

    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(lotSize = const(10.), proto = Limit()) : IObservable[Order]
}