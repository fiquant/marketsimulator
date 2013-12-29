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
        
    
    @python.order.factory("order.meta.fixed_budget.FixedBudget_Impl")
    @label = "FixedBudget(%(side)s, %(budget)s)"
    def FixedBudget(side = side.Sell(),
                    budget = constant(1000.0)) : IObservable[Order]
        
    
    @python.order.factory("order.meta.ioc.ImmediateOrCancel_Impl")
    @label = "ImmediateOrCancel(%(proto)s)"
    def ImmediateOrCancel(proto = Limit()) : IObservable[Order]
        
}
