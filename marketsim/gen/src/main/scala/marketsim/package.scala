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

    // abstract class for all requests that can be handled by order books
    trait Request

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
         * Called when order is completely matched
         */
        def OnMatched(order : Order)

        /**
         * Called when order is cancelled (for limit orders) or cannot be matched (for market orders)
         * Implies that order book stops this order processing
         */
        def OnCancelled(order : Order)
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

        def OnTraded(price : Ticks, volume : Volume) = owner OnTraded (self, price, volume)
        def OnMatched() = owner OnMatched self
        def OnCancelled() = owner OnCancelled self
    }

    case class MarketOrder(volume : Volume, owner : MarketOrderListener) extends Order[MarketOrder]
    {
    }
    
    case class LimitOrder(price : Ticks, volume : Volume, owner : LimitOrderListener) extends Order[LimitOrder]
    {
    }
}
