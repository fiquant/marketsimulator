@category = "Price function"

package observable.pricefunc() {
    def LiquidityProvider(side = side.Sell(),
                          initialValue = 100.0,
                          priceDistr = math.random.lognormvariate(0.0,0.1),
                          book = orderbook.OfTrader())
         = orderbook.SafeSidePrice(orderbook.Queue(book,side),constant(initialValue))*priceDistr
}
