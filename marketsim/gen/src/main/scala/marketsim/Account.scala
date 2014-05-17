package marketsim

class Account(orderbook         : Orderbook,
              initialPosition   : Int = 0,
              initialBalance    : Ticks = 0) extends OrderListener
{
    private var position = initialPosition
    private var balance = initialBalance

    def getPosition = position
    def getBalance = balance

    val OrderSent = new Event[Order]
    val OrderTraded = new Event[(Order, Ticks, Int)]
    val OrderStopped = new Event[(Order, Int)]

    def send(order : Order)
    {
        orderbook handle order
        OrderSent(order)
    }

    def send(request : Request)
    {
        orderbook handle request
    }

    /**
     * Called when a trade is done with order
     * @param order  - order in trade
     * @param price  - price of the trade
     * @param volume - volume of the trade
     */
    def OnTraded(order : Order, price : Ticks, volume : Int)
    {
        order.side match {
            case Sell =>
                position -= volume
                balance += price
            case Buy =>
                position += volume
                balance -= price
        }
        OrderTraded((order, price, volume))
    }

    /**
     * Called when order is completely matched or cancelled
     */
    def OnStopped(order : Order, unmatchedVolume : Volume)
    {
        OrderStopped((order, unmatchedVolume))
    }

}
