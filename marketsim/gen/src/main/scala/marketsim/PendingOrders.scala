package marketsim

import scala.collection.mutable

class PendingOrders(account : Account)
{
    private val orders = mutable.LinkedHashSet.empty[Order]

    account.OrderSent    += {       order     => orders add    order }
    account.OrderStopped += { case (order, _) => orders remove order }

    def getOrders = orders
}
