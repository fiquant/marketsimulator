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

    type PriceVolume = (Ticks, Int)

    trait OrderQueue
    {
        import marketsim.Event

        val BestPossiblyChanged : Event[Option[PriceVolume]]
        val TradeDone : Event[PriceVolume]
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

        def cancel(order : LimitOrder)
    }

    // abstract class for all requests that can be handled by order books
    trait Request
    {
        def processIn(orderbook : OrderbookDispatch)

        def remote(link : orderbook.remote.Link) : Request
    }

    trait OrderListener
    {
        target =>

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

        def proxy(source : Order) =

            new OrderListener {
                def OnTraded(order : Order, price: Ticks, volume : Volume) = target OnTraded (source, price, volume)
                def OnStopped(order : Order, unmatchedVolume : Volume) = target OnStopped (source, unmatchedVolume)
            }
    }


    trait Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener)
        def withVolume(volume : Int) : Order

        def volume : Volume
        def side = if (volume > 0) Sell else Buy
        def volumeAbsolute = volume.abs
    }

    trait PriceOrder extends Order
    {
        def price : Ticks
        def withPrice(p : Ticks) : PriceOrder

        def withVolume(volume : Int) : PriceOrder
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

        override def toString = s"{$order}"
    }


    case class MarketOrder(volume : Volume) extends Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener) = target process (this, events)

        def withVolume(v : Int) = copy(volume = v)

        override def toString = s"Market[$volume]"
    }

    trait OrderFactory
    {
        def create : Order
    }

    trait PriceOrderFactory extends OrderFactory
    {
        def create : PriceOrder
    }


    trait OrderFactoryByVolume
    {
        def create(volume : Int) : Order
    }

    case class MarketOrderFactory(volume : () => Volume) extends OrderFactory
    {
        def create = MarketOrder(volume())
    }
    
    case class LimitOrder(price : Ticks, volume : Volume) extends PriceOrder
    {
        def processIn(target : OrderbookDispatch, events : OrderListener) = target process (this, events)

        def withVolume(v : Int) = copy(volume = v)
        def withPrice(p : Ticks) = copy(price = p)

        override def toString = s"Limit[$volume@$price]"
    }

    case class LimitOrderFactory(price  : () => Ticks,
                                 volume : () => Volume) extends PriceOrderFactory
    {
        def create = LimitOrder(price(), volume())

        override def toString = s"Limit{$price, $volume}"
    }

    trait MetaOrder extends Order
    {
        protected var cancel_ = () => ()

        def cancel() = cancel_()
    }

    trait PriceMetaOrder extends PriceOrder with MetaOrder


    case class CancelOrder(order : Order) extends Request
    {
        def remote(link : orderbook.remote.Link) = this

        def processIn(book : OrderbookDispatch) = order match {
            case x : LimitOrder => book cancel x
            case x : MetaOrder  => x.cancel()
        }
    }

    def const[T](x : T) = Constant[T](x)

    case class Constant[T](x : T) extends (() => T)
    {
        def apply() = x

        override def toString() = x.toString
    }
}
