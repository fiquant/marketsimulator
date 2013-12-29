@category = "Order"

package order {
    @python.order.factory("order.market.Market_Impl")
    @label = "Market(%(side)s, %(volume)s)"
    def Market(side = side.Sell(),
               volume = constant(1.0)) : IObservable[Order]
        
    
    @python.order.factory("order.limit.Limit_Impl")
    @label = "Limit(%(side)s, %(price)s, %(volume)s)"
    def Limit(side = side.Sell(),
              price = constant(100.0),
              volume = constant(1.0)) : IObservable[Order]
        
}
