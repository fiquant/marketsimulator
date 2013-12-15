
package observable.pricefunc {
    @python.observable("Price function", "Lp_{%(side)s}(%(book)s)")
    def LiquidityProvider(side = side.Sell(),
                          initialValue = 100.0,
                          priceDistr = mathutils.rnd.lognormvariate(0.0,0.1),
                          book = orderbook.OfTrader())
         = orderbook.SafeSidePrice(orderbook.Queue(book,side),constant(initialValue))*priceDistr
}
