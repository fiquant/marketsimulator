import marketsim.Event

package object marketsim {

    type Time     = Double
    type Callback = () => Unit

    sealed abstract class Side
    case object Sell extends Side
    case object Buy  extends Side

    // positive volume corresponds to Sell side, negative volume - to Buy side
    type Volume = Int

    // orderbook will work in term of ticks
    // converting floating price to ticks should be done by order factories
    type Ticks = Int

    trait Orderbook
    {
        def process(order : MarketOrder)
        def process(order : LimitOrder)

        def handle(request : Request)
    }

    // abstract class for all requests that can be handled by order books
    trait Request
    {
        def processIn(orderbook : Orderbook)
    }

    trait OrderListener[Order]
    {
        /**
         * Called when a trade is done with order
         * @param order  - order in trade
         * @param price  - price of the trade
         * @param volume - volume of the trade
         */
        def OnTraded(order : Order, price : Ticks, volume : Volume)

        /**
         * Called when order is completely matched or cancelled
         */
        def OnStopped(order : Order, unmatchedVolume : Volume)
    }
    
    type MarketOrderListener = OrderListener[MarketOrder]
    type LimitOrderListener = OrderListener[LimitOrder]

    trait Order[T] extends Request
    {
        self : T =>

        val volume : Volume
        def side = if (volume > 0) Sell else Buy
        def volumeAbsolute = volume.abs

        val owner : OrderListener[T]

        import marketsim.Scheduler.async

        def OnTraded(price : Ticks, volume : Volume) = async { owner OnTraded (self, price, volume) }
        def OnStopped(unmatchedVolume : Volume)      = async { owner OnStopped (self, unmatchedVolume) }
    }

    case class MarketOrder(volume : Volume, owner : MarketOrderListener) extends Order[MarketOrder]
    {
        def processIn(orderbook : Orderbook) = orderbook process this
    }
    
    case class LimitOrder(price : Ticks, volume : Volume, owner : LimitOrderListener) extends Order[LimitOrder]
    {
        def processIn(orderbook : Orderbook) = orderbook process this
    }

    trait IOrderQueue
    {
        import marketsim.Event

        val BestPossiblyChanged : Event[Option[Ticks]]
        val TradeDone : Event[(Ticks, Int)]
    }
}
