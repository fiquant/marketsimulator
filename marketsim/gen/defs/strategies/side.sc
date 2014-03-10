@category = "Side function"
package strategy.side
{
    abstract type SideStrategy
    {
        def Strategy(/** Event source making the strategy to wake up*/
                    eventGen        = event.Every(math.random.expovariate(1.)),
                    /** order factory function*/
                    orderFactory    = order.side.Market())

            = Generic(orderFactory(Side), eventGen)
    }

    type Noise(side_distribution = math.random.uniform(0., 1.)) : SideStrategy
    {
        def Side = if side_distribution > 0.5 then side.Sell() else side.Buy()
    }

    /**
     * Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    type Signal(/** signal to be listened to */
               source       = .constant(0.),
               /** threshold when the trader starts to act */
               threshold    = 0.7) : SideStrategy
    {
        def S_Side =
            if source >   threshold then side.Buy()  else
            if source < 0-threshold then side.Sell() else
                                         side.Nothing()

        def Side = S_Side
    }


    /**
     * Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand
     * the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    type TrendFollower(
            /** parameter |alpha| for exponentially weighted moving average */
            alpha   = 0.15,
            /** threshold when the trader starts to act */
            threshold    = 0.,
            /** asset in question */
            book = .orderbook.OfTrader()) : SideStrategy
    {
        def Side = (book~>MidPrice
                        ~>EW(alpha)~>Avg
                        ~>Derivative)
                        ~>Signal(threshold)~>S_Side
    }


    /**
      * Two averages strategy compares two averages of price of the same asset but
      * with different parameters ('slow' and 'fast' averages) and when
      * the first is greater than the second one it buys,
      * when the first is lower than the second one it sells
      */
    type CrossingAverages(
            /** parameter |alpha| for exponentially weighted moving average 1 */
            alpha_1 = 0.15,
            /** parameter |alpha| for exponentially weighted moving average 2 */
            alpha_2 = 0.015,
            /** threshold when the trader starts to act */
            threshold    = 0.,
            /** asset in question */
            book = .orderbook.OfTrader()) : SideStrategy
    {
        def Side = (book~>MidPrice~>EW(alpha_1)~>Avg -
                    book~>MidPrice~>EW(alpha_2)~>Avg)
                        ~>Signal(threshold)~>S_Side
    }

    abstract type FundamentalValueStrategy() : SideStrategy
    {
        def book = .orderbook.OfTrader()

        def Side
            =   if book~>Bids~>BestPrice > Fundamental_Value then side.Sell() else
                if book~>Asks~>BestPrice < Fundamental_Value then side.Buy()  else
                                                                  side.Nothing()
    }

    /**
     * Fundamental value strategy believes that an asset should have
     * some specific price (*fundamental value*) and if the current
     * asset price is lower than the fundamental value it starts to buy
     * the asset and if the price is higher it starts to sell the asset.
     */
    type FundamentalValue(/** observable fundamental value */
                          fv = .constant(200.)) : FundamentalValueStrategy
    {
        def Fundamental_Value = fv
    }

    /**
      * Mean reversion strategy believes that
      * asset price should return to its average value.
      * It estimates this average using some functional and
      * if the current asset price is lower than the average
      * it buys the asset and if the price is higher it sells the asset.
      */
    type MeanReversion(/** parameter |alpha| for exponentially weighted moving average */
                       alpha = 0.15) : FundamentalValueStrategy
    {
        def Fundamental_Value = book~>MidPrice~>EW(alpha)~>Avg
    }

    /**
      * Dependent price strategy believes that the fair price of an asset *A*
      * is completely correlated with price of another asset *B* and
      * the following relation should be held: *PriceA* = *kPriceB*,
      * where *k* is some factor. It may be considered as a variety of
      * a fundamental value strategy with the exception that it is invoked
      * every the time price of another asset *B* changes.
      */
    type PairTrading(
            /** reference to order book for another asset
              * used to evaluate fair price of our asset */
            bookToDependOn  = .orderbook.OfTrader(),
            /** multiplier to obtain fair asset price from the reference asset price */
            factor          = 1.0) : FundamentalValueStrategy
    {
        def Fundamental_Value = bookToDependOn~>MidPrice * factor
    }

    type RSIbis(/** parameter |alpha| for exponentially weighted moving average when calculating RSI */
                alpha        = 1./14,
                /** lag for calculating up and down movements for RSI */
                timeframe    = 1.,
                /** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */
                threshold    = 30.) : SideStrategy
    {
        def Side = (Signal(50.0 - orderbook.OfTrader()~>MidPrice~>RSI(timeframe, alpha)~>Value,
                           50.0 - threshold))~>S_Side
    }
}