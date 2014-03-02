@category = "Side function"
package strategy.side
{
    abstract type SideStrategy
    {
        def Strategy(/** Event source making the strategy to wake up*/
                    eventGen        = event.Every(math.random.expovariate(1.)),
                    /** order factory function*/
                    orderFactory    = order.side.Market()) = Generic(orderFactory(Side), eventGen)
    }

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

        = Signal(book~>MidPrice~>EW(alpha)~>Avg~>Derivative, threshold)

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
                book~>MidPrice~>EW(alpha_1)~>Avg -
                book~>MidPrice~>EW(alpha_2)~>Avg,
            threshold)

    /**
     * Fundamental value strategy believes that an asset should have some specific price
     * (*fundamental value*) and if the current asset price is lower than the fundamental value
     * it starts to buy the asset and if the price is higher it starts to sell the asset.
     */
    type FundamentalValue(
        /** observable fundamental value */
        fv      = .constant(200.),
        /** asset in question */
        book    = .orderbook.OfTrader()) : SideStrategy
    {
        /**
         * Side function for fundamental value strategy
         */
        def FV_Side
            =   if book~>Bids~>BestPrice > fv then side.Sell() else
                if book~>Asks~>BestPrice < fv then side.Buy()  else
                                                       side.Nothing()

        def Side = FV_Side
    }

    /**
      * Mean reversion strategy believes that asset price should return to its average value.
      * It estimates this average using some functional and
      * if the current asset price is lower than the average
      * it buys the asset and if the price is higher it sells the asset.
      */
    type MeanReversion(
        /** parameter |alpha| for exponentially weighted moving average */
        alpha = 0.015,
        /** asset in question */
        book = orderbook.OfTrader()) : SideStrategy
    {
        /**
         * Side function for mean reversion strategy
         */
        def Side = (FundamentalValue(
                            book~>MidPrice~>EW(alpha)~>Avg,
                            book))~>FV_Side
    }

    /**
      * Dependent price strategy believes that the fair price of an asset *A*
      * is completely correlated with price of another asset *B* and the following relation
      * should be held: *PriceA* = *kPriceB*, where *k* is some factor.
      * It may be considered as a variety of a fundamental value strategy
      * with the exception that it is invoked every the time price of another
      * asset *B* changes.
      */
    type PairTrading(
        /** reference to order book for another asset used to evaluate fair price of our asset */
        bookToDependOn  = .orderbook.OfTrader(),
        /** multiplier to obtain fair asset price from the reference asset price */
        factor          = 1.0,
        /** asset in question */
        book = orderbook.OfTrader()) : SideStrategy
    {
        /** Side function for pair trading strategy */
        def Side = (FundamentalValue(
                bookToDependOn~>MidPrice * factor,
                book))~>FV_Side
    }
}