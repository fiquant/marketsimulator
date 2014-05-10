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
        def OnTraded(order : Order, price : Ticks, volume : Volume)
        def OnMatched(order : Order)
    }
    
    type MarketOrderListener = OrderListener[MarketOrder]

    trait LimitOrderListener extends OrderListener[LimitOrder]
    {
        def OnCancelled(order : LimitOrder)
    }

    trait Order[T] extends Request
    {
        self : T =>

        val volume : Volume
        def side = if (volume > 0) Sell else Buy
        def volumeAbsolute = volume.abs

        val owner : OrderListener[T]

        def OnTraded(price : Ticks, volume : Volume)
        {
            owner OnTraded (self, price, volume)
        }
    }
    
    case class MarketOrder(volume : Volume, owner : MarketOrderListener) extends Order[MarketOrder]
    {
    }
    
    case class LimitOrder(price : Ticks, volume : Volume, owner : LimitOrderListener) extends Order[LimitOrder]
    {
    }
}
