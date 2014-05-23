package marketsim.orderbook

import marketsim._

abstract class Entry(initialVolume : Volume)
{
    val order : LimitOrder
    val owner : OrderListener

    private var volumeUnmatched = initialVolume

    def isEmpty = volumeUnmatched == 0
    def getVolumeUnmatched = volumeUnmatched

    def getVolumeUnmatchedSigned = side match {
        case Sell => volumeUnmatched
        case Buy  => -volumeUnmatched
    }

    def side : Side
    def canMatchWith(other : LimitOrder) : Boolean
    def price = order.price
    def signedTicks = makeSignedTicks(order.price)
    def makeSignedTicks(ticks : Int) : Ticks

    /**
     * Matches a limit order with a suitable market or limit order
     * @param other - order to match with
     * @param otherVolumeUnmatched - unmatched volume of the other order
     * @return new unmatched volume of the other order
     */
    def matchWith[T <: Order](other : T, otherVolumeUnmatched : Volume, otherEvents : OrderListener) =
    {
        assert(otherVolumeUnmatched > 0)
        assert(volumeUnmatched > 0)

        val trade_volume = otherVolumeUnmatched min volumeUnmatched
        val trade_price = order.price

        val (v, p) = side match {
            case Sell => (-trade_volume,  trade_price)
            case Buy  => ( trade_volume, -trade_price)
        }

        import marketsim.Scheduler.async

        async { owner       OnTraded (order,  p,  v) }
        async { otherEvents OnTraded (other, -p, -v) }

        volumeUnmatched -= trade_volume
        trade_volume
    }
}

final class SellEntry(val order : LimitOrder, initialVolume : Volume, val owner : OrderListener) extends Entry(initialVolume)
{
    def side = Sell

    def canMatchWith(other : LimitOrder) = {
        assert(other.side == Buy)
        other.price >= order.price
    }

    def makeSignedTicks(price : Ticks) = price
}

object SellEntry
{
    def apply(order : LimitOrder, initialVolume : Volume, owner : OrderListener) = new SellEntry(order, initialVolume, owner)
    def apply(order : LimitOrder, owner : OrderListener) = new SellEntry(order, order.volumeAbsolute, owner)
}

final class BuyEntry(val order : LimitOrder, initialVolume : Volume, val owner : OrderListener) extends Entry(initialVolume)
{
    def side = Buy

    def canMatchWith(other : LimitOrder) = {
        assert(other.side == Sell)
        other.price <= order.price
    }

    def makeSignedTicks(price : Ticks) = -price
}

object BuyEntry
{
    def apply(order : LimitOrder, initialVolume : Volume, owner : OrderListener) = new BuyEntry(order, initialVolume, owner)
    def apply(order : LimitOrder, owner : OrderListener) = new BuyEntry(order, order.volumeAbsolute, owner)
}


object Entry
{
    def apply(order : LimitOrder, owner : OrderListener) =
        order.side match {
            case Sell => SellEntry(order, owner)
            case Buy => BuyEntry(order, owner)
        }
}