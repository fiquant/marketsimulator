
package side {
    @python.intrinsic.function("Side", "Sell", "side._Sell_Impl")
    def Sell() : () => Side
        
    
    @python.intrinsic.function("Side", "Buy", "side._Buy_Impl")
    def Buy() : () => Side
        
    
    @python.intrinsic.function("Side", "None", "side._Buy_Impl")
    def Nothing() : () => Side
        
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("Trigonometric", "atan", "atan(%(x)s)")
    def Atan(x = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
    def Sqrt(x = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("Log/Pow", "exp", "e^{%(x)s}")
    def Exp(x = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("Log/Pow", "log", "log(%(x)s)")
    def Log(x = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
    def Pow(base = constant(1.0),
            power = constant(1.0)) : () => Float
        
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
        def gammavariate(Alpha = 1.0,
                         Beta = 1.0) : () => Float
            
        
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu = 0.0,
                          /** |sigma| is the standard deviation */ Sigma = 1.0) : () => Float
            
        
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha = 1.0) : () => Float
            
        
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
                       Mode = 0.5) : () => Float
            
        
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa = 0.0) : () => Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low = -10.0,
                    High = 10.0) : () => Float
            
        
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha = 1.0,
                           /** |beta| is the shape parameter  */ Beta = 1.0) : () => Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda = 1.0) : () => Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu = 0.0,
                           Sigma = 1.0) : () => Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha = 1.0,
                        Beta = 1.0) : () => Float
            
    }
}

package observable {
    package pricefunc {
        @python.observable("Price function", "Lp_{%(side)s}(%(book)s)")
        def LiquidityProvider(side = side.Sell(),
                              initialValue = 100.0,
                              priceDistr = mathutils.rnd.lognormvariate(0.0,0.1),
                              book = orderbook.OfTrader())
             = orderbook.SafeSidePrice(orderbook.Queue(book,side),constant(initialValue))*priceDistr
    }
    
    package sidefunc {
        @python.observable("Side function", "Pt_{%(factor)s*%(dependee)s}(%(book)s)")
        def PairTrading(dependee = orderbook.OfTrader(),
                        factor = constant(1.0),
                        book = orderbook.OfTrader())
             = FundamentalValue(orderbook.MidPrice(dependee)*factor,book)
        
        @python.observable("Side function", "SignalSide_{%(threshold)s}(%(signal)s)")
        def Signal(signal = constant(),
                   threshold = 0.7)
             = if signal>threshold then side.Buy() else if signal<0.0-threshold then side.Sell() else side.Nothing()
        
        @python.observable("Side function", "CrAvg_{%(alpha_1)s}^{%(alpha_2)s}(%(book)s)")
        def CrossingAverages(alpha_1 = 0.015,
                             alpha_2 = 0.15,
                             threshold = 0.0,
                             book = orderbook.OfTrader())
             = Signal(EW.Avg(orderbook.MidPrice(book),alpha_1)-EW.Avg(orderbook.MidPrice(book),alpha_2),threshold)
        
        @python.observable("Side function", "Tf_{%(alpha)s}(%(book)s)")
        def TrendFollower(alpha = 0.015,
                          threshold = 0.0,
                          book = orderbook.OfTrader())
             = Signal(Derivative(EW.Avg(orderbook.MidPrice(book),alpha)),threshold)
        
        @python.observable("Side function", "Fv_{%(fv)s}(%(book)s)")
        def FundamentalValue(fv = constant(200.0),
                             book = orderbook.OfTrader())
             = if orderbook.BidPrice(book)>fv then side.Sell() else if orderbook.AskPrice(book)<fv then side.Buy() else side.Nothing()
        
        @python.observable("Side function", "Mr_{%(alpha)s}(%(book)s)")
        def MeanReversion(alpha = 0.015,
                          book = orderbook.OfTrader())
             = FundamentalValue(EW.Avg(orderbook.MidPrice(book),alpha),book)
        
        @python.observable("Side function", "Noise_{%(side_distribution)s}")
        def Noise(side_distribution : IFunction = mathutils.rnd.uniform(0.0,1.0))
             = if side_distribution>0.5 then side.Sell() else side.Buy()
    }
    
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        def Avg(source = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        def Var(source = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        def StdDev(source = const())
             = mathops.Sqrt(Var(source))
        
        @python.function("Statistics", "RSD_{cumul}_{%(source)s}")
        def RelStdDev(source = const())
             = (source-Avg(source))/StdDev(source)
    }
    
    package rsi {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source = orderbook.MidPrice(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
    
    package macd {
        @python.function("MACD", "MACD_{%(fast)s}^{%(slow)s}(%(x)s)")
        def MACD(x = orderbook.MidPrice(),
                 slow = 26.0,
                 fast = 12.0)
             = EW.Avg(x,2.0/(fast+1.0))-EW.Avg(x,2.0/(slow+1.0))
        
        @python.function("MACD", "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Signal(x = orderbook.MidPrice(),
                   slow = 26.0,
                   fast = 12.0,
                   timeframe = 9.0,
                   step = 1.0)
             = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2.0/(timeframe+1.0))
        
        @python.function("MACD", "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Histogram(x = orderbook.MidPrice(),
                      slow = 26.0,
                      fast = 12.0,
                      timeframe = 9.0,
                      step = 1.0)
             = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
    }
    
    package trader {
        @python.intrinsic.observable("Trader's", "Balance_{%(trader)s}", "trader.props.Balance_Impl")
        def Balance(trader = SingleProxy()) : () => Float
            
        
        @python.intrinsic.observable("Trader's", "Amount_{%(trader)s}", "trader.props.Position_Impl")
        def Position(trader = SingleProxy()) : () => Float
            
        
        @python.observable("Trader's", "Efficiency_{%(trader)s}")
        def Efficiency(trader = SingleProxy())
             = Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader))
        
        @python.intrinsic.function("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
            
        
        @python.function("Trader's", "EfficiencyTrend_{%(trader)s}")
        def EfficiencyTrend(trader = SingleProxy(),
                            alpha = 0.15)
             = Derivative(EW.Avg(Efficiency(trader),alpha))
        
        @python.intrinsic.observable("Trader's", "PendingVolume_{%(trader)s}", "trader.props.PendingVolume_Impl")
        def PendingVolume(trader = SingleProxy()) : () => Float
            
    }
    
    package volumefunc {
        @python.observable("Volume function", "Dp_{%(trader)s}(%(desiredPosition)s)")
        def DesiredPosition(desiredPosition = constant(),
                            trader = trader.SingleProxy())
             = desiredPosition-trader.Position(trader)-trader.PendingVolume(trader)
        
        def Bollinger_linear(alpha = 0.15,
                             k = const(0.5),
                             trader = trader.SingleProxy())
             = DesiredPosition(EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)),alpha)*k,trader)
        
        def RSI_linear(alpha = 1.0/14.0,
                       k = const(-0.04),
                       timeframe = 1.0,
                       trader = trader.SingleProxy())
             = DesiredPosition((50.0-orderbook.RSI(orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
    }
    
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source = constant(),
                alpha = 0.015) : IDifferentiable
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        def StdDev(source = const(),
                   alpha = 0.015)
             = mathops.Sqrt(Var(source,alpha))
        
        @python.function("Statistics", "RSD_{\\alpha=%(alpha)s}_{%(source)s}")
        def RelStdDev(source = const(),
                      alpha = 0.15)
             = (source-Avg(source,alpha))/StdDev(source,alpha)
    }
    
    package orderbook {
        @python.observable("Orderbook", "SafeSidePrice^{%(queue)s}")
        def SafeSidePrice(queue = Asks(),
                          defaultValue = constant(100.0))
             = IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue))
        
        def PriceAtVolume(queue = Asks(),
                          volume = 100.0) : () => Float
            
        
        @python.observable("Orderbook", "Price_{%(alpha)s}^{%(queue)s}")
        def WeightedPrice(queue = Asks(),
                          alpha = 0.015)
             = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
        
        def TickSize(book = OfTrader()) : () => Float
            
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskLastPrice(book = OfTrader())
             = LastPrice(Asks(book))
        
        @python.observable("Orderbook", "Ask_{%(alpha)s}^{%(book)s}")
        def AskWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Asks(book),alpha)
        
        @python.observable("Orderbook", "MidPrice_{%(book)s}")
        def MidPrice(book = OfTrader())
             = (AskPrice(book)+BidPrice(book))/2.0
        
        @python.intrinsic.function("Asset's", "Asks(%(book)s)", "orderbook.queue._Asks_Impl")
        def Asks(book = OfTrader())
             = Queue(book,side.Sell())
        
        @python.observable("Orderbook", "Bid_{%(alpha)s}^{%(book)s}")
        def BidWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Bids(book),alpha)
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskPrice(book = OfTrader())
             = BestPrice(Asks(book))
        
        @python.intrinsic.observable("Orderbook", "LastTradeVolume(%(queue)s)", "orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue = Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidPrice(book = OfTrader())
             = BestPrice(Bids(book))
        
        @python.intrinsic.function("Asset's", "Bids(%(book)s)", "orderbook.queue._Bids_Impl")
        def Bids(book = OfTrader())
             = Queue(book,side.Buy())
        
        @python.intrinsic.observable("Orderbook", "Price(%(queue)s)", "orderbook.props._BestPrice_Impl")
        def BestPrice(queue = Asks()) : IObservable
            
        
        @python.intrinsic.function("Asset's", "Queue(%(book)s)", "orderbook.queue._Queue_Impl")
        def Queue(book = OfTrader(),
                  side = side.Sell()) : IOrderQueue
            
        
        @python.intrinsic.function("Proxies", "N/A", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidLastPrice(book = OfTrader())
             = LastPrice(Bids(book))
        
        @python.intrinsic.observable("Orderbook", "CumulativePrice(%(book)s, %(depth)s)", "orderbook.cumulative_price.CumulativePrice_Impl")
        def CumulativePrice(book = OfTrader(),
                            depth = constant()) : () => Float
            
        
        @python.intrinsic.observable("Orderbook", "LastPrice(%(queue)s)", "orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue = Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Spread_{%(book)s}")
        def Spread(book = OfTrader())
             = AskPrice(book)-BidPrice(book)
        
        @python.intrinsic.observable("Orderbook", "LastTradePrice(%(queue)s)", "orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue = Asks()) : IObservable
            
    }
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        def Avg(source = const(),
                timeframe = 100.0) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{n=%(timeframe)s}(%(source)s)", "moments.mv.MV_Impl")
        def Var(source = const(),
                timeframe = 100.0)
             = Max(const(0.0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}")
        def StdDev(source = const(),
                   timeframe = 100.0)
             = mathops.Sqrt(Var(source))
        
        @python.function("Statistics", "RSD_{n=%(timeframe)s}_{%(source)s}")
        def RelStdDev(source = const(),
                      timeframe = 100.0)
             = (source-Avg(source,timeframe))/StdDev(source,timeframe)
    }
    
    @python.intrinsic.observable("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt = 1.0,
                  x = constant()) : IObservable
        
    
    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x = constant(),
            y = constant())
         = if x<y then x else y
    
    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source = orderbook.MidPrice(),
                      timeframe = 10.0)
         = Max(const(0.0),Lagged(source,timeframe)-source)
    
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable
        
    
    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x = constant(),
            y = constant())
         = if x>y then x else y
    
    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source = orderbook.MidPrice(),
                    timeframe = 10.0)
         = Max(const(0.0),source-Lagged(source,timeframe))
    
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x = constant())
         = x*x
    
    @python.observable("RSI", "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)")
    def RSI(book = orderbook.OfTrader(),
            timeframe = 10.0,
            alpha = 0.015)
         = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha))
}

package trash {
    package types {
        type T
        
        type R : T
        
        type U : T, R
        
        type T1 = T
    }
    
    package in1 {
        package in2 {
            def A(x = constant(),
                  y = if 3.0>x+2.0 then x else x*2.0) : () => types.T
                
        }
        
        def A(x : () => types.T1 = trash.A()) : () => types.U
            
    }
    
    def A(x = in1.in2.A()) : () => types.R
        
}

@python.function("Basic", "C=%(x)s")
def constant(x = 1.0) : IFunction
     = const(x)

type Side

@python.intrinsic.function("Basic", "Null", "_constant._Null_Impl")
def null() : () => Float
    

type IOrderQueue

type IOrderBook

@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x = 1.0) : IObservable
    

type ISingleAssetTrader

@python.intrinsic.function("Basic", "\\frac{d%(x)s}{dt}", "observable.derivative._Derivative_Impl")
def Derivative(x : IDifferentiable = observable.EW.Avg()) : () => Float
    

type IDifferentiable : IFunction

@python.observable("Basic", "If def(%(x)s) else %(elsePart)s")
def IfDefined(x = constant(),
              elsePart = constant())
     = if x<>null() then x else elsePart
