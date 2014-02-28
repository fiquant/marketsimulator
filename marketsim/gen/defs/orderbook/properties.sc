@category = "Asset"
package orderbook
{
    /**
     *  Returns order queue of order *book* for trade *side*
     */
    @python.intrinsic("orderbook.proxy._Queue_Impl")
    def Queue(book = OfTrader(), side = side.Sell()) : IOrderQueue

    /**
     *  Returns sell side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Asks_Impl")
    def Asks(book = OfTrader()) = Queue(book, side.Sell())

    /**
     *  Returns buy side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Bids_Impl")
    def Bids(book = OfTrader()) = Queue(book, side.Buy())

    /**
     *  Returns best order price of *queue*
     *  Returns None is *queue* is empty
     */
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    def BestPrice(queue = Asks()) : IObservable[Price]

    /**
     *  Returns last defined price at *queue*
     *  Returns None is *queue* has been always empty
     */
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    def LastPrice(queue = Asks()) : IObservable[Price]

    /**
     *  Returns price of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    def LastTradePrice (queue = Asks()) : IObservable[Price]

    /**
     *  Returns volume of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    def LastTradeVolume(queue = Asks()) : IObservable[Volume]

    /**
     *  Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    @python.observable
    def SafeSidePrice(queue = Asks(),
                      /** price to be used if there haven't been any trades */
                      defaultValue = constant(100.))

        =   queue~>BestPrice~>getOrElse(
                queue~>LastPrice~>getOrElse(
                    defaultValue))

    /**
     *  Returns moving average of trade prices weighted by their volumes
     */
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      /** parameter alpha for the moving average  */
                      alpha = 0.15) =

        (queue~>LastTradePrice * queue~>LastTradeVolume)~>EW(alpha)~>Avg /
                queue~>LastTradeVolume~>EW(alpha)~>Avg

    /**
     *  Returns tick size for the order *book*
     */
    @python.intrinsic("orderbook.props._TickSize_Impl")
    def TickSize(book = OfTrader()) => Price

    /**
     *  Spread of order *book*
     */
    def Spread(book = OfTrader())
        = book~>Asks~>BestPrice - book~>Bids~>BestPrice

    /**
     *  MidPrice of order *book*
     */
    def MidPrice(book = OfTrader())
        = (book~>Asks~>BestPrice + book~>Bids~>BestPrice) / 2.0

    /**
     *  Returns price for best orders of total volume *depth*
     *
     *  In other words cumulative price corresponds to trader balance change
     *  if a market order of volume *depth* is completely matched
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book    = OfTrader(),
                        depth   = constant(1.)) : IObservable[Price]

    /**
     *  Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    def NaiveCumulativePrice(book   = OfTrader(),
                             depth  = constant(1.)) =

            if depth < 0.0 then depth * book~>Asks~>BestPrice else
            if depth > 0.0 then depth * book~>Bids~>BestPrice else
                0.0

    /**
     *  Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]
     *  Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     /** distance between two volumes */
                     volumeDelta = 30.,
                     /** number of volume levels to track */
                     volumeCount = 10) : IObservable[IVolumeLevels]
}

