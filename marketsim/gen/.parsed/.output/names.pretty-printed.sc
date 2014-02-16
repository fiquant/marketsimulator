@category = "Side"

package side() {
    // defined at .output\names.sc: 5.5
    /** Observable always equal to Buy side
     */
    @python.intrinsic.observable("side._Buy_Impl")
    def observableBuy() : .IObservable[.Side]
    
    // defined at .output\names.sc: 10.5
    /** Function always returning None of type Side
     */
    @python.intrinsic("side._None_Impl")
    def Nothing() : () => .Side
    
    // defined at .output\names.sc: 15.5
    /** Function always returning Buy side
     */
    @python.intrinsic("side._Buy_Impl")
    def Buy() : () => .Side
    
    // defined at .output\names.sc: 20.5
    /** Observable always equal to None of type Side
     */
    @python.intrinsic.observable("side._None_Impl")
    def observableNothing() : .IObservable[.Side]
    
    // defined at .output\names.sc: 25.5
    /** Observable always equal to Sell side
     */
    @python.intrinsic.observable("side._Sell_Impl")
    def observableSell() : .IObservable[.Side]
    
    // defined at .output\names.sc: 30.5
    /** Function always returning Sell side
     */
    @python.intrinsic("side._Sell_Impl")
    def Sell() : () => .Side
}
@category = "Event"

package event() {
    // defined at .output\names.sc: 40.5
    /** Event that fires every *intervalFunc* moments of time
     */
    @python.intrinsic("event._Every_Impl")
    def Every(/** interval of time between two events */ intervalFunc = .math.random.expovariate(1.0)) : .IEvent
    
    // defined at .output\names.sc: 45.5
    /** Event that once at *delay*
     */
    @python.intrinsic("event._After_Impl")
    def After(/** when the event should be fired */ delay = .constant(10.0)) : .IEvent
}
@category = "N/A"

package veusz() {
    // defined at .output\names.sc: 55.5
    /** Graph to render at Veusz. Time series are added to it automatically in their constructor
     */
    @python.intrinsic("veusz._Graph_Impl")
    def Graph(name = "graph") : .IGraph
}
@category = "Ops"

package ops() {
    // defined at .output\names.sc: 65.5
    @label = "-%(x)s"
    @python.intrinsic.observable("ops._Negate_Impl")
    def Negate(x = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 69.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "+"
    @python.intrinsic.observable("ops._Add_Impl")
    def Add(x = .constant(1.0),
            y = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 75.5
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    @python.intrinsic.observable("ops._Condition_Impl")
    def Condition(cond = .true(),
                  ifpart = .constant(1.0),
                  elsepart = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 81.5
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    @python.intrinsic.observable("ops._Condition_Impl")
    def Condition(cond = .true(),
                  ifpart = .side.Sell(),
                  elsepart = .side.Buy()) : .IFunction[.Side]
    
    // defined at .output\names.sc: 87.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<"
    @python.intrinsic.observable("ops._Less_Impl")
    def Less(x = .constant(1.0),
             y = .constant(1.0)) : .IFunction[.Boolean]
    
    // defined at .output\names.sc: 93.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "*"
    @python.intrinsic.observable("ops._Mul_Impl")
    def Mul(x = .constant(1.0),
            y = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 99.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<>"
    @python.intrinsic.observable("ops._NotEqual_Impl")
    def NotEqual(x = .constant(1.0),
                 y = .constant(1.0)) : .IFunction[.Boolean]
    
    // defined at .output\names.sc: 105.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">="
    @python.intrinsic.observable("ops._GreaterEqual_Impl")
    def GreaterEqual(x = .constant(1.0),
                     y = .constant(1.0)) : .IFunction[.Boolean]
    
    // defined at .output\names.sc: 111.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "-"
    @python.intrinsic.observable("ops._Sub_Impl")
    def Sub(x = .constant(1.0),
            y = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 117.5
    @label = "\\frac{%(x)s}{%(y)s}"
    @python.intrinsic.observable("ops._Div_Impl")
    def Div(x = .constant(1.0),
            y = .constant(1.0)) : .IFunction[.Float]
    
    // defined at .output\names.sc: 122.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<="
    @python.intrinsic.observable("ops._LessEqual_Impl")
    def LessEqual(x = .constant(1.0),
                  y = .constant(1.0)) : .IFunction[.Boolean]
    
    // defined at .output\names.sc: 128.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "=="
    @python.intrinsic.observable("ops._Equal_Impl")
    def Equal(x = .constant(1.0),
              y = .constant(1.0)) : .IFunction[.Boolean]
    
    // defined at .output\names.sc: 134.5
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">"
    @python.intrinsic.observable("ops._Greater_Impl")
    def Greater(x = .constant(1.0),
                y = .constant(1.0)) : .IFunction[.Boolean]
}
@category = "Basic"

package math() {
    package random() {
        // defined at .output\names.sc: 147.9
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
        def gammavariate(Alpha = 1.0,
                         Beta = 1.0) : () => .Float
        
        // defined at .output\names.sc: 161.9
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu = 0.0,
                          /** |sigma| is the standard deviation */ Sigma = 1.0) : () => .Float
        
        // defined at .output\names.sc: 167.9
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha = 1.0) : () => .Float
        
        // defined at .output\names.sc: 172.9
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        @python.random()
        def triangular(Low = 0.0,
                       High = 1.0,
                       Mode = 0.5) : () => .Float
        
        // defined at .output\names.sc: 185.9
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa = 0.0) : () => .Float
        
        // defined at .output\names.sc: 193.9
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low = -10.0,
                    High = 10.0) : () => .Float
        
        // defined at .output\names.sc: 204.9
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha = 1.0,
                           /** |beta| is the shape parameter  */ Beta = 1.0) : () => .Float
        
        // defined at .output\names.sc: 210.9
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda = 1.0) : () => .Float
        
        // defined at .output\names.sc: 217.9
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu = 0.0,
                           Sigma = 1.0) : () => .Float
        
        // defined at .output\names.sc: 227.9
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha = 1.0,
                        Beta = 1.0) : () => .Float
    }
    @category = "Statistics"
    @suffix = "_{cumul}(%(source)s)"
    
    package Cumulative() {
        // defined at .output\names.sc: 242.9
        /** Cumulative relative standard deviation
         */
        @label = "RSD{{suffix}}"
        def RelStdDev(/** observable data source */ source = .const(1.0)) = (source-.math.Cumulative.Avg(source))/.math.Cumulative.StdDev(source)
        
        // defined at .output\names.sc: 247.9
        /** Cumulative variance
         */
        @python.intrinsic("moments.cmv.Variance_Impl")
        @label = "\\sigma^2{{suffix}}"
        def Var(/** observable data source */ source = .const(1.0)) : () => .Float
        
        // defined at .output\names.sc: 253.9
        /** Cumulative average
         */
        @python.intrinsic("moments.cma.CMA_Impl")
        @label = "Avg{{suffix}}"
        def Avg(/** observable data source */ source = .const(1.0)) : () => .Float
        
        // defined at .output\names.sc: 259.9
        /** Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        def MinEpsilon(/** observable data source */ source = .const(1.0),
                       /** tolerance step         */ epsilon = .constant(0.01)) : .IObservable[.Float]
        
        // defined at .output\names.sc: 268.9
        /** Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        def MaxEpsilon(/** observable data source */ source = .const(1.0),
                       /** tolerance step         */ epsilon = .constant(0.01)) : .IObservable[.Float]
        
        // defined at .output\names.sc: 277.9
        /** Cumulative standard deviation
         */
        @label = "\\sqrt{\\sigma^2{{suffix}}}"
        def StdDev(/** observable data source */ source = .const(1.0)) = .math.Sqrt(.math.Cumulative.Var(source))
    }
    @category = "RSI"
    
    package rsi() {
        // defined at .output\names.sc: 287.9
        /** Absolute value for Relative Strength Index
         */
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(/** observable data source */ source = .const(1.0),
                /** lag size */ timeframe = 10.0,
                /** alpha parameter for EWMA */ alpha = 0.015) = .math.EW.Avg(.math.UpMovements(source,timeframe),alpha)/.math.EW.Avg(.math.DownMovements(source,timeframe),alpha)
    }
    @category = "MACD"
    
    package macd() {
        // defined at .output\names.sc: 299.9
        /** Moving average convergence/divergence
         */
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
        def MACD(/** source */ x = .const(1.0),
                 /** long period */ slow = 26.0,
                 /** short period */ fast = 12.0) = .math.EW.Avg(x,2.0/(fast+1))-.math.EW.Avg(x,2.0/(slow+1))
        
        // defined at .output\names.sc: 306.9
        /** Moving average convergence/divergence signal
         */
        @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Signal(/** source */ x = .const(1.0),
                   /** long period */ slow = 26.0,
                   /** short period */ fast = 12.0,
                   /** signal period */ timeframe = 9.0,
                   /** discretization step */ step = 1.0) = .math.EW.Avg(.observable.OnEveryDt(step,.math.macd.MACD(x,slow,fast)),2/(timeframe+1))
        
        // defined at .output\names.sc: 315.9
        /** Moving average convergence/divergence histogram
         */
        @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Histogram(/** source */ x = .const(1.0),
                      /** long period */ slow = 26.0,
                      /** short period */ fast = 12.0,
                      /** signal period */ timeframe = 9.0,
                      /** discretization step */ step = 1.0) = .math.macd.MACD(x,slow,fast)-.math.macd.Signal(x,slow,fast,timeframe,step)
    }
    @category = "Statistics"
    @suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
    
    package EW() {
        // defined at .output\names.sc: 330.9
        /** Exponentially weighted moving average
         */
        @python.intrinsic("moments.ewma.EWMA_Impl")
        @label = "Avg{{suffix}}"
        def Avg(/** observable data source */ source = .const(1.0),
                /** alpha parameter */ alpha = 0.015) : .IDifferentiable
        
        // defined at .output\names.sc: 337.9
        /** Exponentially weighted moving variance
         */
        @python.intrinsic("moments.ewmv.EWMV_Impl")
        @label = "\\sigma^2{{suffix}}"
        def Var(/** observable data source */ source = .const(1.0),
                /** alpha parameter */ alpha = 0.015) : () => .Float
        
        // defined at .output\names.sc: 344.9
        /** Exponentially weighted moving standard deviation
         */
        @label = "\\sqrt{\\sigma^2{{suffix}}}"
        def StdDev(/** observable data source */ source = .const(1.0),
                   /** alpha parameter */ alpha = 0.015) = .math.Sqrt(.math.EW.Var(source,alpha))
        
        // defined at .output\names.sc: 350.9
        /** Exponentially weighted moving relative standard deviation
         */
        @label = "RSD{{suffix}}"
        def RelStdDev(/** observable data source */ source = .const(1.0),
                      /** alpha parameter */ alpha = 0.015) = (source-.math.EW.Avg(source,alpha))/.math.EW.StdDev(source,alpha)
    }
    @category = "Statistics"
    @suffix = "_{n=%(timeframe)s}(%(source)s)"
    
    package Moving() {
        // defined at .output\names.sc: 362.9
        /** Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        def Min(/** observable data source */ source = .const(1.0),
                /** sliding window size    */ timeframe = 100.0) : .IObservable[.Float]
        
        // defined at .output\names.sc: 369.9
        /** Simple moving relative standard deviation
         */
        @label = "RSD{{suffix}}"
        def RelStdDev(/** observable data source */ source = .const(1.0),
                      /** sliding window size    */ timeframe = 100.0) = (source-.math.Moving.Avg(source,timeframe))/.math.Moving.StdDev(source,timeframe)
        
        // defined at .output\names.sc: 375.9
        /** Simple moving variance
         */
        @python.intrinsic("moments.mv.MV_Impl")
        @label = "\\sigma^2{{suffix}}"
        def Var(/** observable data source */ source = .const(1.0),
                /** sliding window size    */ timeframe = 100.0) = .math.Max(.const(0),.math.Moving.Avg(source*source,timeframe)-.math.Sqr(.math.Moving.Avg(source,timeframe)))
        
        // defined at .output\names.sc: 382.9
        /** Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        def Max(/** observable data source */ source = .const(1.0),
                /** sliding window size    */ timeframe = 100.0) : .IObservable[.Float]
        
        // defined at .output\names.sc: 389.9
        /** Simple moving average
         */
        @python.intrinsic("moments.ma.MA_Impl")
        @label = "Avg{{suffix}}"
        def Avg(/** observable data source */ source = .const(1.0),
                /** sliding window size    */ timeframe = 100.0) : () => .Float
        
        // defined at .output\names.sc: 396.9
        /** Simple moving standard deviation
         */
        @label = "\\sqrt{\\sigma^2{{suffix}}}"
        def StdDev(/** observable data source */ source = .const(1.0),
                   /** sliding window size    */ timeframe = 100.0) = .math.Sqrt(.math.Moving.Var(source))
    }
    
    // defined at .output\names.sc: 404.5
    /** Function returning minimum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @python.observable()
    @label = "min{%(x)s, %(y)s}"
    def Min(x = .constant(1.0),
            y = .constant(1.0)) = if x<y then x else y
    
    // defined at .output\names.sc: 412.5
    /** Returns negative movements of some observable *source* with lag *timeframe*
     */
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(/** observable data source */ source = .const(1.0),
                      /** lag size */ timeframe = 10.0) = .math.Max(0.0,.math.Lagged(source,timeframe)-source)
    
    // defined at .output\names.sc: 418.5
    /** Arc tangent of x, in radians.
     *
     */
    @category = "Trigonometric"
    @python.mathops("atan")
    def Atan(x = .constant(0.0)) : () => .Float
    
    // defined at .output\names.sc: 425.5
    /** Observable that adds a lag to an observable data source so [Lagged(x, dt)]t=t0 == [x]t=t0+dt
     */
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged(/** observable data source */ source = .const(1.0),
               /** lag size */ timeframe = 10.0) : .IObservable[.Float]
    
    // defined at .output\names.sc: 432.5
    /** Function returning maximum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @python.observable()
    @label = "max{%(x)s, %(y)s}"
    def Max(x = .constant(1.0),
            y = .constant(1.0)) = if x>y then x else y
    
    // defined at .output\names.sc: 440.5
    /** Returns positive movements of some observable *source* with lag *timeframe*
     */
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(/** observable data source */ source = .const(1.0),
                    /** lag size */ timeframe = 10.0) = .math.Max(0.0,source-.math.Lagged(source,timeframe))
    
    // defined at .output\names.sc: 446.5
    /** Square of *x*
     */
    @category = "Log/Pow"
    @python.observable()
    @label = "{%(x)s}^2"
    def Sqr(x = .constant(1.0)) = x*x
    
    // defined at .output\names.sc: 453.5
    /** Log returns
     */
    @label = "LogReturns_{%(timeframe)s}(%(x)s)"
    def LogReturns(/** observable data source */ x = .const(1.0),
                   /** lag size */ timeframe = 10.0) = .math.Log(x/.math.Lagged(x,timeframe))
    
    // defined at .output\names.sc: 459.5
    /** Square root of *x*
     *
     */
    @category = "Log/Pow"
    @python.mathops("sqrt")
    @label = "\\sqrt{%(x)s}"
    def Sqrt(x = .constant(1.0)) : () => .Float
    
    // defined at .output\names.sc: 467.5
    /** Relative Strength Index
     */
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(/** asset price in question  */ book = .orderbook.OfTrader(),
            /** lag size */ timeframe = 10.0,
            /** alpha parameter for EWMA */ alpha = 0.015) = 100.0-100.0/(1.0+.math.rsi.Raw(.orderbook.MidPrice(book),timeframe,alpha))
    
    // defined at .output\names.sc: 474.5
    /** Exponent of *x*
     *
     */
    @category = "Log/Pow"
    @python.mathops("exp")
    @label = "e^{%(x)s}"
    def Exp(x = .constant(1.0)) : () => .Float
    
    // defined at .output\names.sc: 482.5
    /** Natural logarithm of *x* (to base e)
     *
     */
    @category = "Log/Pow"
    @python.mathops("log")
    @label = "log(%(x)s)"
    def Log(x = .constant(1.0)) : () => .Float
    
    // defined at .output\names.sc: 490.5
    /** A discrete signal with user-defined increments.
     */
    @python.intrinsic("observable.randomwalk._RandomWalk_Impl")
    @label = "%(name)s"
    def RandomWalk(/** initial value of the signal */ initialValue = 0.0,
                   /** increment function */ deltaDistr = .math.random.normalvariate(0.0,1.0),
                   /** intervals between signal updates */ intervalDistr = .math.random.expovariate(1.0),
                   name = "-random-") : .IObservable[.Float]
    
    // defined at .output\names.sc: 499.5
    /** Function returning first derivative on time of *x*
     * *x* should provide *derivative* member
     */
    @python.intrinsic("observable.derivative._Derivative_Impl")
    @label = "\\frac{d%(x)s}{dt}"
    def Derivative(x = .math.EW.Avg() : .IDifferentiable) : () => .Float
    
    // defined at .output\names.sc: 506.5
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @category = "Log/Pow"
    @python.mathops("pow")
    @label = "%(base)s^{%(power)s}"
    def Pow(base = .constant(1.0),
            power = .constant(1.0)) : () => .Float
}
@category = "Order"

package order() {
    package side() {
        package price() {
            def Limit = .order._curried.side_price_Limit
            
            def ImmediateOrCancel = .order._curried.side_price_ImmediateOrCancel
            
            def StopLoss = .order._curried.side_price_StopLoss
            
            def WithExpiry = .order._curried.side_price_WithExpiry
            
            def FloatingPrice = .order._curried.side_price_FloatingPrice
            
            def Iceberg = .order._curried.side_price_Iceberg
            
            def Peg = .order._curried.side_price_Peg
        }
        
        def Limit = .order._curried.side_Limit
        
        def ImmediateOrCancel = .order._curried.side_ImmediateOrCancel
        
        def Market = .order._curried.side_Market
        
        def StopLoss = .order._curried.side_StopLoss
        
        def WithExpiry = .order._curried.side_WithExpiry
        
        def FloatingPrice = .order._curried.side_FloatingPrice
        
        def Iceberg = .order._curried.side_Iceberg
        
        def FixedBudget = .order._curried.side_FixedBudget
        
        def Peg = .order._curried.side_Peg
    }
    
    package side_price() {
        def Limit = .order._curried.sideprice_Limit
        
        def ImmediateOrCancel = .order._curried.sideprice_ImmediateOrCancel
        
        def StopLoss = .order._curried.sideprice_StopLoss
        
        def WithExpiry = .order._curried.sideprice_WithExpiry
        
        def FloatingPrice = .order._curried.sideprice_FloatingPrice
        
        def Iceberg = .order._curried.sideprice_Iceberg
        
        def Peg = .order._curried.sideprice_Peg
    }
    
    package side_volume() {
        package price() {
            def Limit = .order._curried.sidevolume_price_Limit
            
            def ImmediateOrCancel = .order._curried.sidevolume_price_ImmediateOrCancel
            
            def StopLoss = .order._curried.sidevolume_price_StopLoss
            
            def WithExpiry = .order._curried.sidevolume_price_WithExpiry
            
            def FloatingPrice = .order._curried.sidevolume_price_FloatingPrice
            
            def Iceberg = .order._curried.sidevolume_price_Iceberg
            
            def Peg = .order._curried.sidevolume_price_Peg
        }
        
        def Limit = .order._curried.sidevolume_Limit
        
        def ImmediateOrCancel = .order._curried.sidevolume_ImmediateOrCancel
        
        def Market = .order._curried.sidevolume_Market
        
        def StopLoss = .order._curried.sidevolume_StopLoss
        
        def WithExpiry = .order._curried.sidevolume_WithExpiry
        
        def FloatingPrice = .order._curried.sidevolume_FloatingPrice
        
        def Iceberg = .order._curried.sidevolume_Iceberg
        
        def Peg = .order._curried.sidevolume_Peg
    }
    
    package price() {
        def Limit = .order._curried.price_Limit
        
        def ImmediateOrCancel = .order._curried.price_ImmediateOrCancel
        
        def StopLoss = .order._curried.price_StopLoss
        
        def WithExpiry = .order._curried.price_WithExpiry
        
        def FloatingPrice = .order._curried.price_FloatingPrice
        
        def Iceberg = .order._curried.price_Iceberg
        
        def Peg = .order._curried.price_Peg
    }
    
    package signed() {
        def Limit = .order.LimitSigned
        
        def Market = .order.MarketSigned
    }
    
    package signedVolume() {
        def LimitSigned = .order._curried.signedVolume_LimitSigned
        
        def MarketSigned = .order._curried.signedVolume_MarketSigned
    }
    
    package _curried() {
        // defined at .output\names.sc: 657.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("ImmediateOrCancel")
        def side_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.side.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 669.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("price_Limit")
        def volume_price_Limit(/** function defining side of orders to create */ side = .side.Sell()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 678.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("Iceberg")
        def sidevolume_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                               /** underlying orders to create */ proto = .order.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 688.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("WithExpiry")
        def sidevolume_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                                  /** underlying orders to create */ proto = .order.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 697.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("price_StopLoss")
        def side_price_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                                /** underlying orders to create */ proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 708.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("Iceberg")
        def price_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                          /** underlying orders to create */ proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 718.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("FloatingPrice")
        def sideprice_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                    /** underlying orders to create */ proto = .order.side.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 728.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("StopLoss")
        def price_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                           /** underlying orders to create */ proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 739.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("ImmediateOrCancel")
        def price_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 751.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("price_WithExpiry")
        def volume_price_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                                    /** underlying orders to create */ proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 760.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("StopLoss")
        def sideprice_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                               /** underlying orders to create */ proto = .order.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 771.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("price_Peg")
        def volume_price_Peg(proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 781.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("Iceberg")
        def side_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                         /** underlying orders to create */ proto = .order.side.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 791.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("price_WithExpiry")
        def sidevolume_price_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                                        /** underlying orders to create */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 800.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("Peg")
        def volume_Peg(proto = .order.volume.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 810.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sidevolume_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 822.9
        /** Factory creating fixed budget orders
         *
         *  Fixed budget order acts like a market order
         *  but the volume is implicitly given by a budget available for trades.
         *  Internally first it sends request.EvalVolumesForBudget
         *  to estimate volumes and prices of orders to sent and
         *  then sends a sequence of order.ImmediateOrCancel to be sure that
         *  cumulative price of trades to be done won't exceed the given budget.
         */
        @python.order.factory.curried("FixedBudget")
        def side_FixedBudget(/** function defining budget on which it may send orders at one time */ budget = .constant(1000.0)) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 834.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("Limit")
        def sideprice_Limit(/** function defining volume of orders to create */ volume = .constant(1.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 843.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("Peg")
        def sideprice_Peg(proto = .order.side.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 853.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("Peg")
        def sidevolume_Peg(proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 863.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("Peg")
        def side_Peg(proto = .order.side.price.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 873.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("LimitSigned")
        def signedVolume_LimitSigned(/** function defining price of orders to create */ price = .constant(100.0)) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 882.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("price_Iceberg")
        def side_price_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                               /** underlying orders to create */ proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 892.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def side_price_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 904.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("WithExpiry")
        def side_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                            /** underlying orders to create */ proto = .order.side.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 913.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("StopLoss")
        def side_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                          /** underlying orders to create */ proto = .order.side.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 924.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("price_StopLoss")
        def sidevolume_price_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                                      /** underlying orders to create */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 935.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("Peg")
        def price_Peg(proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 945.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("StopLoss")
        def volume_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                            /** underlying orders to create */ proto = .order.volume.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 956.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("price_Limit")
        def sidevolume_price_Limit() : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 965.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("StopLoss")
        def sidevolume_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                                /** underlying orders to create */ proto = .order.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 976.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("WithExpiry")
        def volume_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                              /** underlying orders to create */ proto = .order.volume.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 985.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("WithExpiry")
        def sideprice_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                                 /** underlying orders to create */ proto = .order.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 994.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("ImmediateOrCancel")
        def volume_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.volume.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1006.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("FloatingPrice")
        def volume_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                 /** underlying orders to create */ proto = .order.volume.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1016.9
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        @python.order.factory.curried("Market")
        def volume_Market(/** function defining side of orders to create */ side = .side.Sell()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1023.9
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        @python.order.factory.on_proto("price_StopLoss")
        def volume_price_StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                                  /** underlying orders to create */ proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1034.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def volume_price_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1046.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("Limit")
        def side_Limit(/** function defining price of orders to create */ price = .constant(100.0),
                       /** function defining volume of orders to create */ volume = .constant(1.0)) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 1056.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("price_FloatingPrice")
        def side_price_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                     /** underlying orders to create */ proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1066.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("FloatingPrice")
        def side_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                               /** underlying orders to create */ proto = .order.side.price.Limit()) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 1076.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("price_WithExpiry")
        def side_price_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                                  /** underlying orders to create */ proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1085.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("price_Limit")
        def side_price_Limit(/** function defining volume of orders to create */ volume = .constant(1.0)) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1094.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("Iceberg")
        def volume_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                           /** underlying orders to create */ proto = .order.volume.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1104.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("price_FloatingPrice")
        def volume_price_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                       /** underlying orders to create */ proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1114.9
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        @python.order.factory.curried("Market")
        def side_Market(/** function defining volume of orders to create */ volume = .constant(1.0)) : (() => .Side) => .IOrderGenerator
        
        // defined at .output\names.sc: 1121.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("FloatingPrice")
        def price_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                /** underlying orders to create */ proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1131.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("FloatingPrice")
        def sidevolume_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                     /** underlying orders to create */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 1141.9
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        @python.order.factory.on_proto("WithExpiry")
        def price_WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                             /** underlying orders to create */ proto = .order.price.Limit()) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1150.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("price_Iceberg")
        def volume_price_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                                 /** underlying orders to create */ proto = .order.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1160.9
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        @python.order.factory.on_proto("price_FloatingPrice")
        def sidevolume_price_FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                                           /** underlying orders to create */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1170.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def sidevolume_price_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1182.9
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        @python.order.factory.curried("Market")
        def sidevolume_Market() : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 1189.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("Limit")
        def price_Limit(/** function defining side of orders to create */ side = .side.Sell(),
                        /** function defining volume of orders to create */ volume = .constant(1.0)) : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1199.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("Limit")
        def sidevolume_Limit(/** function defining price of orders to create */ price = .constant(100.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 1208.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("Iceberg")
        def sideprice_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                              /** underlying orders to create */ proto = .order.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 1218.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("price_Peg")
        def sidevolume_price_Peg(proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1228.9
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        @python.order.factory.curried("MarketSigned")
        def signedVolume_MarketSigned() : (() => .Float) => .IOrderGenerator
        
        // defined at .output\names.sc: 1235.9
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sideprice_ImmediateOrCancel(/** factory for underlying orders */ proto = .order.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
        
        // defined at .output\names.sc: 1247.9
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        @python.order.factory.on_proto("price_Peg")
        def side_price_Peg(proto = .order.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1257.9
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        @python.order.factory.on_proto("price_Iceberg")
        def sidevolume_price_Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                                     /** underlying orders to create */ proto = .order.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
        
        // defined at .output\names.sc: 1267.9
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        @python.order.factory.curried("Limit")
        def volume_Limit(/** function defining side of orders to create */ side = .side.Sell(),
                         /** function defining price of orders to create */ price = .constant(100.0)) : (() => .Float) => .IOrderGenerator
    }
    
    package volume() {
        package price() {
            def Limit = .order._curried.volume_price_Limit
            
            def ImmediateOrCancel = .order._curried.volume_price_ImmediateOrCancel
            
            def StopLoss = .order._curried.volume_price_StopLoss
            
            def WithExpiry = .order._curried.volume_price_WithExpiry
            
            def FloatingPrice = .order._curried.volume_price_FloatingPrice
            
            def Iceberg = .order._curried.volume_price_Iceberg
            
            def Peg = .order._curried.volume_price_Peg
        }
        
        def Limit = .order._curried.volume_Limit
        
        def ImmediateOrCancel = .order._curried.volume_ImmediateOrCancel
        
        def Market = .order._curried.volume_Market
        
        def StopLoss = .order._curried.volume_StopLoss
        
        def WithExpiry = .order._curried.volume_WithExpiry
        
        def FloatingPrice = .order._curried.volume_FloatingPrice
        
        def Iceberg = .order._curried.volume_Iceberg
        
        def Peg = .order._curried.volume_Peg
    }
    
    // defined at .output\names.sc: 1317.5
    /** Factory creating limit orders
     *
     *  Limit orders ask to buy or sell some asset at price better than some limit price.
     *  If a limit order is not competely fulfilled
     *  it remains in an order book waiting to be matched with another order.
     */
    @python.order.factory("order.limit.Order_Impl")
    def Limit(/** function defining side of orders to create */ side = .side.Sell(),
              /** function defining price of orders to create */ price = .constant(100.0),
              /** function defining volume of orders to create */ volume = .constant(1.0)) : .IOrderGenerator
    
    // defined at .output\names.sc: 1328.5
    /** Factory creating market orders
     *
     *  Market order intructs buy or sell given volume immediately
     */
    @python.order.factory("order.market.Order_Impl")
    def MarketSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0)) : .IOrderGenerator
    
    // defined at .output\names.sc: 1335.5
    /** Factory creating Immediate-Or-Cancel orders
     *
     *  Immediate-Or-Cancel order sends an underlying order to the market and
     *  immediately sends a cancel request for it.
     *  It allows to combine market and limit order behaviour:
     *  the order is either executed immediately
     *  at price equal or better than given one
     *  either it is cancelled (and consequently never stored in the order queue).
     */
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(/** factory for underlying orders */ proto = .order.Limit()) : .IOrderGenerator
    
    // defined at .output\names.sc: 1347.5
    /** Factory creating market orders
     *
     *  Market order intructs buy or sell given volume immediately
     */
    @python.order.factory("order.market.Order_Impl")
    def Market(/** function defining side of orders to create */ side = .side.Sell(),
               /** function defining volume of orders to create */ volume = .constant(1.0)) : .IOrderGenerator
    
    // defined at .output\names.sc: 1355.5
    /** Factory creating StopLoss orders
     *
     *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
     *  It keeps track of position and balance change induced by trades of the underlying order and
     *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
     *  the meta order clears its position.
     */
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(/** maximal acceptable loss factor */ maxloss = .constant(0.1),
                 /** underlying orders to create */ proto = .order.Limit()) : .IOrderGenerator
    
    // defined at .output\names.sc: 1366.5
    /** Factory creating WithExpiry orders
     *
     * WithExpiry orders can be viewed as ImmediateOrCancel orders
     * where cancel order is sent not immediately but after some delay
     */
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(/** expiration period for orders */ expiry = .constant(10.0),
                   /** underlying orders to create */ proto = .order.Limit()) : .IOrderGenerator
    
    // defined at .output\names.sc: 1375.5
    /** Factory creating orders with floating price
     *
     *  Floating price order is initialized by an order having a price and an observable that generates new prices.
     *  When the observable value changes the order is cancelled and
     *  a new order with new price is created and sent to the order book.
     */
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(/** observable defining price of orders to create */ floatingPrice = .const(10.0),
                      /** underlying orders to create */ proto = .order.price.Limit()) : .IOrderGenerator
    
    // defined at .output\names.sc: 1385.5
    /** Factory creating iceberg orders
     *
     *  Iceberg order is initialized by an underlying order and a lot size.
     *  It sends consequently pieces of the underlying order of size equal or less to the lot size
     *  thus maximum lot size volume is visible at the market at any moment.
     */
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(/** maximal size of order to send */ lotSize = .constant(10.0),
                /** underlying orders to create */ proto = .order.Limit()) : .IOrderGenerator
    
    // defined at .output\names.sc: 1395.5
    /** Factory creating fixed budget orders
     *
     *  Fixed budget order acts like a market order
     *  but the volume is implicitly given by a budget available for trades.
     *  Internally first it sends request.EvalVolumesForBudget
     *  to estimate volumes and prices of orders to sent and
     *  then sends a sequence of order.ImmediateOrCancel to be sure that
     *  cumulative price of trades to be done won't exceed the given budget.
     */
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(/** function defining side of orders to create */ side = .side.Sell(),
                    /** function defining budget on which it may send orders at one time */ budget = .constant(1000.0)) : .IOrderGenerator
    
    // defined at .output\names.sc: 1408.5
    /** Factory creating limit orders
     *
     *  Limit orders ask to buy or sell some asset at price better than some limit price.
     *  If a limit order is not competely fulfilled
     *  it remains in an order book waiting to be matched with another order.
     */
    @python.order.factory("order.limit.Order_Impl")
    def LimitSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0),
                    /** function defining price of orders to create */ price = .constant(100.0)) : .IOrderGenerator
    
    // defined at .output\names.sc: 1418.5
    /** Factory creating Peg orders
     *
     *  A peg order is a particular case of the floating price order
     *  with the price better at one tick than the best price of the order queue.
     *  It implies that if several peg orders are sent to the same order queue
     *  they start to race until being matched against the counterparty orders.
     */
    @python.order.factory("order.meta.peg.Factory_Impl")
    def Peg(proto = .order.price.Limit()) : .IOrderGenerator
}
@category = "Strategy"

package strategy() {@category = "Side function"
    
    package side() {
        // defined at .output\names.sc: 1436.9
        /** Side function for pair trading strategy
         */
        def PairTrading(/** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn = .orderbook.OfTrader(),
                        /** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0,
                        /** asset in question */ book = .orderbook.OfTrader()) = .strategy.side.FundamentalValue(.orderbook.MidPrice(bookToDependOn)*factor,book)
        
        // defined at .output\names.sc: 1442.9
        /** Side function for signal strategy
         */
        @python.observable()
        def Signal(/** signal to be listened to */ signal = .constant(0.0),
                   /** threshold when the trader starts to act */ threshold = 0.7) = if signal>threshold then .side.Buy() else if signal<0-threshold then .side.Sell() else .side.Nothing()
        
        // defined at .output\names.sc: 1448.9
        /** Side function for crossing averages strategy
         */
        def CrossingAverages(/** parameter |alpha| for exponentially weighted moving average 1 */ alpha_1 = 0.15,
                             /** parameter |alpha| for exponentially weighted moving average 2 */ alpha_2 = 0.015,
                             /** threshold when the trader starts to act */ threshold = 0.0,
                             /** asset in question */ book = .orderbook.OfTrader()) = .strategy.side.Signal(.math.EW.Avg(.orderbook.MidPrice(book),alpha_1)-.math.EW.Avg(.orderbook.MidPrice(book),alpha_2),threshold)
        
        // defined at .output\names.sc: 1455.9
        /** Side function for trend follower strategy
         */
        def TrendFollower(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.15,
                          /** threshold when the trader starts to act */ threshold = 0.0,
                          /** asset in question */ book = .orderbook.OfTrader()) = .strategy.side.Signal(.math.Derivative(.math.EW.Avg(.orderbook.MidPrice(book),alpha)),threshold)
        
        // defined at .output\names.sc: 1461.9
        /** Side function for fundamental value strategy
         */
        @python.observable()
        def FundamentalValue(/** observable fundamental value */ fv = .constant(200.0),
                             /** asset in question */ book = .orderbook.OfTrader()) = if .orderbook.bid.Price(book)>fv then .side.Sell() else if .orderbook.ask.Price(book)<fv then .side.Buy() else .side.Nothing()
        
        // defined at .output\names.sc: 1467.9
        /** Side function for mean reversion strategy
         */
        def MeanReversion(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.015,
                          /** asset in question */ book = .orderbook.OfTrader()) = .strategy.side.FundamentalValue(.math.EW.Avg(.orderbook.MidPrice(book),alpha),book)
        
        // defined at .output\names.sc: 1472.9
        /** Side function for a noise trading strategy
         */
        def Noise(side_distribution = .math.random.uniform(0.0,1.0)) = if side_distribution>0.5 then .side.Sell() else .side.Buy()
    }
    
    package weight() {
        package array() {
            // defined at .output\names.sc: 1482.13
            /** Function returning an array of length *len(array)*
             *  having 1 at the index of the maximal element and 0 are at the rest
             */
            @python.curried("ChooseTheBest")
            def array_ChooseTheBest() : .Optional[.List[.Float]] => .List[.Float]
            
            // defined at .output\names.sc: 1488.13
            /** Identity function for an array of floats
             */
            @python.curried("IdentityL")
            def array_IdentityL() : .Optional[.List[.Float]] => .List[.Float]
        }
        
        package trader() {
            // defined at .output\names.sc: 1497.13
            /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
             */
            @python.curried("Efficiency")
            def trader_Efficiency() : .IAccount => .IFunction[.Float]
            
            // defined at .output\names.sc: 1502.13
            /** Calculates how many times efficiency of trader went up and went down
             * Returns difference between them.
             *
             * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
             */
            @python.curried("Score")
            def trader_Score() : .IAccount => .IFunction[.Float]
            
            // defined at .output\names.sc: 1510.13
            /** Returns first derivative of a moving average of the trader efficiency
             */
            @python.curried("EfficiencyTrend")
            def trader_EfficiencyTrend(/** parameter alpha for the moving average */ alpha = 0.15) : .IAccount => .IFunction[.Float]
            
            // defined at .output\names.sc: 1515.13
            /** Unit function. Used to simulate uniform random choice of a strategy
             */
            @python.curried("Unit")
            def trader_Unit() : .IAccount => .IFunction[.Float]
        }
        
        package f() {
            // defined at .output\names.sc: 1524.13
            /** scaling function = max(0, f(x)) + 1
             */
            @python.curried("Clamp0")
            def f_Clamp0() : .Optional[.IFunction[.Float]] => .IFunction[.Float]
            
            // defined at .output\names.sc: 1529.13
            /** scaling function = atan(base^f(x))
             */
            @python.curried("AtanPow")
            def f_AtanPow(/** base for power function */ base = 1.002) : .Optional[.IFunction[.Float]] => .IFunction[.Float]
            
            // defined at .output\names.sc: 1534.13
            /** identity scaling = f(x)
             */
            @python.curried("IdentityF")
            def f_IdentityF() : .Optional[.IFunction[.Float]] => .IFunction[.Float]
        }
        
        def efficiency = .strategy.weight.trader.trader_Efficiency
        
        // defined at .output\names.sc: 1543.9
        /** Function returning an array of length *len(array)*
         *  having 1 at the index of the maximal element and 0 are at the rest
         */
        @python.intrinsic("strategy.weight._ChooseTheBest_Impl")
        @curried("array")
        def ChooseTheBest(array : .Optional[.List[.Float]] = []) : .List[.Float]
        
        def chooseTheBest = .strategy.weight.array.array_ChooseTheBest
        
        def score = .strategy.weight.trader.trader_Score
        
        def identityL = .strategy.weight.array.array_IdentityL
        
        // defined at .output\names.sc: 1556.9
        /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
         */
        @curried("trader")
        def Efficiency(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float] = .trader.Efficiency(trader)
        
        def efficiencyTrend = .strategy.weight.trader.trader_EfficiencyTrend
        
        def clamp0 = .strategy.weight.f.f_Clamp0
        
        // defined at .output\names.sc: 1565.9
        /** Calculates how many times efficiency of trader went up and went down
         * Returns difference between them.
         *
         * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
         */
        @python.intrinsic("strategy.weight._Score_Impl")
        @curried("trader")
        def Score(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float]
        
        // defined at .output\names.sc: 1574.9
        /** scaling function = max(0, f(x)) + 1
         */
        @curried("f")
        def Clamp0(/** function to scale */ f : .Optional[.IFunction[.Float]] = .constant(1.0)) : .IFunction[.Float] = .math.Max(0,f)+1
        
        def identityF = .strategy.weight.f.f_IdentityF
        
        // defined at .output\names.sc: 1581.9
        /** Returns first derivative of a moving average of the trader efficiency
         */
        @curried("trader")
        def EfficiencyTrend(/** account in question */ trader : .IAccount = .trader.SingleProxy(),
                            /** parameter alpha for the moving average */ alpha = 0.15) : .IFunction[.Float] = .math.Derivative(.math.EW.Avg(.trader.Efficiency(trader),alpha))
        
        def atanPow = .strategy.weight.f.f_AtanPow
        
        def unit = .strategy.weight.trader.trader_Unit
        
        // defined at .output\names.sc: 1591.9
        /** Unit function. Used to simulate uniform random choice of a strategy
         */
        @curried("trader")
        def Unit(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float] = .constant(1.0)
        
        // defined at .output\names.sc: 1596.9
        /** scaling function = atan(base^f(x))
         */
        @curried("f")
        def AtanPow(/** function to scale */ f : .Optional[.IFunction[.Float]] = .constant(1.0),
                    /** base for power function */ base = 1.002) : .IFunction[.Float] = .math.Atan(.math.Pow(base,f))
        
        // defined at .output\names.sc: 1602.9
        /** Identity function for an array of floats
         */
        @python.intrinsic("strategy.weight._Identity_Impl")
        @curried("array")
        def IdentityL(array : .Optional[.List[.Float]] = []) : .List[.Float]
        
        // defined at .output\names.sc: 1608.9
        /** identity scaling = f(x)
         */
        @curried("f")
        def IdentityF(f : .Optional[.IFunction[.Float]] = .constant(1.0)) : .IFunction[.Float] = f
    }
    
    package lp() {
        // defined at .output\names.sc: 1617.9
        /** Liquidity provider for one side
         */
        def OneSide(/** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                    /** defines multipliers for current asset price when price of
                      *                    order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1),
                    /** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                    /** order factory function*/ orderFactory = .order.side_price.Limit(),
                    /** side of orders to create */ side = .side.Sell() : .IFunction[.Side]) = .strategy.Generic(orderFactory(side,.strategy.price.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
        
        // defined at .output\names.sc: 1626.9
        /** Liquidity provider for two sides
         */
        def TwoSide(/** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                    /** defines multipliers for current asset price when price of
                      *                    order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1),
                    /** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                    /** order factory function*/ orderFactory = .order.side_price.Limit()) = .strategy.Array([.strategy.lp.OneSide(initialValue,priceDistr,eventGen,orderFactory,.side.Sell()),.strategy.lp.OneSide(initialValue,priceDistr,eventGen,orderFactory,.side.Buy())])
    }
    @category = "Price function"
    
    package price() {
        // defined at .output\names.sc: 1639.9
        /** Price function for a liquidity provider strategy
         */
        def LiquidityProvider(/** side of orders to create */ side = .side.Sell() : .IFunction[.Side],
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *             order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1),
                              /** asset in question */ book = .orderbook.OfTrader()) = .orderbook.SafeSidePrice(.orderbook.Queue(book,side),initialValue)*priceDistr
    }
    @category = "Volume function"
    
    package position() {
        // defined at .output\names.sc: 1652.9
        /** Position function for desired position strategy
         */
        def DesiredPosition(/** observable desired position */ desiredPosition = .const(1.0),
                            /** trader in question */ trader = .trader.SingleProxy()) = desiredPosition-.trader.Position(trader)-.trader.PendingVolume(trader)
        
        // defined at .output\names.sc: 1657.9
        /** Position function for Bollinger bands strategy with linear scaling
         */
        def Bollinger_linear(/** alpha parameter for exponentially weighted moving everage and variance */ alpha = 0.15,
                             /** observable scaling function that maps relative deviation to desired position */ k = .const(0.5),
                             /** trader in question */ trader = .trader.SingleProxy()) = .strategy.position.DesiredPosition(.observable.OnEveryDt(1.0,.math.EW.RelStdDev(.orderbook.MidPrice(.orderbook.OfTrader(trader)),alpha)*k),trader)
        
        // defined at .output\names.sc: 1663.9
        /** Position function for Relative Strength Index strategy with linear scaling
         */
        def RSI_linear(/** alpha parameter for exponentially moving averages of up movements and down movements */ alpha = 1.0/14.0,
                       /** observable scaling function that maps RSI deviation from 50 to the desired position */ k = .const(-0.04),
                       /** lag for calculating up and down movements */ timeframe = 1.0,
                       /** trader in question */ trader = .trader.SingleProxy()) = .strategy.position.DesiredPosition(.observable.OnEveryDt(1.0,(50.0-.math.RSI(.orderbook.OfTrader(trader),timeframe,alpha))*k),trader)
    }
    
    package account() {
        package inner() {
            // defined at .output\names.sc: 1676.13
            /** Associated with a strategy account that tracks
             *  how orders sent by the strategy have been actually traded
             */
            @python.curried("Real")
            def inner_Real() : .Optional[.ISingleAssetStrategy] => .IAccount
            
            // defined at .output\names.sc: 1682.13
            /** Associated with a strategy account that evaluates for every order sent by the strategy
             *  how it would be traded by sending request.evalMarketOrder
             *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
             *  but we want evaluate in any case would it be profitable or not)
             */
            @python.curried("VirtualMarket")
            def inner_VirtualMarket() : .Optional[.ISingleAssetStrategy] => .IAccount
        }
        
        // defined at .output\names.sc: 1692.9
        /** Associated with a strategy account that tracks
         *  how orders sent by the strategy have been actually traded
         */
        @python.intrinsic("strategy.account._Account_Impl")
        @curried("inner")
        def Real(/** strategy to track */ inner : .Optional[.ISingleAssetStrategy] = .strategy.Noise()) : .IAccount
        
        // defined at .output\names.sc: 1699.9
        /** Associated with a strategy account that evaluates for every order sent by the strategy
         *  how it would be traded by sending request.evalMarketOrder
         *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
         *  but we want evaluate in any case would it be profitable or not)
         */
        @python.intrinsic("strategy.account._VirtualMarket_Impl")
        @curried("inner")
        def VirtualMarket(/** strategy to track */ inner : .Optional[.ISingleAssetStrategy] = .strategy.Noise()) : .IAccount
        
        def real = .strategy.account.inner.inner_Real
        
        def virtualMarket = .strategy.account.inner.inner_VirtualMarket
    }
    
    // defined at .output\names.sc: 1714.5
    /** Creates a strategy combining two strategies
     *  Can be considered as a particular case of Array strategy
     */
    @python.intrinsic("strategy.combine._Combine_Impl")
    def Combine(A = .strategy.Noise(),
                B = .strategy.Noise()) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1721.5
    /** Strategy believing that trader position should be proportional to 50 - RSI(asset)
     */
    def RSI_linear(/** order factory function */ orderFactory = .order.signedVolume.MarketSigned(),
                   /** alpha parameter for exponentially moving averages of up movements and down movements */ alpha = 1.0/14,
                   /** observable scaling function that maps RSI deviation from 50 to the desired position */ k = .const(-0.04),
                   /** lag for calculating up and down movements */ timeframe = 1.0) = .strategy.Generic(orderFactory(.strategy.position.RSI_linear(alpha,k,timeframe)))
    
    // defined at .output\names.sc: 1728.5
    /** Dependent price strategy believes that the fair price of an asset *A*
     * is completely correlated with price of another asset *B* and the following relation
     * should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     * It may be considered as a variety of a fundamental value strategy
     * with the exception that it is invoked every the time price of another
     * asset *B* changes.
     */
    def PairTrading(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                    /** order factory function*/ orderFactory = .order.side.Market(),
                    /** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn = .orderbook.OfTrader(),
                    /** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0) = .strategy.Generic(orderFactory(.strategy.side.PairTrading(bookToDependOn,factor)),eventGen)
    
    // defined at .output\names.sc: 1740.5
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * It can be considered as a particular case for MultiArmedBandit strategy with
     * *corrector* parameter set to *chooseTheBest*
     */
    @python.intrinsic("strategy.choose_the_best._ChooseTheBest_Impl")
    def ChooseTheBest(/** original strategies that can be suspended */ strategies = [.strategy.Noise()],
                      /** function creating phantom strategy used for efficiency estimation */ account = .strategy.account.virtualMarket(),
                      /** function estimating is the strategy efficient or not */ performance = .strategy.weight.efficiencyTrend()) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1751.5
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    def Signal(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
               /** order factory function*/ orderFactory = .order.side.Market(),
               /** signal to be listened to */ signal = .constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7) = .strategy.Generic(orderFactory(.strategy.side.Signal(signal,threshold)),eventGen)
    
    // defined at .output\names.sc: 1760.5
    /** Liquidity provider for two sides
     */
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                          /** order factory function*/ orderFactory = .order.side_price.Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1)) = .strategy.Array([.strategy.LiquidityProviderSide(eventGen,orderFactory,.side.Sell(),initialValue,priceDistr),.strategy.LiquidityProviderSide(eventGen,orderFactory,.side.Buy(),initialValue,priceDistr)])
    
    // defined at .output\names.sc: 1768.5
    /** Two averages strategy compares two averages of price of the same asset but
     * with different parameters ('slow' and 'fast' averages) and when
     * the first is greater than the second one it buys,
     * when the first is lower than the second one it sells
     */
    def CrossingAverages(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                         /** order factory function*/ orderFactory = .order.side.Market(),
                         /** parameter |alpha| for exponentially weighted moving average 1 */ ewma_alpha_1 = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ ewma_alpha_2 = 0.015,
                         /** threshold when the trader starts to act */ threshold = 0.0) = .strategy.Generic(orderFactory(.strategy.side.CrossingAverages(ewma_alpha_1,ewma_alpha_2,threshold)),eventGen)
    
    // defined at .output\names.sc: 1779.5
    /** Strategy that wraps another strategy and passes its orders only if *predicate* is true
     */
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(/** wrapped strategy */ inner = .strategy.Noise(),
                    /** predicate to evaluate */ predicate = .true()) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1785.5
    /** Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    def TrendFollower(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                      /** order factory function*/ orderFactory = .order.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15,
                      /** threshold when the trader starts to act */ threshold = 0.0) = .strategy.Generic(orderFactory(.strategy.side.TrendFollower(ewma_alpha,threshold)),eventGen)
    
    // defined at .output\names.sc: 1797.5
    /** Fundamental value strategy believes that an asset should have some specific price
     * (*fundamental value*) and if the current asset price is lower than the fundamental value
     * it starts to buy the asset and if the price is higher it starts to sell the asset.
     */
    def FundamentalValue(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                         /** order factory function*/ orderFactory = .order.side.Market(),
                         /** defines fundamental value */ fundamentalValue = .constant(100.0)) = .strategy.Generic(orderFactory(.strategy.side.FundamentalValue(fundamentalValue)),eventGen)
    
    // defined at .output\names.sc: 1805.5
    /** Strategy for a multi asset trader.
     * It believes that these assets represent a single asset traded on different venues
     * Once an ask at one venue becomes lower than a bid at another venue
     * it sends market sell and buy orders in order to exploit this arbitrage possibility
     */
    @python.intrinsic("strategy.arbitrage._Arbitrage_Impl")
    def Arbitrage() : .IMultiAssetStrategy
    
    // defined at .output\names.sc: 1813.5
    /** Strategy that calculates Relative Strength Index of an asset
     *  and starts to buy when RSI is greater than 50 + *threshold*
     *  and sells when RSI is less than 50 - *thresold*
     */
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
               /** order factory function*/ orderFactory = .order.side.Market(),
               /** parameter |alpha| for exponentially weighted moving average when calculating RSI */ alpha = 1.0/14,
               /** lag for calculating up and down movements for RSI */ timeframe = 1.0,
               /** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */ threshold = 30.0) = .strategy.Generic(orderFactory(.strategy.side.Signal(50.0-.math.RSI(.orderbook.OfTrader(),timeframe,alpha),50.0-threshold)),eventGen)
    
    // defined at .output\names.sc: 1823.5
    /** Adaptive strategy that evaluates *inner* strategy efficiency and if it is considered as good, sends orders
     */
    def TradeIfProfitable(/** wrapped strategy */ inner = .strategy.Noise(),
                          /** defines how strategy trades are booked: actually traded amount or virtual market orders are
                            * used in order to estimate how the strategy would have traded if all her orders appear at market */ account = .strategy.account.virtualMarket(),
                          /** given a trading account tells should it be considered as effective or not */ performance = .strategy.weight.efficiencyTrend()) = .strategy.Suspendable(inner,performance(account(inner))>=0)
    
    // defined at .output\names.sc: 1830.5
    /** Creates a strategy combining an array of strategies
     */
    @python.intrinsic("strategy.combine._Array_Impl")
    def Array(/** strategies to combine */ strategies = [.strategy.Noise()]) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1835.5
    /** Mean reversion strategy believes that asset price should return to its average value.
     * It estimates this average using some functional and
     * if the current asset price is lower than the average
     * it buys the asset and if the price is higher it sells the asset.
     */
    def MeanReversion(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                      /** order factory function*/ orderFactory = .order.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15) = .strategy.Generic(orderFactory(.strategy.side.MeanReversion(ewma_alpha)),eventGen)
    
    // defined at .output\names.sc: 1844.5
    /** Empty strategy doing nothing
     */
    @python.intrinsic("strategy.basic._Empty_Impl")
    def Empty() : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1849.5
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the efficiency of the strategies is evaluated
     * These efficiencies are mapped into weights using *weight* and *normilizer*
     * functions per every strategy and *corrector* for the whole collection of weights
     * These weights are used to choose randomly a strategy to run for the next quant of time.
     * All other strategies are suspended
     */
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(/** original strategies that can be suspended */ strategies = [.strategy.Noise()],
                         /** function creating a virtual account used for estimate efficiency of the strategy itself */ account = .strategy.account.virtualMarket(),
                         /** function estimating is the strategy efficient or not */ weight = .strategy.weight.efficiencyTrend(),
                         /** function that maps trader efficiency to its weight that will be used for random choice */ normalizer = .strategy.weight.atanPow(),
                         /** given array of strategy weights corrects them.
                           * for example it may set to 0 all weights except the maximal one */ corrector = .strategy.weight.identityL()) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1864.5
    /** A Strategy that allows to drive the asset price based on historical market data
     *  by creating large volume orders for the given price.
     *
     *  Every time step of 1 in the simulation corresponds to a 1 day in the market data.
     *
     *  At each time step the previous Limit Buy/Sell orders are cancelled and new ones
     *  are created based on the next price of the market data.
     */
    def MarketData(/** Ticker of the asset */ ticker = "^GSPC",
                   /** Start date in DD-MM-YYYY format */ start = "2001-1-1",
                   /** End date in DD-MM-YYYY format */ end = "2010-1-1",
                   /** Price difference between orders placed and underlying quotes */ delta = 1.0,
                   /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0) = .strategy.Combine(.strategy.Generic(.order.Iceberg(volume,.order.FloatingPrice(.observable.BreaksAtChanges(.observable.Quote(ticker,start,end)+delta),.order.price.Limit(.side.Sell(),volume*1000))),.event.After(0.0)),.strategy.Generic(.order.Iceberg(volume,.order.FloatingPrice(.observable.BreaksAtChanges(.observable.Quote(ticker,start,end)-delta),.order.price.Limit(.side.Buy(),volume*1000))),.event.After(0.0)))
    
    // defined at .output\names.sc: 1878.5
    /** Strategy that listens to all orders sent by a trader to the market
     *  and in some moments of time it randomly chooses an order and cancels it
     *  Note: a similar effect can be obtained using order.WithExpiry meta orders
     */
    @python.intrinsic("strategy.canceller._Canceller_Impl")
    def Canceller(/** intervals between order cancellations */ cancellationIntervalDistr = .math.random.expovariate(1.0)) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1885.5
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
                              /** order factory function*/ orderFactory = .order.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell() : .IFunction[.Side],
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1)) = .strategy.Generic(orderFactory(side,.strategy.price.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    // defined at .output\names.sc: 1894.5
    /** Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** order factory function*/ orderFactory = .order.Limit(),
                /** Event source making the strategy to wake up*/ eventGen = .event.Every()) : .ISingleAssetStrategy
    
    // defined at .output\names.sc: 1901.5
    def MarketMaker(delta = 1.0,
                    volume = 20.0) = .strategy.Combine(.strategy.Generic(.order.Iceberg(volume,.order.FloatingPrice(.observable.BreaksAtChanges(.observable.OnEveryDt(0.9,.orderbook.SafeSidePrice(.orderbook.Asks(),100+delta)/.math.Exp(.math.Atan(.trader.Position())/1000))),.order.price.Limit(.side.Sell(),volume*1000))),.event.After(0.0)),.strategy.Generic(.order.Iceberg(volume,.order.FloatingPrice(.observable.BreaksAtChanges(.observable.OnEveryDt(0.9,.orderbook.SafeSidePrice(.orderbook.Bids(),100-delta)/.math.Exp(.math.Atan(.trader.Position())/1000))),.order.price.Limit(.side.Buy(),volume*1000))),.event.After(0.0)))
    
    // defined at .output\names.sc: 1904.5
    /** Noise strategy is a quite dummy strategy that randomly chooses trade side and sends market orders
     */
    def Noise(/** Event source making the strategy to wake up*/ eventGen = .event.Every(.math.random.expovariate(1.0)),
              /** order factory function*/ orderFactory = .order.side.Market()) = .strategy.Generic(orderFactory(.strategy.side.Noise()),eventGen)
    
    // defined at .output\names.sc: 1909.5
    /** Strategy believing that trader position should be proportional to the relative standard deviation of its price
     */
    def Bollinger_linear(/** order factory function */ orderFactory = .order.signedVolume.MarketSigned(),
                         /** alpha parameter for exponentially weighted moving everage and variance */ alpha = 0.15,
                         /** observable scaling function that maps relative deviation to desired position */ k = .const(0.5)) = .strategy.Generic(orderFactory(.strategy.position.Bollinger_linear(alpha,k)))
}
@category = "Trader"

package trader() {
    // defined at .output\names.sc: 1920.5
    /** Number of money owned by trader
     */
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = .trader.SingleProxy() : .IAccount) : .IObservable[.Price]
    
    // defined at .output\names.sc: 1925.5
    /** Returns traders naive approximation of trader eficiency.
     *  It takes into account only the best price of the order queue
     */
    def RoughPnL(trader = .trader.SingleProxy() : .IAccount) = .trader.Balance(trader)+.orderbook.NaiveCumulativePrice(.orderbook.OfTrader(trader),.trader.Position(trader))
    
    // defined at .output\names.sc: 1930.5
    /** Returns position of the trader
     *  It is negative if trader has sold more assets than has bought and
     *  positive otherwise
     */
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader = .trader.SingleProxy() : .IAccount) : .IObservable[.Volume]
    
    // defined at .output\names.sc: 1937.5
    /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    def Efficiency(trader = .trader.SingleProxy() : .IAccount) = .trader.Balance(trader)+.orderbook.CumulativePrice(.orderbook.OfTrader(trader),.trader.Position(trader))
    
    // defined at .output\names.sc: 1941.5
    /** Phantom trader that is used to refer to the current trader
     *  (normally it is used to define trader properties and strategies)
     */
    @python.intrinsic("trader.proxy._Single_Impl")
    @label = "N/A"
    def SingleProxy() : .ISingleAssetTrader
    
    // defined at .output\names.sc: 1948.5
    /** A trader that trades different assets
     *  It can be considered as a composition of single asset traders and multi asset strategies
     *  At the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets
     */
    @python.intrinsic("trader.classes._MultiAsset_Impl")
    @label = "%(name)s"
    def MultiAsset(/** defines accounts for every asset to trade */ traders = [] : .List[.ISingleAssetTrader],
                   /** multi asset strategy run by the trader */ strategy = .strategy.Arbitrage(),
                   name = "-trader-",
                   /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                   /** defines what data should be gathered for the trader */ timeseries = [] : .List[.ITimeSerie]) : .ITrader
    
    // defined at .output\names.sc: 1960.5
    /** Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(trader = .trader.SingleProxy() : .IAccount,
                        alpha = 0.15) = .math.Derivative(.math.EW.Avg(.trader.Efficiency(trader),alpha))
    
    // defined at .output\names.sc: 1965.5
    /** Cumulative volume of orders sent to the market but haven't matched yet
     */
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = .trader.SingleProxy() : .IAccount) : .IObservable[.Volume]
    
    // defined at .output\names.sc: 1970.5
    /** A trader that trades a single asset on a single market
     */
    @python.intrinsic("trader.classes._SingleAsset_Impl")
    @label = "%(name)s"
    def SingleAsset(/** order book for the asset being traded */ orderBook : .IOrderBook,
                    /** strategy run by the trader */ strategy = .strategy.Noise(),
                    name = "-trader-",
                    /** current position of the trader (number of assets that it owns) */ amount = 0.0,
                    /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                    /** defines what data should be gathered for the trader */ timeseries = [] : .List[.ITimeSerie]) : .ISingleAssetTrader
}
@category = "Asset"

package orderbook() {@queue = "Ask_{%(book)s}"
    
    package ask() {
        // defined at .output\names.sc: 1989.9
        @label = "[{{queue}}]_{%(alpha)s}"
        def WeightedPrice(book = .orderbook.OfTrader(),
                          alpha = 0.15) = .orderbook.WeightedPrice(.orderbook.ask._queue(book),alpha)
        
        // defined at .output\names.sc: 1993.9
        @label = "LastTradeVolume({{queue}})"
        def LastTradeVolume(book = .orderbook.OfTrader()) = .orderbook.LastTradeVolume(.orderbook.ask._queue(book))
        
        // defined at .output\names.sc: 1996.9
        @label = "{{queue}}"
        def Price(book = .orderbook.OfTrader()) = .orderbook.BestPrice(.orderbook.ask._queue(book))
        
        // defined at .output\names.sc: 1999.9
        @label = "Last({{queue}})"
        def LastPrice(book = .orderbook.OfTrader()) = .orderbook.LastPrice(.orderbook.ask._queue(book))
        
        def _queue = .orderbook.Asks
        
        // defined at .output\names.sc: 2004.9
        @label = "LastTrade({{queue}})"
        def LastTradePrice(book = .orderbook.OfTrader()) = .orderbook.LastTradePrice(.orderbook.ask._queue(book))
    }
    @queue = "Bid^{%(book)s}"
    
    package bid() {
        // defined at .output\names.sc: 2012.9
        @label = "[{{queue}}]_{%(alpha)s}"
        def WeightedPrice(book = .orderbook.OfTrader(),
                          alpha = 0.15) = .orderbook.WeightedPrice(.orderbook.bid._queue(book),alpha)
        
        // defined at .output\names.sc: 2016.9
        @label = "LastTradeVolume({{queue}})"
        def LastTradeVolume(book = .orderbook.OfTrader()) = .orderbook.LastTradeVolume(.orderbook.bid._queue(book))
        
        // defined at .output\names.sc: 2019.9
        @label = "{{queue}}"
        def Price(book = .orderbook.OfTrader()) = .orderbook.BestPrice(.orderbook.bid._queue(book))
        
        // defined at .output\names.sc: 2022.9
        @label = "Last({{queue}})"
        def LastPrice(book = .orderbook.OfTrader()) = .orderbook.LastPrice(.orderbook.bid._queue(book))
        
        def _queue = .orderbook.Bids
        
        // defined at .output\names.sc: 2027.9
        @label = "LastTrade({{queue}})"
        def LastTradePrice(book = .orderbook.OfTrader()) = .orderbook.LastTradePrice(.orderbook.bid._queue(book))
    }
    
    // defined at .output\names.sc: 2032.5
    /** Phantom orderbook that is used to refer to the current order book
     *
     *  May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
     */
    @python.intrinsic("orderbook.of_trader._Proxy_Impl")
    @label = "N/A"
    def Proxy() : .IOrderBook
    
    // defined at .output\names.sc: 2040.5
    /** Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    @python.observable()
    def SafeSidePrice(queue = .orderbook.Asks(),
                      /** price to be used if there haven't been any trades */ defaultValue = .constant(100.0)) = .IfDefined(.orderbook.BestPrice(queue),.IfDefined(.orderbook.LastPrice(queue),defaultValue))
    
    // defined at .output\names.sc: 2047.5
    /** Returns moving average of trade prices weighted by their volumes
     */
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = .orderbook.Asks(),
                      /** parameter alpha for the moving average  */ alpha = 0.15) = .math.EW.Avg(.orderbook.LastTradePrice(queue)*.orderbook.LastTradeVolume(queue),alpha)/.math.EW.Avg(.orderbook.LastTradeVolume(queue),alpha)
    
    // defined at .output\names.sc: 2053.5
    /** Returns tick size for the order *book*
     */
    @python.intrinsic("orderbook.props._TickSize_Impl")
    def TickSize(book = .orderbook.OfTrader()) : () => .Price
    
    // defined at .output\names.sc: 2058.5
    /** MidPrice of order *book*
     */
    def MidPrice(book = .orderbook.OfTrader()) = (.orderbook.ask.Price(book)+.orderbook.bid.Price(book))/2.0
    
    // defined at .output\names.sc: 2062.5
    /** Returns sell side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Asks_Impl")
    def Asks(book = .orderbook.OfTrader()) = .orderbook.Queue(book,.side.Sell())
    
    // defined at .output\names.sc: 2067.5
    /** Returns volume of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    def LastTradeVolume(queue = .orderbook.Asks()) : .IObservable[.Volume]
    
    // defined at .output\names.sc: 2073.5
    /** Returns buy side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Bids_Impl")
    def Bids(book = .orderbook.OfTrader()) = .orderbook.Queue(book,.side.Buy())
    
    // defined at .output\names.sc: 2078.5
    /** Returns best order price of *queue*
     *  Returns None is *queue* is empty
     */
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    def BestPrice(queue = .orderbook.Asks()) : .IObservable[.Price]
    
    // defined at .output\names.sc: 2084.5
    /** Represents latency in information propagation between two agents
     * (normally between a trader and a market).
     * Ensures that sending packets via links preserves their order.
     * Holds two one-way links in opposite directions.
     */
    @python.intrinsic("orderbook.link._TwoWayLink_Impl")
    def TwoWayLink(/** Forward link (normally from a trader to a market)*/ up = .orderbook.Link(),
                   /** Backward link (normally from a market to a trader)*/ down = .orderbook.Link()) : .ITwoWayLink
    
    // defined at .output\names.sc: 2093.5
    /** Returns order queue of order *book* for trade *side*
     */
    @python.intrinsic("orderbook.proxy._Queue_Impl")
    def Queue(book = .orderbook.OfTrader(),
              side = .side.Sell()) : .IOrderQueue
    
    // defined at .output\names.sc: 2099.5
    /** Phantom orderbook used to refer to the order book associated with a single asset trader
     *
     *  May be used only in objects that are held by traders (so it is used in trader properties and strategies)
     */
    @python.intrinsic("orderbook.of_trader._OfTrader_Impl")
    @label = "N/A"
    def OfTrader(Trader = .trader.SingleProxy() : .IAccount) : .IOrderBook
    
    // defined at .output\names.sc: 2107.5
    /** Returns price for best orders of total volume *depth*
     *
     *  In other words cumulative price corresponds to trader balance change
     *  if a market order of volume *depth* is completely matched
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book = .orderbook.OfTrader(),
                        depth = .constant(1.0)) : .IObservable[.Price]
    
    // defined at .output\names.sc: 2119.5
    /** Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]
     *  Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = .orderbook.Asks(),
                     /** distance between two volumes */ volumeDelta = 30.0,
                     /** number of volume levels to track */ volumeCount = 10) : .IObservable[.IVolumeLevels]
    
    // defined at .output\names.sc: 2128.5
    /** Returns last defined price at *queue*
     *  Returns None is *queue* has been always empty
     */
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    def LastPrice(queue = .orderbook.Asks()) : .IObservable[.Price]
    
    // defined at .output\names.sc: 2134.5
    /** Order book for a single asset in a market.
     * Maintains two order queues for orders of different sides
     */
    @python.intrinsic("orderbook.local._Local_Impl")
    @label = "%(name)s"
    def Local(name = "-orderbook-",
              tickSize = 0.01,
              _digitsToShow = 2,
              timeseries = [] : .List[.ITimeSerie]) : .IOrderBook
    
    // defined at .output\names.sc: 2144.5
    /** Represent an *orderbook* from point of view of a remote trader connected
     * to the market by means of a *link* that introduces some latency in information propagation
     */
    @python.intrinsic("orderbook.remote._Remote_Impl")
    @label = "%(orderbook)s.name^remote"
    def Remote(orderbook = .orderbook.Local(),
               link = .orderbook.TwoWayLink(),
               timeseries = [] : .List[.ITimeSerie]) : .IOrderBook
    
    // defined at .output\names.sc: 2153.5
    /** Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    def NaiveCumulativePrice(book = .orderbook.OfTrader(),
                             depth = .constant(1.0)) = if depth<0.0 then depth*.orderbook.ask.Price(book) else if depth>0.0 then depth*.orderbook.bid.Price(book) else 0.0
    
    // defined at .output\names.sc: 2162.5
    /** Represents latency in information propagation from one agent to another one
     * (normally between a trader and a market).
     * Ensures that sending packets via a link preserves their order.
     */
    @python.intrinsic("orderbook.link._Link_Impl")
    def Link(/** function called for each packet in order to determine
               * when it will appear at the end point*/ latency = .const(0.001)) : .ILink
    
    // defined at .output\names.sc: 2170.5
    /** Spread of order *book*
     */
    def Spread(book = .orderbook.OfTrader()) = .orderbook.ask.Price(book)-.orderbook.bid.Price(book)
    
    // defined at .output\names.sc: 2174.5
    /** Returns price of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    def LastTradePrice(queue = .orderbook.Asks()) : .IObservable[.Price]
}
@category = "Basic"

package observable() {
    // defined at .output\names.sc: 2185.5
    /** Discretizes function *x* at even time steps *dt*
     */
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    def OnEveryDt(/** time discretization step */ dt = 1.0,
                  /** function to discretize */ x = .constant(1.0)) : .IObservable[.Float]
    
    // defined at .output\names.sc: 2193.5
    /** Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker*
     *  and follows the price in scale 1 model unit of time = 1 real day
     */
    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(/** defines quotes to download */ ticker = "^GSPC",
              /** defines first day to download in form YYYY-MM-DD */ start = "2001-1-1",
              /** defines last day to download in form YYYY-MM-DD */ end = "2010-1-1") : .IObservable[.Price]
    
    // defined at .output\names.sc: 2202.5
    /** Observable listening to *source*
     *  When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
     */
    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source = .const(1.0)) : .IObservable[.Float]
}
@python = "no"

package trash() {
    package in1() {
        package in2() {
            // defined at .output\names.sc: 2217.13
            def S1(y = "abc") = y
            
            // defined at .output\names.sc: 2219.13
            def F(x = .trash.in1.in2.IntFunc() : .IFunction[.Float]) = x
            
            // defined at .output\names.sc: 2221.13
            def A(x = .constant(),
                  y = if 3>x+2 then x else x*2) : () => .trash.types.T
            
            // defined at .output\names.sc: 2224.13
            def IntObs() : .IObservable[.Int]
            
            // defined at .output\names.sc: 2226.13
            def IntFunc() : .IFunction[.Int]
            
            // defined at .output\names.sc: 2228.13
            def C(x : .IFunction[.CandleStick],
                  p = [12,23.2,0]) = p
            
            // defined at .output\names.sc: 2231.13
            def S2() : .Optional[.String] = .trash.in1.in2.S1()
            
            // defined at .output\names.sc: 2233.13
            def O(x = .trash.in1.in2.IntObs() : .IObservable[.Float]) = x
        }
        
        // defined at .output\names.sc: 2237.9
        def A(x : () => .trash.types.T1 = .trash.A()) : () => .trash.types.U
        
        // defined at .output\names.sc: 2239.9
        def toInject1() : () => .Int
        
        // defined at .output\names.sc: 2241.9
        def toInject2() : () => .Int
    }
    
    package types() {
        type T1 = T
        
        type T
        
        type R : T
        
        type U : T, R
    }
    
    package overloading() {
        // defined at .output\names.sc: 2259.9
        def f(x : .IFunction[.Volume]) = x
        
        // defined at .output\names.sc: 2261.9
        def f(x : .IFunction[.Price]) = x
        
        // defined at .output\names.sc: 2263.9
        def g(x : .IFunction[.Volume]) = .trash.overloading.f(x)
        
        // defined at .output\names.sc: 2265.9
        def h() = .trash.overloading.f(12)
        
        // defined at .output\names.sc: 2267.9
        def hh() = .trash.overloading.f(12.2)
    }
    
    // defined at .output\names.sc: 2271.5
    def A(x = .trash.in1.in2.A()) : () => .trash.types.R
}

type ITrader

type IGraph

@impl = "_Function_Impl"
type Function[T] : IFunction[T]

type CandleStick

type Volume = Int

type Optional[T]

type IAccount

type Side

type Boolean

type Price = Float

type IOrderQueue

type Float

type Int : Float

type ILink

type IOrderBook

type IEvent

type IMultiAssetStrategy

type ITwoWayLink

type IObservable[U] : IFunction[U], IEvent

type IFunction[T] = () => T

type ISingleAssetStrategy

type ISingleAssetTrader : IAccount, ITrader

type IVolumeLevels

type Order

type List[T]

type IDifferentiable : IFunction[Float]

type ITimeSerie

type Any

type IOrderGenerator = IObservable[Order]

type String

// defined at .output\names.sc: 2336.1
/** Function always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"
def constant(x = 1.0) = .const(x) : .IFunction[.Float]

// defined at .output\names.sc: 2342.1
/** Function always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"
def constant(x = 1) = .const(x) : .IFunction[.Int]

// defined at .output\names.sc: 2348.1
/** Function always returning *False*
 */
@category = "Basic"
@python.intrinsic.function("_constant._False_Impl")
@label = "False"
def false() : .IFunction[.Boolean]

// defined at .output\names.sc: 2355.1
/** Trivial observable always returning *True*
 */
@category = "Basic"
@python.intrinsic.observable("_constant._True_Impl")
@label = "True"
def observableTrue() : .IObservable[.Boolean]

// defined at .output\names.sc: 2362.1
/** Trivial observable always returning *undefined* or *None* value
 */
@category = "Basic"
@python.intrinsic("_constant._Null_Impl")
def null() : () => .Float

// defined at .output\names.sc: 2368.1
/** Time serie to store and render it after on a graph
 *  Used to specify what data should be collected about order books and traders
 */
@category = "Basic"
@python.intrinsic("timeserie._ToRecord_Impl")
@label = "%(source)s"
def TimeSerie(source = .const(0.0) : .IObservable[.Any],
              graph = .veusz.Graph(),
              _digitsToShow = 4,
              _smooth = 1) : .ITimeSerie

// defined at .output\names.sc: 2379.1
/** Trivial observable always returning *False*
 */
@category = "Basic"
@python.intrinsic.observable("_constant._False_Impl")
@label = "False"
def observableFalse() : .IObservable[.Boolean]

// defined at .output\names.sc: 2386.1
/** Trivial observable always returning *x*
 */
@category = "Basic"
@python.intrinsic.observable("_constant._Constant_Impl")
@label = "C=%(x)s"
def const(x = 1.0) : .IObservable[.Float]

// defined at .output\names.sc: 2393.1
/** Trivial observable always returning *x*
 */
@category = "Basic"
@python.intrinsic.observable("_constant._Constant_Impl")
@label = "C=%(x)s"
def const(x = 1) : .IObservable[.Int]

// defined at .output\names.sc: 2400.1
/** Observable returning at the end of every *timeframe*
 * open/close/min/max price, its average and standard deviation
 */
@category = "Basic"
@python.intrinsic("observable.candlestick.CandleSticks_Impl")
@label = "Candles_{%(source)s}"
def CandleSticks(/** observable data source considered as asset price */ source = .const(1.0),
                 /** size of timeframe */ timeframe = 10.0) : .IObservable[.CandleStick]

// defined at .output\names.sc: 2409.1
/** Function always returning *True*
 */
@category = "Basic"
@python.intrinsic.function("_constant._True_Impl")
@label = "True"
def true() : .IFunction[.Boolean]

// defined at .output\names.sc: 2416.1
/** Returns *x* if defined and *elsePart* otherwise
 */
@category = "Basic"
@python.observable()
@label = "If def(%(x)s) else %(elsePart)s"
def IfDefined(x = .constant(1.0),
              /** function to take values from when *x* is undefined */ elsePart = .constant(1.0)) = if x<>.null() then x else elsePart

// defined at .output\names.sc: 2424.1
/** Time serie holding volume levels of an asset
 * Level of volume V is a price at which cumulative volume of better orders is V
 */
@category = "Basic"
@python.intrinsic("timeserie._VolumeLevels_Impl")
@label = "%(source)s"
def volumeLevels(source : .IFunction[.IVolumeLevels],
                 graph = .veusz.Graph(),
                 _digitsToShow = 4,
                 _smooth = 1,
                 _volumes = [30.0],
                 _isBuy = 1) : .ITimeSerie
