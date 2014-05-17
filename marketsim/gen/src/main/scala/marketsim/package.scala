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
        def process(order : MarketOrder)
        def process(order : LimitOrder)

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
    
    trait Order extends Request
    {
        self =>

        val volume : Volume
        def side = if (volume > 0) Sell else Buy
        def volumeAbsolute = volume.abs

        val owner : OrderListener

        import marketsim.Scheduler.async

        def OnTraded(price : Ticks, volume : Volume) = async { owner OnTraded (this, price, volume) }
        def OnStopped(unmatchedVolume : Volume)      = async { owner OnStopped (this, unmatchedVolume) }

        protected def withOwner(owner : OrderListener) : Order

        def remote(link : orderbook.remote.Link) = withOwner(new OrderListener {
            def OnTraded(order : Order, price : Ticks, volume : Volume) = link send { owner OnTraded (order, price, volume) }
            def OnStopped(order : Order, unmatchedVolume : Volume)      = link send { owner OnStopped (order, unmatchedVolume) }
            override def toString = self.toString
        })
    }

    case class MarketOrder(volume : Volume, owner : OrderListener) extends Order
    {
        def processIn(orderbook : OrderbookDispatch) = orderbook process this
        protected def withOwner(owner : OrderListener) = copy(owner = owner)

        override def toString = s"Market[$volume]"
    }

    trait OrderFactory
    {
        def create : Order
    }

    case class MarketOrderFactory(volume : () => Volume,
                                  owner  : OrderListener) extends OrderFactory
    {
        def create = MarketOrder(volume(), owner)
    }
    
    case class LimitOrder(price : Ticks, volume : Volume, owner : OrderListener) extends Order
    {
        def processIn(orderbook : OrderbookDispatch) = orderbook process this
        protected def withOwner(owner : OrderListener) = copy(owner = owner)

        override def toString = s"Limit[$volume@$price]"
    }

    case class LimitOrderFactory(price  : () => Ticks,
                                 volume : () => Volume,
                                 owner  : OrderListener) extends OrderFactory
    {
        def create = LimitOrder(price(), volume(), owner)
    }

    case class CancelOrder(order : LimitOrder) extends Request
    {
        def remote(link : orderbook.remote.Link) = this

        def processIn(book : OrderbookDispatch) = book process this
    }
}
