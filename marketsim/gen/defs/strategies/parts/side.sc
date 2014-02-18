@category = "Side function"
package strategy.side
{
    /**
     * Side function for a noise trading strategy
     */
    def Noise(side_distribution = math.random.uniform(0., 1.)) =

        if side_distribution > 0.5 then side.Sell() else side.Buy()

    /**
     * Side function for signal strategy
     */
    @python.observable
    def Signal(/** signal to be listened to */
               signal       = constant(0.),
               /** threshold when the trader starts to act */
               threshold    = 0.7) =

        if signal >   threshold then side.Buy()  else
        if signal < 0-threshold then side.Sell() else
                                     side.Nothing()

    /**
     * Side function for trend follower strategy
     */
    def TrendFollower(
            /** parameter |alpha| for exponentially weighted moving average */
            alpha   = 0.15,
            /** threshold when the trader starts to act */
            threshold    = 0.,
            /** asset in question */
            book = orderbook.OfTrader())

        = Signal(math.Derivative(math.EW.Avg(orderbook.MidPrice(book), alpha)), threshold)

    /**
     * Side function for crossing averages strategy
     */
    def CrossingAverages(
            /** parameter |alpha| for exponentially weighted moving average 1 */
            alpha_1 = 0.15,
            /** parameter |alpha| for exponentially weighted moving average 2 */
            alpha_2 = 0.015,
            /** threshold when the trader starts to act */
            threshold    = 0.,
            /** asset in question */
            book = orderbook.OfTrader())

        = Signal(
                math.EW.Avg(orderbook.MidPrice(book), alpha_1) -
                math.EW.Avg(orderbook.MidPrice(book), alpha_2),
            threshold)

    /**
     * Side function for fundamental value strategy
     */
    def FundamentalValue(
        /** observable fundamental value */
        fv      = constant(200.),
        /** asset in question */
        book    = orderbook.OfTrader())

        =   if orderbook.bid.Price(book) > fv then side.Sell() else
            if orderbook.ask.Price(book) < fv then side.Buy()  else
                                                   side.Nothing()

    /**
     * Side function for mean reversion strategy
     */
    def MeanReversion(
        /** parameter |alpha| for exponentially weighted moving average */
        alpha = 0.015,
        /** asset in question */
        book = orderbook.OfTrader())

        =   FundamentalValue(
                math.EW.Avg(orderbook.MidPrice(book), alpha),
                book)

    /** Side function for pair trading strategy */
    def PairTrading(
        /** reference to order book for another asset used to evaluate fair price of our asset */
        bookToDependOn  = orderbook.OfTrader(),
        /** multiplier to obtain fair asset price from the reference asset price */
        factor          = 1.0,
        /** asset in question */
        book = orderbook.OfTrader())

        =   FundamentalValue(
                orderbook.MidPrice(bookToDependOn) * factor,
                book)
}