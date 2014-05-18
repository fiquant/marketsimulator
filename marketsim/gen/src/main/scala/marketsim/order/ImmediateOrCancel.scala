package marketsim.order

import marketsim._
import marketsim.OrderRequest

class ImmediateOrCancel(proto : LimitOrder) extends Order
{
    val volume = proto.volume

    def processIn(target : OrderbookDispatch, events : OrderListener)
    {
        target handle OrderRequest(proto, events)
        target handle CancelOrder(proto)
    }
}
