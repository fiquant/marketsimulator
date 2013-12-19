@category = "Side"

package side {
    @python.intrinsic.function("side._Sell_Impl")
    @label = "Sell"
    def Sell() : () => Side
        
    
    @python.intrinsic.function("side._Buy_Impl")
    @label = "Buy"
    def Buy() : () => Side
        
    
    @python.intrinsic.function("side._Buy_Impl")
    @label = "NoneSide"
    def Nothing() : () => Side
        
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("atan")
    @category = "Trigonometric"
    @label = "atan(%(x)s)"
    def Atan(x = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("sqrt")
    @category = "Log/Pow"
    @label = "\\sqrt{%(x)s}"
    def Sqrt(x = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("exp")
    @category = "Log/Pow"
    @label = "e^{%(x)s}"
    def Exp(x = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("log")
    @category = "Log/Pow"
    @label = "log(%(x)s)"
    def Log(x = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("pow")
    @category = "Log/Pow"
    @label = "%(base)s^{%(power)s}"
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
@category = "Basic"

package observable {@category = "Price function"
    
    package pricefunc {
        @python.observable()
        @label = "Lp_{%(side)s}(%(book)s)"
        def LiquidityProvider(side = side.Sell(),
                              initialValue = 100.0,
                              priceDistr = mathutils.rnd.lognormvariate(0.0,0.1),
                              book = orderbook.OfTrader())
             = orderbook.SafeSidePrice(orderbook.Queue(book,side),constant(initialValue))*priceDistr
    }
    @category = "Side function"
    
    package sidefunc {
        @python.observable()
        @label = "Pt_{%(factor)s*%(dependee)s}(%(book)s)"
        def PairTrading(dependee = orderbook.OfTrader(),
                        factor = constant(1.0),
                        book = orderbook.OfTrader())
             = FundamentalValue(orderbook.MidPrice(dependee)*factor,book)
        
        @python.observable()
        @label = "SignalSide_{%(threshold)s}(%(signal)s)"
        def Signal(signal = constant(),
                   threshold = 0.7)
             = if signal>threshold then side.Buy() else if signal<0.0-threshold then side.Sell() else side.Nothing()
        
        @python.observable()
        @label = "CrAvg_{%(alpha_1)s}^{%(alpha_2)s}(%(book)s)"
        def CrossingAverages(alpha_1 = 0.015,
                             alpha_2 = 0.15,
                             threshold = 0.0,
                             book = orderbook.OfTrader())
             = Signal(EW.Avg(orderbook.MidPrice(book),alpha_1)-EW.Avg(orderbook.MidPrice(book),alpha_2),threshold)
        
        @python.observable()
        @label = "Tf_{%(alpha)s}(%(book)s)"
        def TrendFollower(alpha = 0.015,
                          threshold = 0.0,
                          book = orderbook.OfTrader())
             = Signal(Derivative(EW.Avg(orderbook.MidPrice(book),alpha)),threshold)
        
        @python.observable()
        @label = "Fv_{%(fv)s}(%(book)s)"
        def FundamentalValue(fv = constant(200.0),
                             book = orderbook.OfTrader())
             = if orderbook.BidPrice(book)>fv then side.Sell() else if orderbook.AskPrice(book)<fv then side.Buy() else side.Nothing()
        
        @python.observable()
        @label = "Mr_{%(alpha)s}(%(book)s)"
        def MeanReversion(alpha = 0.015,
                          book = orderbook.OfTrader())
             = FundamentalValue(EW.Avg(orderbook.MidPrice(book),alpha),book)
        
        @python.observable()
        @label = "Noise_{%(side_distribution)s}"
        def Noise(side_distribution : IFunction = mathutils.rnd.uniform(0.0,1.0))
             = if side_distribution>0.5 then side.Sell() else side.Buy()
    }
    @category = "Statistics"
    
    package Cumulative {
        @python.intrinsic.function("moments.cma.CMA_Impl")
        @label = "Avg_{cumul}(%(source)s)"
        def Avg(source = const()) : () => Float
            
        
        @python.intrinsic.function("moments.cmv.Variance_Impl")
        @label = "\\sigma^2_{cumul}(%(source)s)"
        def Var(source = const()) : () => Float
            
        
        @python.function()
        @label = "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}"
        def StdDev(source = const())
             = mathops.Sqrt(Var(source))
        
        @python.function()
        @label = "RSD_{cumul}_{%(source)s}"
        def RelStdDev(source = const())
             = (source-Avg(source))/StdDev(source)
    }
    @category = "RSI"
    
    package rsi {
        @python.observable()
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(source = orderbook.MidPrice(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
    @category = "MACD"
    
    package macd {
        @python.function()
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
        def MACD(x = orderbook.MidPrice(),
                 slow = 26.0,
                 fast = 12.0)
             = EW.Avg(x,2.0/(fast+1.0))-EW.Avg(x,2.0/(slow+1.0))
        
        @python.function()
        @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Signal(x = orderbook.MidPrice(),
                   slow = 26.0,
                   fast = 12.0,
                   timeframe = 9.0,
                   step = 1.0)
             = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2.0/(timeframe+1.0))
        
        @python.function()
        @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Histogram(x = orderbook.MidPrice(),
                      slow = 26.0,
                      fast = 12.0,
                      timeframe = 9.0,
                      step = 1.0)
             = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
    }
    @category = "Trader's"
    
    package trader {
        @python.intrinsic.observable("trader.props.Balance_Impl")
        @label = "Balance_{%(trader)s}"
        def Balance(trader = SingleProxy()) : () => Float
            
        
        @python.intrinsic.observable("trader.props.Position_Impl")
        @label = "Amount_{%(trader)s}"
        def Position(trader = SingleProxy()) : () => Float
            
        
        @python.observable()
        @label = "Efficiency_{%(trader)s}"
        def Efficiency(trader = SingleProxy())
             = Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader))
        
        @python.intrinsic.function("trader.proxy._Single_Impl")
        @label = "N/A"
        def SingleProxy() : ISingleAssetTrader
            
        
        @python.function()
        @label = "EfficiencyTrend_{%(trader)s}"
        def EfficiencyTrend(trader = SingleProxy(),
                            alpha = 0.15)
             = Derivative(EW.Avg(Efficiency(trader),alpha))
        
        @python.intrinsic.observable("trader.props.PendingVolume_Impl")
        @label = "PendingVolume_{%(trader)s}"
        def PendingVolume(trader = SingleProxy()) : () => Float
            
    }
    @category = "Volume function"
    
    package volumefunc {
        @python.observable()
        @label = "Dp_{%(trader)s}(%(desiredPosition)s)"
        def DesiredPosition(desiredPosition = const(),
                            trader = trader.SingleProxy())
             = desiredPosition-trader.Position(trader)-trader.PendingVolume(trader)
        
        @python.observable()
        @label = "Bl_{%(trader)s}(%(alpha)s)*%(k)s"
        def Bollinger_linear(alpha = 0.15,
                             k = const(0.5),
                             trader = trader.SingleProxy())
             = DesiredPosition(OnEveryDt(1.0,EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)),alpha))*k,trader)
        
        @python.observable()
        @label = "RSI_{%(trader)s}(%(alpha)s, %(timeframe)s)*%(k)s"
        def RSI_linear(alpha = 1.0/14.0,
                       k = const(-0.04),
                       timeframe = 1.0,
                       trader = trader.SingleProxy())
             = DesiredPosition(OnEveryDt(1.0,50.0-orderbook.RSI(orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
    }
    @category = "Statistics"
    
    package EW {
        @python.intrinsic.function("moments.ewma.EWMA_Impl")
        @label = "Avg_{\\alpha=%(alpha)s}(%(source)s)"
        def Avg(source = constant(),
                alpha = 0.015) : IDifferentiable
            
        
        @python.intrinsic.function("moments.ewmv.EWMV_Impl")
        @label = "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}"
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.function()
        @label = "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}"
        def StdDev(source = const(),
                   alpha = 0.015)
             = mathops.Sqrt(Var(source,alpha))
        
        @python.function()
        @label = "RSD_{\\alpha=%(alpha)s}_{%(source)s}"
        def RelStdDev(source = const(),
                      alpha = 0.15)
             = (source-Avg(source,alpha))/StdDev(source,alpha)
    }
    @category = "Asset's"
    
    package orderbook {
        @python.observable()
        @label = "SafeSidePrice^{%(queue)s}"
        def SafeSidePrice(queue = Asks(),
                          defaultValue = constant(100.0))
             = IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue))
        
        def PriceAtVolume(queue = Asks(),
                          volume = 100.0) : () => Float
            
        
        @python.observable()
        @label = "Price_{%(alpha)s}^{%(queue)s}"
        def WeightedPrice(queue = Asks(),
                          alpha = 0.015)
             = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
        
        def TickSize(book = OfTrader()) : () => Float
            
        
        @python.observable()
        @label = "Ask_{%(book)s}"
        def AskLastPrice(book = OfTrader())
             = LastPrice(Asks(book))
        
        @python.observable()
        @label = "Ask_{%(alpha)s}^{%(book)s}"
        def AskWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Asks(book),alpha)
        
        @python.observable()
        @label = "MidPrice_{%(book)s}"
        def MidPrice(book = OfTrader())
             = (AskPrice(book)+BidPrice(book))/2.0
        
        @python.intrinsic.function("orderbook.queue._Asks_Impl")
        @label = "Asks(%(book)s)"
        def Asks(book = OfTrader())
             = Queue(book,side.Sell())
        
        @python.observable()
        @label = "Bid_{%(alpha)s}^{%(book)s}"
        def BidWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Bids(book),alpha)
        
        @python.observable()
        @label = "Ask_{%(book)s}"
        def AskPrice(book = OfTrader())
             = BestPrice(Asks(book))
        
        @python.intrinsic.observable("orderbook.last_trade._LastTradeVolume_Impl")
        @label = "LastTradeVolume(%(queue)s)"
        def LastTradeVolume(queue = Asks()) : IObservable
            
        
        @python.observable()
        @label = "Bid^{%(book)s}"
        def BidPrice(book = OfTrader())
             = BestPrice(Bids(book))
        
        @python.intrinsic.function("orderbook.queue._Bids_Impl")
        @label = "Bids(%(book)s)"
        def Bids(book = OfTrader())
             = Queue(book,side.Buy())
        
        @python.intrinsic.observable("orderbook.props._BestPrice_Impl")
        @label = "Price(%(queue)s)"
        def BestPrice(queue = Asks()) : IObservable
            
        
        @python.intrinsic.function("orderbook.queue._Queue_Impl")
        @label = "Queue(%(book)s)"
        def Queue(book = OfTrader(),
                  side = side.Sell()) : IOrderQueue
            
        
        @python.intrinsic.function("orderbook.of_trader._OfTrader_Impl")
        @label = "N/A"
        def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
            
        
        @python.observable()
        @label = "Bid^{%(book)s}"
        def BidLastPrice(book = OfTrader())
             = LastPrice(Bids(book))
        
        @python.intrinsic.observable("orderbook.cumulative_price.CumulativePrice_Impl")
        @label = "CumulativePrice(%(book)s, %(depth)s)"
        def CumulativePrice(book = OfTrader(),
                            depth = constant()) : () => Float
            
        
        @python.intrinsic.observable("orderbook.last_price._LastPrice_Impl")
        @label = "LastPrice(%(queue)s)"
        def LastPrice(queue = Asks()) : IObservable
            
        
        @python.observable()
        @label = "Spread_{%(book)s}"
        def Spread(book = OfTrader())
             = AskPrice(book)-BidPrice(book)
        
        @python.intrinsic.observable("orderbook.last_trade._LastTradePrice_Impl")
        @label = "LastTradePrice(%(queue)s)"
        def LastTradePrice(queue = Asks()) : IObservable
            
    }
    @category = "Statistics"
    
    package Moving {
        @python.intrinsic.function("moments.ma.MA_Impl")
        @label = "Avg_{n=%(timeframe)s}(%(source)s)"
        def Avg(source = const(),
                timeframe = 100.0) : () => Float
            
        
        @python.intrinsic.function("moments.mv.MV_Impl")
        @label = "\\sigma^2_{n=%(timeframe)s}(%(source)s)"
        def Var(source = const(),
                timeframe = 100.0)
             = Max(const(0.0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
        
        @python.function()
        @label = "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}"
        def StdDev(source = const(),
                   timeframe = 100.0)
             = mathops.Sqrt(Var(source))
        
        @python.function()
        @label = "RSD_{n=%(timeframe)s}_{%(source)s}"
        def RelStdDev(source = const(),
                      timeframe = 100.0)
             = (source-Avg(source,timeframe))/StdDev(source,timeframe)
    }
    
    @python.intrinsic.observable("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    def OnEveryDt(dt = 1.0,
                  x = constant()) : IObservable
        
    
    @python.observable()
    @label = "min{%(x)s, %(y)s}"
    def Min(x = constant(),
            y = constant())
         = if x<y then x else y
    
    @python.observable()
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(source = orderbook.MidPrice(),
                      timeframe = 10.0)
         = Max(const(0.0),Lagged(source,timeframe)-source)
    
    @python.intrinsic.observable("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable
        
    
    @python.observable()
    @label = "max{%(x)s, %(y)s}"
    def Max(x = constant(),
            y = constant())
         = if x>y then x else y
    
    @python.observable()
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(source = orderbook.MidPrice(),
                    timeframe = 10.0)
         = Max(const(0.0),source-Lagged(source,timeframe))
    
    @python.observable()
    @category = "Pow/Log"
    @label = "{%(x)s}^2"
    def Sqr(x = constant())
         = x*x
    
    @python.observable()
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(book = orderbook.OfTrader(),
            timeframe = 10.0,
            alpha = 0.015)
         = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha))
}

package trash {
    package types {
        package $2 {
            package $0 {
                type U : T, R
            }
        }
        
        package $1 {
            type R : T
        }
        
        package $0 {
            type T
        }
        
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

@python.function()
@label = "C=%(x)s"
@category = "Basic"
def constant(x = 1.0) : IFunction
     = const(x)

type Side

@python.intrinsic.function("_constant._Null_Impl")
@category = "Basic"
@label = "Null"
def null() : () => Float
    

type IOrderQueue

type IOrderBook

@python.intrinsic.function("_constant._Constant_Impl")
@category = "Basic"
@label = "C=%(x)s"
def const(x = 1.0) : IObservable
    

type ISingleAssetTrader

@python.intrinsic.function("observable.derivative._Derivative_Impl")
@category = "Basic"
@label = "\\frac{d%(x)s}{dt}"
def Derivative(x : IDifferentiable = observable.EW.Avg()) : () => Float
    

type IDifferentiable : IFunction

@python.observable()
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
def IfDefined(x = constant(),
              elsePart = constant())
     = if x<>null() then x else elsePart
