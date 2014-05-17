package marketsim.orderbook

import marketsim._

abstract class Entry(initialVolume : Volume)
{
    val order : LimitOrder

    private var volumeUnmatched = initialVolume

    def isEmpty = volumeUnmatched == 0
    def getVolumeUnmatched = volumeUnmatched

    def side : Side
    def canMatchWith(other : LimitOrder) : Boolean
    def signedTicks = makeSignedTicks(order.price)
    def makeSignedTicks(ticks : Int) : Ticks

    /**
     * Matches a limit order with a suitable market or limit order
     * @param other - order to match with
     * @param otherVolumeUnmatched - unmatched volume of the other order
     * @return new unmatched volume of the other order
     */
    def matchWith[T <: Order](other : T, otherVolumeUnmatched : Volume) =
    {
        assert(otherVolumeUnmatched > 0)
        assert(volumeUnmatched > 0)

        val trade_volume = otherVolumeUnmatched min volumeUnmatched
        val trade_price = order.price

        order OnTraded (trade_price, trade_volume)
        other OnTraded (trade_price, trade_volume)

        volumeUnmatched -= trade_volume
        trade_volume
    }
}

final class SellEntry(val order : LimitOrder, initialVolume : Volume) extends Entry(initialVolume)
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
    def apply(order : LimitOrder, initialVolume : Volume) = new SellEntry(order, initialVolume)
    def apply(order : LimitOrder) = new SellEntry(order, order.volumeAbsolute)
}

final class BuyEntry(val order : LimitOrder, initialVolume : Volume) extends Entry(initialVolume)
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
    def apply(order : LimitOrder, initialVolume : Volume) = new BuyEntry(order, initialVolume)
    def apply(order : LimitOrder) = new BuyEntry(order, order.volumeAbsolute)
}


object Entry
{
    def apply(order : LimitOrder) =
        order.side match {
            case Sell => SellEntry(order)
            case Buy => BuyEntry(order)
        }
}