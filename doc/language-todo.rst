Possible language improvements
==============================

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Package parameters
------------------

It is not rare to see a lot of boiler plate code in strategies definition that comes from a fact that many functions share a considerable subset of their parameters. For example all liquidity provider related functions (price calculating function, strategy for one side, strategy for two sides) share parameters ``initialValue`` and ``priceDistr`` along with their default values and documentation comments. Liquidity provider strategies also share ``eventGen`` and ``orderFactory`` parameters. We might refactor these into package parameters:

.. code-block:: scala

    package LiquidityProvider(
            /** initial price which is taken if orderBook is empty */
            initialValue = 100.0,
            /** defines multipliers for current asset price when price of
                order to create is calculated*/
            priceDistr   = math.random.lognormvariate(0., .1))
    {
        def Price(  /** side of orders to create */
                    side         = .side.Sell(),
                    /** asset in question */
                    book = orderbook.OfTrader())

            = orderbook.SafeSidePrice(
                    orderbook.Queue(book, side),
                    constant(initialValue)
                ) * priceDistr

        package Strategy(
                    /** Event source making the strategy to wake up*/
                    eventGen     = event.Every(math.random.expovariate(1.)),
                    /** order factory function*/
                    orderFactory = order.side_price.Limit())
        {
            /**
             * Liquidity provider for one side
             */
            def OneSide(/** side of orders to create */
                        side         = .side.Sell())

                =   Generic(
                        orderFactory(side, Price(side)),
                        eventGen)

            /**
             * Liquidity provider for two sides
             */
            def TwoSides()

                =   Array([
                        OneSide(side.Sell()),
                        OneSide(side.Buy())
                    ])

        }
    }

A liquidity provider strategy would be created in this syntax in the following way:

.. code-block :: scala

    lp = LiquidityProvider(200.).Strategy(event.Every(1.)).TwoSides

Note that since arguments are spread into different levels that helps to omit those who have default values.

Package parameters with package inheritance would facilate code reuse. For example variance, standard deviation and relative stardard deviation can be generated automatically for different kinds of moving averages (exponentially weighted, cumulative and simple moving):

.. code-block:: scala

        @category = "Statistics"
        abstract package base
        {
            /**
             *  {{Kind}} moving variance
             */
            @label = "\\sigma^2{{suffix}}"
            def Var (source = const ())

                =   math.Max(0, Avg(Sqr(source)) - Sqr(Avg(source)))

            /**
             *  {{Kind}} moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (source = const ())

                =   Sqrt(Var(source))

            /**
             *  {{Kind}} moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(source = const ())

                = (source - Avg(source)) / StdDev(source)
        }

        @Kind = "Exponentially weighted"
        @suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        package EW(/** alpha parameter */  alpha = 0.015) extends base
        {
            /**
             *  {{Kind}} moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (source = const ()) : IDifferentiable
        }

        @Kind = "Cumulative"
        @suffix = "_{cumul}(%(source)s)"
        package Cumulative
        {
            /**
             *  {{Kind}} moving average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (source = const ()) : IDifferentiable
        }

        @Kind = "Simple"
        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        package Moving(/** sliding window size    */ timeframe = 100.0)
        {
            /**
             *  {{Kind}} moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (source = const ()) : IDifferentiable
        }

Extension methods
-----------------

Object-oriented programmers got used to property-like access to functions: ``obj.propA.propB.f(args)`` instead of ``f(propB(propA(obj)), args)``. To enable this notation a user might mark a parameter to be considered as object base by keyword ``this``:

.. code-block:: scala

    /**
     *  Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(this trader = SingleProxy() : IAccount, alpha = 0.15)
        =   trader.Efficiency.EW(alpha).Avg.Derivative

instead of

.. code-block:: scala

    /**
     *  Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(trader = SingleProxy() : IAccount, alpha = 0.15)
        = math.Derivative(
                math.EW.Avg(
                        Efficiency(trader),
                        alpha)
        )

If multiple functions should be added as extension methods for a type, a special syntax might be used:

.. code-block:: scala

    IOrderQueue {
        /**
         *  Returns best order price of *queue*
         *  Returns None is *queue* is empty
         */
        @python.intrinsic("orderbook.props._BestPrice_Impl")
        def BestPrice : IObservable[Price]
    }

    IOrderBook {
        @python.intrinsic("orderbook.proxy._Queue_Impl")
        def Queue(side = side.Sell()) : IOrderQueue

        @python.intrinsic("orderbook.proxy._Asks_Impl")
        def Asks = Queue(side.Sell())

        @python.intrinsic("orderbook.proxy._Bids_Impl")
        def Bids = Queue(side.Buy())

        def Spread = Asks.Price - Bids.Price
        def MidPrice = (Asks.Price + Bids.Price) / 2.0
    }
