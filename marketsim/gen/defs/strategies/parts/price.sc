@category = "Price function"
package strategy.price
{
    def LiquidityProvider(
            side = side.Sell(),
            initialValue = 100.,
            priceDistr = math.random.lognormvariate(0., .1),
            book = orderbook.OfTrader())

        = orderbook.SafeSidePrice(orderbook.Queue(book, side), constant(initialValue)) * priceDistr
}