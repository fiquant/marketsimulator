@category = "Order"

package order {
    @python.order.factory("order.market.Order_Impl")
    def Market(side = side.Sell(),
               volume = constant(1.0)) : IOrderGenerator
        
    
    @python.order.factory("order.limit.Order_Impl")
    def Limit(side = side.Sell(),
              price = constant(100.0),
              volume = constant(1.0)) : IOrderGenerator
        
    
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(side = side.Sell(),
                    budget = constant(1000.0)) : IOrderGenerator
        
    
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(maxloss = const(0.1),
                 proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(expiry = const(10.0),
                   proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(lotSize = const(10.0),
                proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(floatingPrice = constant(10.0),
                      proto = _curried.price_Limit()) : IOrderGenerator
        
}
