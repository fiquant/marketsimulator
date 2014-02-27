package strategy
{
    /**
     * Liquidity provider for one side
     */
    def LiquidityProviderSide(
                /** Event source making the strategy to wake up*/
                eventGen     = event.Every(math.random.expovariate(1.)),
                /** order factory function*/
                orderFactory = order.side_price.Limit(),
                /** side of orders to create */
                side         = .side.Sell() : IFunction[Side],
                /** initial price which is taken if orderBook is empty */
                initialValue = 100.0,
                /** defines multipliers for current asset price when price of
                    order to create is calculated*/
                priceDistr   = math.random.lognormvariate(0., .1))

        =   (orderFactory(
                    side,
                    price.LiquidityProvider(
                        side,
                        initialValue,
                        priceDistr)))~>Strategy(eventGen)

    /**
     * Liquidity provider for two sides
     */
    def LiquidityProvider(
                /** Event source making the strategy to wake up*/
                eventGen     = event.Every(math.random.expovariate(1.)),
                /** order factory function*/
                orderFactory = order.side_price.Limit(),
                /** initial price which is taken if orderBook is empty */
                initialValue = 100.0,
                /** defines multipliers for current asset price when price of
                    order to create is calculated*/
                priceDistr   = math.random.lognormvariate(0., .1))

        =   Array([
                LiquidityProviderSide(eventGen, orderFactory, side.Sell(), initialValue, priceDistr),
                LiquidityProviderSide(eventGen, orderFactory, side.Buy(), initialValue, priceDistr)
            ])

    /**
     *  A Strategy that allows to drive the asset price based on historical market data
     *  by creating large volume orders for the given price.
     *
     *  Every time step of 1 in the simulation corresponds to a 1 day in the market data.
     *
     *  At each time step the previous Limit Buy/Sell orders are cancelled and new ones
     *  are created based on the next price of the market data.
     */
    def MarketData( /** Ticker of the asset */
                    ticker = "^GSPC",
                    /** Start date in DD-MM-YYYY format */
                    start = "2001-1-1",
                    /** End date in DD-MM-YYYY format */
                    end = "2010-1-1",
                    /** Price difference between orders placed and underlying quotes */
                    delta = 1.,
                    /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */
                    volume = 1000.)

    =
    Combine(
            order.price.Limit(side.Sell(), volume*1000)
                ~>FloatingPrice((ticker~>Quote(start, end) + delta)~>BreaksAtChanges)
                ~>Iceberg(volume)
                ~>Strategy(event.After(0.)),

            order.price.Limit(side.Buy(), volume*1000)
                ~>FloatingPrice((ticker~>Quote(start, end) - delta)~>BreaksAtChanges)
                ~>Iceberg(volume)
                ~>Strategy(event.After(0.))
    )

    def MarketMaker(delta = 1., volume = 20.) =

        Combine(
                order.price.Limit(side.Sell(), volume*1000)
                    ~>FloatingPrice(
                        (orderbook.Asks()~>SafeSidePrice(100 + delta) / (trader.Position()~>Atan / 1000)~>Exp)
                            ~>OnEveryDt(0.9)~>BreaksAtChanges)
                    ~>Iceberg(volume)
                    ~>Strategy(event.After(0.)),

                order.price.Limit(side.Buy(), volume*1000)
                    ~>FloatingPrice(
                        (orderbook.Bids()~>SafeSidePrice(100 - delta) / (trader.Position()~>Atan / 1000)~>Exp)
                            ~>OnEveryDt(0.9)~>BreaksAtChanges)
                    ~>Iceberg(volume)
                    ~>Strategy(event.After(0.))
                )


}