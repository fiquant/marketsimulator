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

    trait OrderQueue
    {
        import marketsim.Event

        val BestPossiblyChanged : Event[Option[Ticks]]
        val TradeDone : Event[(Ticks, Int)]
    }
    trait Orderbook
    {
        def handle(request : Request)

        val Asks : OrderQueue
        val Bids : OrderQueue
    }

    trait OrderbookDispatch extends Orderbook
    {
        def process(order : MarketOrder, events : OrderListener)
        def process(order : LimitOrder, events : OrderListener)

        def process(cancel : CancelOrder)
    }

    // abstract class for all requests that can be handled by order books
    trait Request
    {
        def processIn(orderbook : OrderbookDispatch)

        def remote(link : orderbook.remote.Link) : Request
    }

    trait OrderListener
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
    
    trait Order
    {
        self =>

        val volume : Volume
        def side = if (volume > 0) Sell else Buy
        def volumeAbsolute = volume.abs

        def processIn(target : OrderbookDispatch, events : OrderListener)
    }

    case class OrderRequest(order : Order, events : OrderListener) extends Request
    {
        self =>

        def processIn(target : OrderbookDispatch) = order processIn (target, events)

        def remote(link : orderbook.remote.Link) = copy(events = new OrderListener {
            def OnTraded(order : Order, price : Ticks, volume : Volume) = link send { events OnTraded (order, price, volume) }
            def OnStopped(order : Order, unmatchedVolume : Volume)      = link send { events OnStopped (order, unmatchedVolume) }
            override def toString = self.toString
        })
    }


    case class MarketOrder(volume : Volume) extends Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener) = target process (this, events)

        override def toString = s"Market[$volume]"
    }

    trait OrderFactory
    {
        def create : Order
    }

    case class MarketOrderFactory(volume : () => Volume) extends OrderFactory
    {
        def create = MarketOrder(volume())
    }
    
    case class LimitOrder(price : Ticks, volume : Volume) extends Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener) = target process (this, events)

        override def toString = s"Limit[$volume@$price]"
    }

    case class LimitOrderFactory(price  : () => Ticks,
                                 volume : () => Volume) extends OrderFactory
    {
        def create = LimitOrder(price(), volume())
    }

    case class CancelOrder(order : LimitOrder) extends Request
    {
        def remote(link : orderbook.remote.Link) = this

        def processIn(book : OrderbookDispatch) = book process this
    }
}
