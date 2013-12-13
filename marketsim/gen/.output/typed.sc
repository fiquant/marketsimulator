
package observable {
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        def Avg(source : IObservable = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        def Var(source : IObservable = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        def StdDev(source : IObservable = const()) : () => Float
            
            	 = mathops.Sqrt(observable.Cumulative.Var(source))
    }
    
    package rsi {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source : IObservable = observable.orderbook.MidPrice(),
                timeframe : Float = 10.0,
                alpha : Float = 0.015) : IFunction
            
            	 = observable.EW.Avg(observable.UpMovements(source,timeframe),alpha)/observable.EW.Avg(observable.DownMovements(source,timeframe),alpha)
    }
    
    package macd {
        @python.function("MACD", "MACD_{%(fast)s}^{%(slow)s}(%(x)s)")
        def MACD(x : IObservable = observable.orderbook.MidPrice(),
                 slow : Float = 26.0,
                 fast : Float = 12.0) : IFunction
            
            	 = observable.EW.Avg(x,2.0/(fast+1.0))-observable.EW.Avg(x,2.0/(slow+1.0))
        
        @python.function("MACD", "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Signal(x : IObservable = observable.orderbook.MidPrice(),
                   slow : Float = 26.0,
                   fast : Float = 12.0,
                   timeframe : Float = 9.0,
                   step : Float = 1.0) : () => Float
            
            	 = observable.EW.Avg(observable.OnEveryDt(step,observable.macd.MACD(x,slow,fast)),2.0/(timeframe+1.0))
        
        @python.function("MACD", "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Histogram(x : IObservable = observable.orderbook.MidPrice(),
                      slow : Float = 26.0,
                      fast : Float = 12.0,
                      timeframe : Float = 9.0,
                      step : Float = 1.0) : IFunction
            
            	 = observable.macd.MACD(x,slow,fast)-observable.macd.Signal(x,slow,fast,timeframe,step)
    }
    
    package trader {
        @python.intrinsic.function("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
            
    }
    
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source : IFunction = constant(),
                alpha : Float = 0.015) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source : IObservable = const(),
                alpha : Float = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        def StdDev(source : IObservable = const(),
                   alpha : Float = 0.015) : () => Float
            
            	 = mathops.Sqrt(observable.EW.Var(source,alpha))
    }
    
    package orderbook {
        def PriceAtVolume(queue : IOrderQueue = observable.orderbook.Asks(),
                          volume : Float = 100.0) : () => Float
            
        
        @python.observable("Orderbook", "Price_{%(alpha)s}^{%(queue)s}")
        def WeightedPrice(queue : IOrderQueue = observable.orderbook.Asks(),
                          alpha : Float = 0.015) : IFunction
            
            	 = observable.EW.Avg(observable.orderbook.LastTradePrice(queue)*observable.orderbook.LastTradeVolume(queue),alpha)/observable.EW.Avg(observable.orderbook.LastTradeVolume(queue),alpha)
        
        def TickSize(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskLastPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = observable.orderbook.LastPrice(observable.orderbook.Asks(book))
        
        @python.observable("Orderbook", "Ask_{%(alpha)s}^{%(book)s}")
        def AskWeightedPrice(book : IOrderBook = observable.orderbook.OfTrader(),
                             alpha : Float = 0.015) : IFunction
            
            	 = observable.orderbook.WeightedPrice(observable.orderbook.Asks(book),alpha)
        
        @python.observable("Orderbook", "MidPrice_{%(book)s}")
        def MidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = (observable.orderbook.AskPrice(book)+observable.orderbook.BidPrice(book))/const(2.0)
        
        @python.intrinsic.function("Queue's", "Asks(%(book)s)", "orderbook.queue._Asks_Impl")
        def Asks(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
            
        
        @python.observable("Orderbook", "Bid_{%(alpha)s}^{%(book)s}")
        def BidWeightedPrice(book : IOrderBook = observable.orderbook.OfTrader(),
                             alpha : Float = 0.015) : IFunction
            
            	 = observable.orderbook.WeightedPrice(observable.orderbook.Bids(book),alpha)
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = observable.orderbook.BestPrice(observable.orderbook.Asks(book))
        
        @python.intrinsic.observable("Orderbook", "LastTradeVolume(%(queue)s)", "orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = observable.orderbook.BestPrice(observable.orderbook.Bids(book))
        
        @python.intrinsic.function("Queue's", "Bids(%(book)s)", "orderbook.queue._Bids_Impl")
        def Bids(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
            
        
        @python.intrinsic.observable("Orderbook", "Price(%(queue)s)", "orderbook.props._BestPrice_Impl")
        def BestPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.intrinsic.function("Proxies", "N/A", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IOrderBook
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidLastPrice(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = observable.orderbook.LastPrice(observable.orderbook.Bids(book))
        
        @python.intrinsic.observable("Orderbook", "LastPrice(%(queue)s)", "orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Spread_{%(book)s}")
        def Spread(book : IOrderBook = observable.orderbook.OfTrader()) : IObservable
            
            	 = observable.orderbook.AskPrice(book)-observable.orderbook.BidPrice(book)
        
        @python.intrinsic.observable("Orderbook", "LastTradePrice(%(queue)s)", "orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
    }
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        def Avg(source : IObservable = const(),
                timeframe : Float = 100.0) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{n=%(timeframe)s}(%(source)s)", "moments.mv.MV_Impl")
        def Var(source : IObservable = const(),
                timeframe : Float = 100.0) : IFunction
            
            	 = observable.Max(const(0.0),observable.Moving.Avg(source*source,timeframe)-observable.Sqr(observable.Moving.Avg(source,timeframe)))
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}")
        def StdDev(source : IObservable = const(),
                   timeframe : Float = 100.0) : () => Float
            
            	 = mathops.Sqrt(observable.Moving.Var(source))
    }
    @python.intrinsic.observable("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt : Float = 1.0,
                  x : IFunction = constant()) : IObservable
        
    
    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x : IFunction = constant(),
            y : IFunction = constant()) : IFunction
        
        	 = if x<y then x else y
    
    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source : IObservable = observable.orderbook.MidPrice(),
                      timeframe : Float = 10.0) : IFunction
        
        	 = observable.Max(const(0.0),observable.Lagged(source,timeframe)-source)
    
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged(source : IObservable = const(),
               timeframe : Float = 10.0) : IObservable
        
    
    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x : IFunction = constant(),
            y : IFunction = constant()) : IFunction
        
        	 = if x>y then x else y
    
    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source : IObservable = observable.orderbook.MidPrice(),
                    timeframe : Float = 10.0) : IFunction
        
        	 = observable.Max(const(0.0),source-observable.Lagged(source,timeframe))
    
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x : IFunction = constant()) : IFunction
        
        	 = x*x
    
    @python.observable("RSI", "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)")
    def RSI(book : IOrderBook = observable.orderbook.OfTrader(),
            timeframe : Float = 10.0,
            alpha : Float = 0.015) : IObservable
        
        	 = const(100.0)-const(100.0)/(const(1.0)+observable.rsi.Raw(observable.orderbook.MidPrice(book),timeframe,alpha))
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("Trigonometric", "atan", "atan(%(x)s)")
    def Atan(x : IFunction = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
    def Sqrt(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("Log/Pow", "exp", "e^{%(x)s}")
    def Exp(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("Log/Pow", "log", "log(%(x)s)")
    def Log(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
    def Pow(base : IFunction = constant(1.0),
            power : IFunction = constant(1.0)) : () => Float
        
}

package trash {
    package types {type T
        type R : trash.types.T
        type U : trash.types.T, trash.types.R
        type T1 = trash.types.T
    }
    
    package in1 {
        package in2 {
            def A(x : IFunction = constant(),
                  y : IObservable = if const(3.0)>x+const(2.0) then x else x*const(2.0)) : () => trash.types.T
                
        }
        def A(x : () => trash.types.T1 = trash.A()) : () => trash.types.U
            
    }
    def A(x : () => trash.types.T = trash.in1.in2.A()) : () => trash.types.R
        
}

package mathutils {
    package rnd {
        /** Gamma distribution
         *
         *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         *
         *  The probability distribution function is: ::
         *
         *               x ** (alpha - 1) * math.exp(-x / beta)
         *     pdf(x) =  --------------------------------------
         *                  math.gamma(alpha) * beta ** alpha
         */
        @python.random()
        def gammavariate(Alpha : Float = 1.0,
                         Beta : Float = 1.0) : () => Float
            
        
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu : Float = 0.0,
                          /** |sigma| is the standard deviation */ Sigma : Float = 1.0) : () => Float
            
        
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha : Float = 1.0) : () => Float
            
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        @python.random()
        def triangular(Low : Float = 0.0,
                       High : Float = 1.0,
                       Mode : Float = 0.5) : () => Float
            
        
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu : Float = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa : Float = 0.0) : () => Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low : Float = -10.0,
                    High : Float = 10.0) : () => Float
            
        
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha : Float = 1.0,
                           /** |beta| is the shape parameter  */ Beta : Float = 1.0) : () => Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda : Float = 1.0) : () => Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu : Float = 0.0,
                           Sigma : Float = 1.0) : () => Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha : Float = 1.0,
                        Beta : Float = 1.0) : () => Float
            
    }
}type IOrderQueue
type IOrderBook
type IObservable : IFunction
type IFunction = () => Float
type ISingleAssetTrader
@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x : Float = 1.0) : IObservable
    

@python.function("Basic", "C=%(x)s")
def constant(x : Float = 1.0) : IFunction
    
    	 = const(x)
