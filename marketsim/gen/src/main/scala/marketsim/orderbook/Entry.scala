package marketsim.orderbook

import marketsim._

case class Entry (order : LimitOrder)
{
    private var volumeUnmatched = order.volumeAbsolute

    def isEmpty = volumeUnmatched == 0
    def getVolumeUnmatched = volumeUnmatched

    def canMatchWith(other : LimitOrder) =
        order.side match {
            case Sell => other.price >= order.price
            case Buy  => other.price <= order.price
        }

    // returns unmatched volume of the other order
    def matchWith[T](other : Order[T], otherVolumeUnmatched : Volume) =
    {
        assert(otherVolumeUnmatched > 0)
        assert(volumeUnmatched > 0)

        val volume = otherVolumeUnmatched min volumeUnmatched
        val price = order.price

        order.OnTraded(price, volume)
        other.OnTraded(price, volume)

        volumeUnmatched -= volume
        otherVolumeUnmatched - volume
    }
}