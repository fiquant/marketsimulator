@category = "Side function"
package observable.sidefunc
{
    @python.observable
    def Noise(side_distribution : IFunction[Float] = mathutils.rnd.uniform(0., 1.)) =
        if side_distribution > 0.5 then side.Sell() else side.Buy()

    @python.observable
    def Signal(signal = constant(), threshold = 0.7) =
        if signal >   threshold then side.Buy()  else
        if signal < 0-threshold then side.Sell() else
                                     side.Nothing()

    @python.observable
    def TrendFollower(
        alpha = 0.015,
        threshold = 0.,
        book = orderbook.OfTrader())

        = Signal(Derivative(EW.Avg(orderbook.MidPrice(book), alpha)), threshold)

    @python.observable
    def CrossingAverages(
        alpha_1 = 0.015,
        alpha_2 = 0.15,
        threshold = 0.,
        book = orderbook.OfTrader())

        = Signal(EW.Avg(orderbook.MidPrice(book), alpha_1) - EW.Avg(orderbook.MidPrice(book), alpha_2), threshold)

    @python.observable
    def FundamentalValue(
        fv = constant(200.),
        book = orderbook.OfTrader())

        =   if orderbook.BidPrice(book) > fv then side.Sell() else
            if orderbook.AskPrice(book) < fv then side.Buy()  else
                                                  side.Nothing()

    @python.observable
    def MeanReversion(
        alpha = 0.015,
        book = orderbook.OfTrader())

        =   FundamentalValue(EW.Avg(orderbook.MidPrice(book), alpha), book)

    @python.observable
    def PairTrading(
        dependee = orderbook.OfTrader(),
        factor = constant(1.),
        book = orderbook.OfTrader())

        = FundamentalValue(orderbook.MidPrice(dependee) * factor, book)

}
