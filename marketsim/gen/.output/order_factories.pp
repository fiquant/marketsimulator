@category = "Order"

package order {
    @python.order.factory("order.market.Market_Impl")
    @label = "Market(%(side)s, %(volume)s)"
    def Market(side = side.Sell(),
               volume = constant(1.0)) : IObservable[Order]
        
}
