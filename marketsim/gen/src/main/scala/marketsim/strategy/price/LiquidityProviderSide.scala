package marketsim.strategy.price

import marketsim._

class LiquidityProviderSide(account             : Account,
                            side                : Side,
                            intervals           : () => Double,
                            price_multipliers   : () => Double,
                            price_factory       : (() => Ticks) => OrderFactory,
                            default_price       : Double)
{
    private def ticks() = {
        val book = account.orderbook
        val tickSize = book.tickSize
        val queue = book Queue side

        val dp = side match {
            case Sell => (default_price / tickSize).ceil.toInt
            case Buy  => (default_price / tickSize).floor.toInt
        }

        orderbook.SafeSidePrice(queue, dp)()
    }

    new strategy.Periodic(account, Event.Every(intervals), price_factory(ticks))
}
