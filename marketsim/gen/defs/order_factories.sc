@category = "Order"
package order
{
    @python.order.factory("order.market.Order_Impl")
    @label = "Market(%(side)s, %(volume)s)"
    def Market(side = side.Sell(), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.limit.Order_Impl")
    @label = "Limit(%(side)s, %(price)s, %(volume)s)"
    def Limit(side = side.Sell(), price = constant(100.), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    @label = "FixedBudget(%(side)s, %(budget)s)"
    def FixedBudget(side = side.Sell(), budget = constant(1000.)) : IObservable[Order]

    @python.order.factory("order.meta.ioc.Order_Impl")
    @label = "ImmediateOrCancel(%(proto)s)"
    def ImmediateOrCancel(proto = Limit()) : IObservable[Order]

    @python.order.factory("order.meta.stoploss.Order_Impl")
    @label = "StopLoss(%(maxloss)s, %(proto)s)"
    def StopLoss(maxloss = const(0.1), proto = Market()) : IObservable[Order]
}