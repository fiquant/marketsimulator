@category = "Side"
package side {
    
    @python.intrinsic("side._Sell_Impl")
    def Sell() : () => .Side
        
    
    
    @python.intrinsic("side._Buy_Impl")
    def Buy() : () => .Side
        
    
    
    @python.intrinsic("side._Buy_Impl")
    def Nothing() : () => .Side
        
}


package mathops {@category = "Log/Pow"
    package  {
        /** Exponent of x
         *
         */
        @label = "e^{%(x)s}"
        @python.mathops("exp")
        def Exp(x : Optional[.IFunction[.Float]] = .constant(1.0)) : () => .Float
            
        
        /** Natural logarithm of x (to base e)
         *
         */
        @label = "log(%(x)s)"
        @python.mathops("log")
        def Log(x : Optional[.IFunction[.Float]] = .constant(1.0)) : () => .Float
            
        
        /** Square root of x
         *
         */
        @label = "\\sqrt{%(x)s}"
        @python.mathops("sqrt")
        def Sqrt(x : Optional[.IFunction[.Float]] = .constant(1.0)) : () => .Float
            
        
        /** Return *x* raised to the power *y*.
         *
         * Exceptional cases follow Annex F of the C99 standard as far as possible.
         * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
         * even when *x* is a zero or a NaN.
         * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
         * ``pow(x, y)`` is undefined, and raises ``ValueError``.
         */
        @label = "%(base)s^{%(power)s}"
        @python.mathops("pow")
        def Pow(base : Optional[.IFunction[.Float]] = .constant(1.0),
                power : Optional[.IFunction[.Float]] = .constant(1.0)) : () => .Float
            
    }
    
    @category = "Trigonometric"
    package  {
        /** Arc tangent of x, in radians.
         *
         */
        
        @python.mathops("atan")
        def Atan(x : Optional[.IFunction[.Float]] = .constant(0.0)) : () => .Float
            
    }
    
}

@category = "Event"
package event {
    
    @python.intrinsic("event._Every_Impl")
    def Every(intervalFunc : Optional[() => .Float] = .mathutils.rnd.expovariate(1.0)) : .IEvent
        
    
    
    @python.intrinsic("event._After_Impl")
    def After(delay : Optional[.IFunction[.Float]] = .constant(10.0)) : .IEvent
        
}

@category = "N/A"
package veusz {
    
    @python.intrinsic("veusz._Graph_Impl")
    def Graph(name : Optional[.String] = "graph") : .IGraph
        
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
        def gammavariate(Alpha : Optional[.Float] = 1.0,
                         Beta : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Normal distribution
         */
        
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu : Optional[.Float] = 0.0,
                          /** |sigma| is the standard deviation */ Sigma : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Pareto distribution
         */
        
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        
        @python.random()
        def triangular(Low : Optional[.Float] = 0.0,
                       High : Optional[.Float] = 1.0,
                       Mode : Optional[.Float] = 0.5) : () => .Float
            
        
        /** Von Mises distribution
         */
        
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu : Optional[.Float] = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa : Optional[.Float] = 0.0) : () => .Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        
        @python.random()
        def uniform(Low : Optional[.Float] = -10.0,
                    High : Optional[.Float] = 10.0) : () => .Float
            
        
        /** Weibull distribution
         */
        
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha : Optional[.Float] = 1.0,
                           /** |beta| is the shape parameter  */ Beta : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        
        @python.random()
        def lognormvariate(Mu : Optional[.Float] = 0.0,
                           Sigma : Optional[.Float] = 1.0) : () => .Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        
        @python.random()
        def betavariate(Alpha : Optional[.Float] = 1.0,
                        Beta : Optional[.Float] = 1.0) : () => .Float
            
    }
    
}

@category = "Order"
package order {
    package signed {
        def Limit = .order.LimitSigned
        
        def Market = .order.MarketSigned
    }
    
    
    package _ {
        package side {
            package price {
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
        
        
        package side_price {
            def Limit = .order._curried.sideprice_Limit
            
            def ImmediateOrCancel = .order._curried.sideprice_ImmediateOrCancel
            
            def StopLoss = .order._curried.sideprice_StopLoss
            
            def WithExpiry = .order._curried.sideprice_WithExpiry
            
            def FloatingPrice = .order._curried.sideprice_FloatingPrice
            
            def Iceberg = .order._curried.sideprice_Iceberg
            
            def Peg = .order._curried.sideprice_Peg
        }
        
        
        package side_volume {
            package price {
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
        
        
        package price {
            def Limit = .order._curried.price_Limit
            
            def ImmediateOrCancel = .order._curried.price_ImmediateOrCancel
            
            def StopLoss = .order._curried.price_StopLoss
            
            def WithExpiry = .order._curried.price_WithExpiry
            
            def FloatingPrice = .order._curried.price_FloatingPrice
            
            def Iceberg = .order._curried.price_Iceberg
            
            def Peg = .order._curried.price_Peg
        }
        
        
        package volume_price {
            def Limit = .order._curried.volumeprice_Limit
            
            def ImmediateOrCancel = .order._curried.volumeprice_ImmediateOrCancel
            
            def StopLoss = .order._curried.volumeprice_StopLoss
            
            def WithExpiry = .order._curried.volumeprice_WithExpiry
            
            def FloatingPrice = .order._curried.volumeprice_FloatingPrice
            
            def Iceberg = .order._curried.volumeprice_Iceberg
            
            def Peg = .order._curried.volumeprice_Peg
        }
        
        
        package signedVolume {
            def LimitSigned = .order._curried.signedVolume_LimitSigned
            
            def MarketSigned = .order._curried.signedVolume_MarketSigned
        }
        
        
        package price_volume {
            def Limit = .order._curried.pricevolume_Limit
            
            def ImmediateOrCancel = .order._curried.pricevolume_ImmediateOrCancel
            
            def StopLoss = .order._curried.pricevolume_StopLoss
            
            def WithExpiry = .order._curried.pricevolume_WithExpiry
            
            def FloatingPrice = .order._curried.pricevolume_FloatingPrice
            
            def Iceberg = .order._curried.pricevolume_Iceberg
            
            def Peg = .order._curried.pricevolume_Peg
        }
        
        
        package volume {
            package price {
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
        
    }
    
    
    package _curried {
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def side_ImmediateOrCancel(proto : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("price_Limit")
        def volume_price_Limit(side : Optional[() => .Side] = .side.Sell()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def sidevolume_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                               proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sidevolume_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def sidevolume_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                  proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sidevolume_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_StopLoss")
        def side_price_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def price_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                          proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def sideprice_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                    proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def price_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                           proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def price_ImmediateOrCancel(proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_WithExpiry")
        def volume_price_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                    proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def sideprice_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                               proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def volumeprice_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                      proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_Peg")
        def volume_price_Peg(proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def side_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                         proto : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_WithExpiry")
        def sidevolume_price_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                        proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("Peg")
        def volume_Peg(proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sidevolume_ImmediateOrCancel(proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sidevolume_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("FixedBudget")
        def side_FixedBudget(budget : Optional[.IFunction[.Float]] = .constant(1000.0)) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("Limit")
        def sideprice_Limit(volume : Optional[.IFunction[.Float]] = .constant(1.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Peg")
        def sideprice_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Peg")
        def sidevolume_Peg(proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Peg")
        def side_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("LimitSigned")
        def signedVolume_LimitSigned(price : Optional[.IFunction[.Float]] = .constant(100.0)) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_Iceberg")
        def side_price_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                               proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def volumeprice_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                   proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.volumeprice_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def side_price_ImmediateOrCancel(proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def volumeprice_ImmediateOrCancel(proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.volumeprice_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def side_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                            proto : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def side_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                          proto : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_StopLoss")
        def sidevolume_price_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                      proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def pricevolume_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                 proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.pricevolume_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def pricevolume_ImmediateOrCancel(proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.pricevolume_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Peg")
        def pricevolume_Peg(proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Peg")
        def price_Peg(proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def volume_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                            proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.volume_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("Limit")
        def volumeprice_Limit(side : Optional[() => .Side] = .side.Sell()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("price_Limit")
        def sidevolume_price_Limit() : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def sidevolume_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sidevolume_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def volumeprice_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                                proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.volumeprice_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def volume_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                              proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.volume_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def sideprice_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                 proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def volume_ImmediateOrCancel(proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.volume_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def volume_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                 proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("Market")
        def volume_Market(side : Optional[() => .Side] = .side.Sell()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_StopLoss")
        def volume_price_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                  proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def volume_price_ImmediateOrCancel(proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("Limit")
        def side_Limit(price : Optional[.IFunction[.Float]] = .constant(100.0),
                       volume : Optional[.IFunction[.Float]] = .constant(1.0)) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def side_price_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                     proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def side_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                               proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def pricevolume_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                                proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.pricevolume_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_WithExpiry")
        def side_price_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                  proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("price_Limit")
        def side_price_Limit(volume : Optional[.IFunction[.Float]] = .constant(1.0)) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("Limit")
        def pricevolume_Limit(side : Optional[() => .Side] = .side.Sell()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def volume_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                           proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.volume_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def volume_price_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                       proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("Market")
        def side_Market(volume : Optional[.IFunction[.Float]] = .constant(1.0)) : (() => .Side) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def price_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def sidevolume_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                     proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("StopLoss")
        def volumeprice_StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                                 proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.volumeprice_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def price_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                             proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_Iceberg")
        def volume_price_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                                 proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def sidevolume_price_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                           proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("Peg")
        def volumeprice_Peg(proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def sidevolume_price_ImmediateOrCancel(proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("Market")
        def sidevolume_Market() : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("Limit")
        def price_Limit(side : Optional[() => .Side] = .side.Sell(),
                        volume : Optional[.IFunction[.Float]] = .constant(1.0)) : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.curried("Limit")
        def sidevolume_Limit(price : Optional[.IFunction[.Float]] = .constant(100.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("Iceberg")
        def sideprice_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                              proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_Peg")
        def sidevolume_price_Peg(proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("MarketSigned")
        def signedVolume_MarketSigned() : (() => .Float) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("FloatingPrice")
        def pricevolume_FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                                      proto : Optional[(() => .Float) => ((() => .Float) => .IOrderGenerator)] = .order._curried.volume_price_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sideprice_ImmediateOrCancel(proto : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("WithExpiry")
        def pricevolume_WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                                   proto : Optional[((() => .Float),(() => .Float)) => .IOrderGenerator] = .order._curried.pricevolume_Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        
        @python.order.factory.on_proto("price_Peg")
        def side_price_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IOrderGenerator)] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.on_proto("price_Iceberg")
        def sidevolume_price_Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                                     proto : Optional[((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)] = .order._curried.sidevolume_price_Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        
        @python.order.factory.curried("Limit")
        def volume_Limit(side : Optional[() => .Side] = .side.Sell(),
                         price : Optional[.IFunction[.Float]] = .constant(100.0)) : (() => .Float) => .IOrderGenerator
            
    }
    
    
    @python.order.factory("order.limit.Order_Impl")
    def Limit(side : Optional[() => .Side] = .side.Sell(),
              price : Optional[.IFunction[.Float]] = .constant(100.0),
              volume : Optional[.IFunction[.Float]] = .constant(1.0)) : .IOrderGenerator
        
    
    
    @python.order.factory("order.market.Order_Impl")
    def MarketSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0)) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(proto : Optional[.IOrderGenerator] = .order.Limit()) : .IOrderGenerator
        
    
    
    @python.order.factory("order.market.Order_Impl")
    def Market(side : Optional[() => .Side] = .side.Sell(),
               volume : Optional[.IFunction[.Float]] = .constant(1.0)) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(maxloss : Optional[.IFunction[.Float]] = .constant(0.1),
                 proto : Optional[.IOrderGenerator] = .order.Limit()) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(expiry : Optional[.IFunction[.Float]] = .constant(10.0),
                   proto : Optional[.IOrderGenerator] = .order.Limit()) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(floatingPrice : Optional[.IObservable[.Float]] = .const(10.0),
                      proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(lotSize : Optional[.IFunction[.Float]] = .constant(10.0),
                proto : Optional[.IOrderGenerator] = .order.Limit()) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(side : Optional[() => .Side] = .side.Sell(),
                    budget : Optional[.IFunction[.Float]] = .constant(1000.0)) : .IOrderGenerator
        
    
    
    @python.order.factory("order.limit.Order_Impl")
    def LimitSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0),
                    price : Optional[.IFunction[.Float]] = .constant(100.0)) : .IOrderGenerator
        
    
    
    @python.order.factory("order.meta.peg.Factory_Impl")
    def Peg(proto : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.price_Limit()) : .IOrderGenerator
        
}

@category = "Strategy"
package strategy {
    package account {
        package _ {
            package inner {
                
                @python.curried("VirtualMarket")
                def inner_VirtualMarket() : Optional[.ISingleAssetStrategy] => .IAccount
                    
                
                
                @python.curried("Real")
                def inner_Real() : Optional[.ISingleAssetStrategy] => .IAccount
                    
            }
            
        }
        
        
        @python.intrinsic("strategy.account._Account_Impl")
        @curried("inner")
        def Real(inner : Optional[.ISingleAssetStrategy] = .strategy.Noise()) : .IAccount
            
        
        
        @python.intrinsic("strategy.account._VirtualMarket_Impl")
        @curried("inner")
        def VirtualMarket(inner : Optional[.ISingleAssetStrategy] = .strategy.Noise()) : .IAccount
            
        def real = .strategy.account._.inner.inner_Real
        
        def virtualMarket = .strategy.account._.inner.inner_VirtualMarket
    }
    
    
    package weight {
        package _ {
            package array {
                
                @python.curried("IdentityL")
                def array_IdentityL() : Optional[List[.Float]] => List[.Float]
                    
                
                
                @python.curried("ChooseTheBest")
                def array_ChooseTheBest() : Optional[List[.Float]] => List[.Float]
                    
            }
            
            
            package trader {
                
                @python.curried("EfficiencyTrend")
                def trader_EfficiencyTrend(alpha : Optional[.Float] = 0.15) : .IAccount => .IFunction[.Float]
                    
                
                
                @python.curried("Efficiency")
                def trader_Efficiency() : .IAccount => .IFunction[.Float]
                    
                
                
                @python.curried("Score")
                def trader_Score() : .IAccount => .IFunction[.Float]
                    
                
                
                @python.curried("Unit")
                def trader_Unit() : .IAccount => .IFunction[.Float]
                    
            }
            
            
            package f {
                
                @python.curried("AtanPow")
                def f_AtanPow(base : Optional[.Float] = 1.002) : Optional[.IFunction[.Float]] => .IFunction[.Float]
                    
                
                
                @python.curried("Clamp0")
                def f_Clamp0() : Optional[.IFunction[.Float]] => .IFunction[.Float]
                    
                
                
                @python.curried("IdentityF")
                def f_IdentityF() : Optional[.IFunction[.Float]] => .IFunction[.Float]
                    
            }
            
        }
        
        
        @python.intrinsic("strategy.weight._ChooseTheBest_Impl")
        @curried("array")
        def ChooseTheBest(array : Optional[List[.Float]] = []) : List[.Float]
            
        
        
        @curried("trader")
        def Efficiency(trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float]
            
            	 = .observable.trader.Efficiency(trader)
        
        
        @python.intrinsic("strategy.weight._Score_Impl")
        @curried("trader")
        def Score(trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float]
            
        
        
        @curried("f")
        def Clamp0(f : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
            
            	 = .observable.Max(.constant(0),f)+1
        
        
        @curried("trader")
        def EfficiencyTrend(trader : .IAccount = .trader.SingleProxy(),
                            alpha : Optional[.Float] = 0.15) : .IFunction[.Float]
            
            	 = .Derivative(.observable.EW.Avg(.observable.trader.Efficiency(trader),alpha))
        
        
        @curried("trader")
        def Unit(trader : .IAccount = .trader.SingleProxy()) : .IFunction[.Float]
            
            	 = .constant(1.0)
        
        
        @curried("f")
        def AtanPow(f : Optional[.IFunction[.Float]] = .constant(),
                    base : Optional[.Float] = 1.002) : .IFunction[.Float]
            
            	 = .mathops.Atan(.mathops.Pow(.constant(base),f))
        
        
        @python.intrinsic("strategy.weight._Identity_Impl")
        @curried("array")
        def IdentityL(array : Optional[List[.Float]] = []) : List[.Float]
            
        
        
        @curried("f")
        def IdentityF(f : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
            
            	 = f
        def efficiency = .strategy.weight._.trader.trader_Efficiency
        
        def score = .strategy.weight._.trader.trader_Score
        
        def atanpow = .strategy.weight._.f.f_AtanPow
        
        def efficiencyTrend = .strategy.weight._.trader.trader_EfficiencyTrend
        
        def clamp0 = .strategy.weight._.f.f_Clamp0
        
        def unit = .strategy.weight._.trader.trader_Unit
        
        def identity_f = .strategy.weight._.f.f_IdentityF
    }
    
    
    @python.intrinsic("strategy.combine._Combine_Impl")
    def Combine(A : Optional[.ISingleAssetStrategy] = .strategy.Noise(),
                B : Optional[.ISingleAssetStrategy] = .strategy.Noise()) : .ISingleAssetStrategy
        
    
    
    def RSI_linear(orderFactory : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.signedVolume_MarketSigned(),
                   alpha : Optional[.Float] = 1.0/14,
                   k : Optional[.IObservable[.Float]] = .const(-0.04),
                   timeframe : Optional[.Float] = 1.0) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.volumefunc.RSI_linear(alpha,k,timeframe)))
    
    /** Dependent price strategy believes that the fair price of an asset *A*
     * is completely correlated with price of another asset *B* and the following relation
     * should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     * It may be considered as a variety of a fundamental value strategy
     * with the exception that it is invoked every the time price of another
     * asset *B* changes.
     */
    
    def PairTrading(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                    /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
                    /** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                    /** multiplier to obtain fair asset price from the reference asset price */ factor : Optional[.Float] = 1.0) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.PairTrading(bookToDependOn,factor)),eventGen)
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     */
    
    @python.intrinsic("strategy.choose_the_best._ChooseTheBest_Impl")
    def ChooseTheBest(/** original strategies that can be suspended */ strategies : Optional[List[.ISingleAssetStrategy]] = [.strategy.Noise()],
                      /** function creating phantom strategy used for efficiency estimation */ account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account._.inner.inner_VirtualMarket(),
                      /** function estimating is the strategy efficient or not */ performance : Optional[.IAccount => .IFunction[.Float]] = .strategy.weight._.trader.trader_EfficiencyTrend()) : .ISingleAssetStrategy
        
    
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    
    def Signal(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
               /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
               /** signal to be listened to */ signal : Optional[.IFunction[.Float]] = .constant(0.0),
               /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.7) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.Signal(signal,threshold)),eventGen)
    
    /** Liquidity provider for two sides
     */
    
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                          /** order factory function*/ orderFactory : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue : Optional[.Float] = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr : Optional[() => .Float] = .mathutils.rnd.lognormvariate(0.0,0.1)) : .ISingleAssetStrategy
        
        	 = .strategy.Array([.strategy.LiquidityProviderSide(eventGen,orderFactory,.side.Sell(),initialValue,priceDistr),.strategy.LiquidityProviderSide(eventGen,orderFactory,.side.Buy(),initialValue,priceDistr)])
    
    /** Two averages strategy compares two averages of price of the same asset but
     * with different parameters ('slow' and 'fast' averages) and when
     * the first is greater than the second one it buys,
     * when the first is lower than the second one it sells
     */
    
    def CrossingAverages(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                         /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
                         /** parameter |alpha| for exponentially weighted moving average 1 */ ewma_alpha_1 : Optional[.Float] = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ ewma_alpha_2 : Optional[.Float] = 0.015,
                         /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.0) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.CrossingAverages(ewma_alpha_1,ewma_alpha_2,threshold)),eventGen)
    
    
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(inner : Optional[.ISingleAssetStrategy] = .strategy.Noise(),
                    predicate : Optional[.IFunction[.Boolean]] = .true() : .IFunction[.Boolean]) : .ISingleAssetStrategy
        
    
    /** Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    
    def TrendFollower(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                      /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha : Optional[.Float] = 0.15,
                      /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.0) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.TrendFollower(ewma_alpha,threshold)),eventGen)
    
    /** Fundamental value strategy believes that an asset should have some specific price
     * (*fundamental value*) and if the current asset price is lower than the fundamental value
     * it starts to buy the asset and if the price is higher it starts to sell the asset.
     */
    
    def FundamentalValue(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                         /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
                         /** defines fundamental value */ fundamentalValue : Optional[.IFunction[.Float]] = .constant(100.0)) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.FundamentalValue(fundamentalValue)),eventGen)
    
    
    @python.intrinsic("strategy.arbitrage._Arbitrage_Impl")
    def Arbitrage() : .IMultiAssetStrategy
        
    
    
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
               /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
               /** parameter |alpha| for exponentially weighted moving average */ alpha : Optional[.Float] = 1.0/14,
               timeframe : Optional[.Float] = 1.0,
               threshold : Optional[.Float] = 30.0) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.Signal(.const(50.0)-.observable.RSI(.observable.orderbook.OfTrader(),timeframe,alpha),50.0-threshold)),eventGen)
    
    
    def TradeIfProfitable(inner : Optional[.ISingleAssetStrategy] = .strategy.Noise(),
                          account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account._.inner.inner_VirtualMarket(),
                          performance : Optional[.IAccount => .IFunction[.Float]] = .strategy.weight._.trader.trader_EfficiencyTrend()) : .ISingleAssetStrategy
        
        	 = .strategy.Suspendable(inner,performance(account(inner))>=0)
    
    
    @python.intrinsic("strategy.combine._Array_Impl")
    def Array(strategies : Optional[List[.ISingleAssetStrategy]] = [] : List[.ISingleAssetStrategy]) : .ISingleAssetStrategy
        
    
    /** Mean reversion strategy believes that asset price should return to its average value.
     * It estimates this average using some functional and
     * if the current asset price is lower than the average
     * it buys the asset and if the price is higher it sells the asset.
     */
    
    def MeanReversion(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                      /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha : Optional[.Float] = 0.15) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.MeanReversion(ewma_alpha)),eventGen)
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * The choice is made randomly among the strategies that have
     * a positive efficiency trend, weighted by the efficiency value.
     */
    
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(/** original strategies that can be suspended */ strategies : Optional[List[.ISingleAssetStrategy]] = [.strategy.Noise()],
                         /** function creating phantom strategy used for efficiency estimation */ account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account._.inner.inner_VirtualMarket(),
                         /** function estimating is the strategy efficient or not */ weight : Optional[.IAccount => .IFunction[.Float]] = .strategy.weight._.trader.trader_EfficiencyTrend(),
                         normalizer : Optional[Optional[.IFunction[.Float]] => .IFunction[.Float]] = .strategy.weight._.f.f_AtanPow(),
                         /** weighting scheme for choosing strategies */ corrector : Optional[Optional[List[.Float]] => List[.Float]] = .strategy.weight._.array.array_IdentityL()) : .ISingleAssetStrategy
        
    
    /** A Strategy that allows to drive the asset price based on historical market data
     *  by creating large volume orders for the given price.
     *
     *  Every time step of 1 in the simulation corresponds to a 1 day in the market data.
     *
     *  At each time step the previous Limit Buy/Sell orders are cancelled and new ones
     *  are created based on the next price of the market data.
     */
    
    def MarketData(/** Ticker of the asset */ ticker : Optional[.String] = "^GSPC",
                   /** Start date in DD-MM-YYYY format */ start : Optional[.String] = "2001-1-1",
                   /** End date in DD-MM-YYYY format */ end : Optional[.String] = "2010-1-1",
                   /** Price difference between orders placed and underlying quotes */ delta : Optional[.Float] = 1.0,
                   /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume : Optional[.Float] = 1000.0) : .ISingleAssetStrategy
        
        	 = .strategy.Combine(.strategy.Generic(.order.Iceberg(.constant(volume),.order.FloatingPrice(.observable.BreaksAtChanges(.observable.Quote(ticker,start,end)+.const(delta)),.order._curried.price_Limit(.side.Sell(),.constant(volume*1000)))),.event.After(.constant(0.0))),.strategy.Generic(.order.Iceberg(.constant(volume),.order.FloatingPrice(.observable.BreaksAtChanges(.observable.Quote(ticker,start,end)-.const(delta)),.order._curried.price_Limit(.side.Buy(),.constant(volume*1000)))),.event.After(.constant(0.0))))
    
    
    @python.intrinsic("strategy.canceller._Canceller_Impl")
    def Canceller(cancellationIntervalDistr : Optional[() => .Float] = .mathutils.rnd.expovariate(1.0)) : .ISingleAssetStrategy
        
    
    /** Liquidity provider for one side
     */
    
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
                              /** order factory function*/ orderFactory : Optional[((() => .Side),(() => .Float)) => .IOrderGenerator] = .order._curried.sideprice_Limit(),
                              /** side of orders to create */ side : Optional[() => .Side] = .side.Sell(),
                              /** initial price which is taken if orderBook is empty */ initialValue : Optional[.Float] = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr : Optional[() => .Float] = .mathutils.rnd.lognormvariate(0.0,0.1)) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(side,.observable.pricefunc.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    /** Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** order factory function*/ orderFactory : Optional[.IOrderGenerator] = .order.Limit(),
                /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .observable.OnEveryDt() : .IEvent) : .ISingleAssetStrategy
        
    
    
    def MarketMaker(delta : Optional[.Float] = 1.0,
                    volume : Optional[.Float] = 20.0) : .ISingleAssetStrategy
        
        	 = .strategy.Combine(.strategy.Generic(.order.Iceberg(.constant(volume),.order.FloatingPrice(.observable.BreaksAtChanges(.observable.OnEveryDt(0.9,.observable.orderbook.SafeSidePrice(.observable.orderbook.Asks(),.constant(100+delta))/.mathops.Exp(.mathops.Atan(.observable.trader.Position())/1000))),.order._curried.price_Limit(.side.Sell(),.constant(volume*1000)))),.event.After(.constant(0.0))),.strategy.Generic(.order.Iceberg(.constant(volume),.order.FloatingPrice(.observable.BreaksAtChanges(.observable.OnEveryDt(0.9,.observable.orderbook.SafeSidePrice(.observable.orderbook.Bids(),.constant(100-delta))/.mathops.Exp(.mathops.Atan(.observable.trader.Position())/1000))),.order._curried.price_Limit(.side.Buy(),.constant(volume*1000)))),.event.After(.constant(0.0))))
    
    /** Noise strategy is a quite dummy strategy that randomly creates an order and sends it to the order book.
     */
    
    def Noise(/** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.mathutils.rnd.expovariate(1.0)),
              /** order factory function*/ orderFactory : Optional[(() => .Side) => .IOrderGenerator] = .order._curried.side_Market()) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.sidefunc.Noise()),eventGen)
    
    
    def Bollinger_linear(orderFactory : Optional[(() => .Float) => .IOrderGenerator] = .order._curried.signedVolume_MarketSigned(),
                         alpha : Optional[.Float] = 0.15,
                         k : Optional[.IObservable[.Float]] = .const(0.5)) : .ISingleAssetStrategy
        
        	 = .strategy.Generic(orderFactory(.observable.volumefunc.Bollinger_linear(alpha,k)))
}

@category = "Trader"
package trader {
    @label = "N/A"
    @python.intrinsic("trader.proxy._Single_Impl")
    def SingleProxy() : .ISingleAssetTrader
        
    
    /** A trader that trades a single asset on a single market
     */
    @label = "%(name)s"
    @python.intrinsic("trader.classes._SingleAsset_Impl")
    def SingleAsset(/** order book for the asset being traded */ orderBook : .IOrderBook,
                    /** strategy run by the trader */ strategy : Optional[.ISingleAssetStrategy] = .strategy.Noise(),
                    name : Optional[.String] = "-trader-",
                    /** current position of the trader (number of assets that it owns) */ amount : Optional[.Float] = 0.0,
                    /** current trader balance (number of money units that it owns) */ PnL : Optional[.Float] = 0.0,
                    timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .ISingleAssetTrader
        
    
    @label = "%(name)s"
    @python.intrinsic("trader.classes._MultiAsset_Impl")
    def MultiAsset(traders : Optional[List[.ISingleAssetTrader]] = [] : List[.ISingleAssetTrader],
                   /** strategy run by the trader */ strategy : Optional[.IMultiAssetStrategy] = .strategy.Arbitrage(),
                   name : Optional[.String] = "-trader-",
                   /** current trader balance (number of money units that it owns) */ PnL : Optional[.Float] = 0.0,
                   timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .ITrader
        
}

@category = "Asset"
package orderbook {
    /** Order book for a single asset in a market.
     * Maintains two order queues for orders of different sides
     */
    @label = "%(name)s"
    @python.intrinsic("orderbook.local._Local_Impl")
    def Local(tickSize : Optional[.Float] = 0.01,
              _digitsToShow : Optional[.Int] = 2,
              name : Optional[.String] = "-orderbook-",
              timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .IOrderBook
        
    
    /** Represents latency in information propagation from one agent to another one
     * (normally between a trader and a market).
     * Ensures that sending packets via a link preserves their order.
     */
    
    @python.intrinsic("orderbook.link._Link_Impl")
    def Link(/** function called for each packet in order to determine
               * when it will appear at the end point*/ latency : Optional[.IObservable[.Float]] = .const(0.001)) : .ILink
        
    
    /** Represents latency in information propagation between two agents
     * (normally between a trader and a market).
     * Ensures that sending packets via links preserves their order.
     * Holds two one-way links in opposite directions.
     */
    
    @python.intrinsic("orderbook.link._TwoWayLink_Impl")
    def TwoWayLink(/** Forward link (normally from a trader to a market)*/ up : Optional[.ILink] = .orderbook.Link(),
                   /** Backward link (normally from a market to a trader)*/ down : Optional[.ILink] = .orderbook.Link()) : .ITwoWayLink
        
    
    /** Represent an *orderbook* from point of view of a remote trader connected
     * to the market by means of a *link* that introduces some latency in information propagation
     */
    @label = "%(orderbook)s.name^remote"
    @python.intrinsic("orderbook.remote._Remote_Impl")
    def Remote(orderbook : Optional[.IOrderBook] = .orderbook.Local(),
               link : Optional[.ITwoWayLink] = .orderbook.TwoWayLink(),
               timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .IOrderBook
        
}

@category = "Basic"
package observable {@category = "Price function"
    package pricefunc {
        
        def LiquidityProvider(side : Optional[() => .Side] = .side.Sell(),
                              initialValue : Optional[.Float] = 100.0,
                              priceDistr : Optional[() => .Float] = .mathutils.rnd.lognormvariate(0.0,0.1),
                              book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Float]
            
            	 = .observable.orderbook.SafeSidePrice(.observable.orderbook.Queue(book,side),.constant(initialValue))*priceDistr
    }
    
    @category = "Side function"
    package sidefunc {
        
        def PairTrading(dependee : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                        factor : Optional[.Float] = 1.0,
                        book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Side]
            
            	 = .observable.ObservableSide(.observable.sidefunc.FundamentalValue(.observable.orderbook.MidPrice(dependee)*.const(factor),book))
        
        
        @python.observable()
        def Signal(signal : Optional[.IFunction[.Float]] = .constant(),
                   threshold : Optional[.Float] = 0.7) : () => .Side
            
            	 = if signal>.const(threshold) then .side.Buy() else if signal<.const(0-threshold) then .side.Sell() else .side.Nothing()
        
        
        def CrossingAverages(alpha_1 : Optional[.Float] = 0.015,
                             alpha_2 : Optional[.Float] = 0.15,
                             threshold : Optional[.Float] = 0.0,
                             book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : () => .Side
            
            	 = .observable.sidefunc.Signal(.observable.EW.Avg(.observable.orderbook.MidPrice(book),alpha_1)-.observable.EW.Avg(.observable.orderbook.MidPrice(book),alpha_2),threshold)
        
        
        def TrendFollower(alpha : Optional[.Float] = 0.015,
                          threshold : Optional[.Float] = 0.0,
                          book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : () => .Side
            
            	 = .observable.sidefunc.Signal(.Derivative(.observable.EW.Avg(.observable.orderbook.MidPrice(book),alpha)),threshold)
        
        
        @python.observable()
        def FundamentalValue(fv : Optional[.IFunction[.Float]] = .constant(200.0),
                             book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : () => .Side
            
            	 = if .observable.orderbook.BidPrice(book)>fv then .side.Sell() else if .observable.orderbook.AskPrice(book)<fv then .side.Buy() else .side.Nothing()
        
        
        def MeanReversion(alpha : Optional[.Float] = 0.015,
                          book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : () => .Side
            
            	 = .observable.sidefunc.FundamentalValue(.observable.EW.Avg(.observable.orderbook.MidPrice(book),alpha),book)
        
        
        def Noise(side_distribution : Optional[.IFunction[.Float]] = .mathutils.rnd.uniform(0.0,1.0) : .IFunction[.Float]) : () => .Side
            
            	 = if side_distribution>.const(0.5) then .side.Sell() else .side.Buy()
    }
    
    
    package Cumulative {
        @label = "Min_{\\epsilon}(%(source)s)"
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        def MinEpsilon(source : Optional[.IFunction[.Float]] = .constant(),
                       epsilon : Optional[.IFunction[.Float]] = .constant(0.01)) : .IObservable[.Float]
            
        
        @label = "Max_{\\epsilon}(%(source)s)"
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        def MaxEpsilon(source : Optional[.IFunction[.Float]] = .constant(),
                       epsilon : Optional[.IFunction[.Float]] = .constant(0.01)) : .IObservable[.Float]
            
    }
    
    @category = "RSI"
    package rsi {
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(source : Optional[.IObservable[.Float]] = .const(),
                timeframe : Optional[.Float] = 10.0,
                alpha : Optional[.Float] = 0.015) : .IFunction[.Float]
            
            	 = .observable.EW.Avg(.observable.UpMovements(source,timeframe),alpha)/.observable.EW.Avg(.observable.DownMovements(source,timeframe),alpha)
    }
    
    @category = "MACD"
    package macd {
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
        def MACD(x : Optional[.IObservable[.Float]] = .const(),
                 slow : Optional[.Float] = 26.0,
                 fast : Optional[.Float] = 12.0) : .IFunction[.Float]
            
            	 = .observable.EW.Avg(x,2.0/(fast+1))-.observable.EW.Avg(x,2.0/(slow+1))
        
        @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Signal(x : Optional[.IObservable[.Float]] = .const(),
                   slow : Optional[.Float] = 26.0,
                   fast : Optional[.Float] = 12.0,
                   timeframe : Optional[.Float] = 9.0,
                   step : Optional[.Float] = 1.0) : .IDifferentiable
            
            	 = .observable.EW.Avg(.observable.OnEveryDt(step,.observable.macd.MACD(x,slow,fast)),2/(timeframe+1))
        
        @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Histogram(x : Optional[.IObservable[.Float]] = .const(),
                      slow : Optional[.Float] = 26.0,
                      fast : Optional[.Float] = 12.0,
                      timeframe : Optional[.Float] = 9.0,
                      step : Optional[.Float] = 1.0) : .IFunction[.Float]
            
            	 = .observable.macd.MACD(x,slow,fast)-.observable.macd.Signal(x,slow,fast,timeframe,step)
    }
    
    @category = "Trader's"
    package trader {
        
        @python.intrinsic("trader.props.Balance_Impl")
        def Balance(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Price]
            
        
        
        def RoughPnL(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
            
            	 = .observable.Observable(.observable.trader.Balance(trader)+.observable.orderbook.NaiveCumulativePrice(.observable.orderbook.OfTrader(trader),.observable.trader.Position(trader)))
        
        
        @python.intrinsic("trader.props.Position_Impl")
        def Position(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Volume]
            
        
        
        def Efficiency(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
            
            	 = .observable.Observable(.observable.trader.Balance(trader)+.observable.orderbook.CumulativePrice(.observable.orderbook.OfTrader(trader),.observable.trader.Position(trader)))
        
        
        def EfficiencyTrend(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount,
                            alpha : Optional[.Float] = 0.15) : () => .Float
            
            	 = .Derivative(.observable.EW.Avg(.observable.trader.Efficiency(trader),alpha))
        
        
        @python.intrinsic("trader.props.PendingVolume_Impl")
        def PendingVolume(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Volume]
            
        def SingleProxy = .trader.SingleProxy
    }
    
    @category = "Volume function"
    package volumefunc {
        
        def DesiredPosition(desiredPosition : Optional[.IObservable[.Float]] = .const(),
                            trader : Optional[.ISingleAssetTrader] = .trader.SingleProxy()) : .IObservable[.Volume]
            
            	 = .observable.ObservableVolume(desiredPosition-.observable.trader.Position(trader)-.observable.trader.PendingVolume(trader))
        
        
        def RSI_linear(alpha : Optional[.Float] = 1.0/14.0,
                       k : Optional[.IObservable[.Float]] = .const(-0.04),
                       timeframe : Optional[.Float] = 1.0,
                       trader : Optional[.ISingleAssetTrader] = .trader.SingleProxy()) : .IObservable[.Volume]
            
            	 = .observable.volumefunc.DesiredPosition(.observable.OnEveryDt(1.0,.const(50.0)-.observable.RSI(.observable.orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
        
        
        def Bollinger_linear(alpha : Optional[.Float] = 0.15,
                             k : Optional[.IObservable[.Float]] = .const(0.5),
                             trader : Optional[.ISingleAssetTrader] = .trader.SingleProxy()) : .IObservable[.Volume]
            
            	 = .observable.volumefunc.DesiredPosition(.observable.OnEveryDt(1.0,.observable.EW.RelStdDev(.observable.orderbook.MidPrice(.observable.orderbook.OfTrader(trader)),alpha))*k,trader)
    }
    
    @category = "Asset's"
    package orderbook {
        
        @python.observable()
        def SafeSidePrice(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks(),
                          defaultValue : Optional[.IFunction[.Float]] = .constant(100.0)) : .IObservable[.Price]
            
            	 = .observable.ObservablePrice(.IfDefined(.observable.orderbook.BestPrice(queue),.IfDefined(.observable.orderbook.LastPrice(queue),defaultValue)))
        
        @label = "Price_{%(alpha)s}^{%(queue)s}"
        def WeightedPrice(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks(),
                          alpha : Optional[.Float] = 0.015) : .IFunction[.Float]
            
            	 = .observable.EW.Avg(.observable.orderbook.LastTradePrice(queue)*.observable.orderbook.LastTradeVolume(queue),alpha)/.observable.EW.Avg(.observable.orderbook.LastTradeVolume(queue),alpha)
        
        
        @python.intrinsic("orderbook.props._TickSize_Impl")
        def TickSize(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : () => .Price
            
        
        @label = "LastAsk_{%(book)s}"
        def AskLastPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.LastPrice(.observable.orderbook.Asks(book))
        
        
        def BidLastTradePrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.LastTradePrice(.observable.orderbook.Bids(book))
        
        @label = "Ask_{%(alpha)s}^{%(book)s}"
        def AskWeightedPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                             alpha : Optional[.Float] = 0.015) : .IFunction[.Float]
            
            	 = .observable.orderbook.WeightedPrice(.observable.orderbook.Asks(book),alpha)
        
        
        def MidPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.ObservablePrice((.observable.orderbook.AskPrice(book)+.observable.orderbook.BidPrice(book))/.const(2.0))
        
        
        @python.intrinsic("orderbook.proxy._Asks_Impl")
        def Asks(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IOrderQueue
            
            	 = .observable.orderbook.Queue(book,.side.Sell())
        
        @label = "Bid_{%(alpha)s}^{%(book)s}"
        def BidWeightedPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                             alpha : Optional[.Float] = 0.015) : .IFunction[.Float]
            
            	 = .observable.orderbook.WeightedPrice(.observable.orderbook.Bids(book),alpha)
        
        @label = "Ask_{%(book)s}"
        def AskPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.BestPrice(.observable.orderbook.Asks(book))
        
        
        @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks()) : .IObservable[.Volume]
            
        
        @label = "Bid^{%(book)s}"
        def BidPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.BestPrice(.observable.orderbook.Bids(book))
        
        
        @python.intrinsic("orderbook.proxy._Bids_Impl")
        def Bids(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IOrderQueue
            
            	 = .observable.orderbook.Queue(book,.side.Buy())
        
        
        @python.intrinsic("orderbook.props._BestPrice_Impl")
        def BestPrice(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks()) : .IObservable[.Price]
            
        
        
        @python.intrinsic("orderbook.proxy._Queue_Impl")
        def Queue(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                  side : Optional[() => .Side] = .side.Sell()) : .IOrderQueue
            
        
        @label = "N/A"
        @python.intrinsic("orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IOrderBook
            
        
        
        def AskLastTradePrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.LastTradePrice(.observable.orderbook.Asks(book))
        
        @label = "LastBid^{%(book)s}"
        def BidLastPrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.orderbook.LastPrice(.observable.orderbook.Bids(book))
        
        
        @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
        def CumulativePrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                            depth : Optional[.IFunction[.Float]] = .constant()) : .IObservable[.Price]
            
        
        @label = "VolumeLevels(%(queue)s)"
        @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
        def VolumeLevels(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks(),
                         volumeDelta : Optional[.Float] = 30.0,
                         volumeCount : Optional[.Int] = 10) : .IFunction[.VolumeLevels]
            
        
        
        @python.intrinsic("orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks()) : .IObservable[.Price]
            
        
        
        def NaiveCumulativePrice(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
                                 depth : Optional[.IFunction[.Float]] = .constant()) : .IObservable[.Price]
            
            	 = .observable.ObservablePrice(if depth<.const(0.0) then depth*.observable.orderbook.AskPrice(book) else if depth>.const(0.0) then depth*.observable.orderbook.BidPrice(book) else .const(0.0))
        
        
        def Spread(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader()) : .IObservable[.Price]
            
            	 = .observable.ObservablePrice(.observable.orderbook.AskPrice(book)-.observable.orderbook.BidPrice(book))
        
        
        @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue : Optional[.IOrderQueue] = .observable.orderbook.Asks()) : .IObservable[.Price]
            
    }
    
    
    package Moving {
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        @python.intrinsic("observable.minmax.Min_Impl")
        def Min(source : Optional[.IFunction[.Float]] = .constant(),
                timeframe : Optional[.Float] = 100.0) : .IObservable[.Float]
            
        
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        @python.intrinsic("observable.minmax.Max_Impl")
        def Max(source : Optional[.IFunction[.Float]] = .constant(),
                timeframe : Optional[.Float] = 100.0) : .IObservable[.Float]
            
    }
    @category = "Statistics"
    package  {
        package EW {
            @label = "Avg_{\\alpha=%(alpha)s}(%(source)s)"
            @python.intrinsic("moments.ewma.EWMA_Impl")
            def Avg(source : Optional[.IObservable[.Float]] = .const(),
                    alpha : Optional[.Float] = 0.015) : .IDifferentiable
                
            
            @label = "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}"
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            def Var(source : Optional[.IObservable[.Float]] = .const(),
                    alpha : Optional[.Float] = 0.015) : () => .Float
                
            
            @label = "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}"
            def StdDev(source : Optional[.IObservable[.Float]] = .const(),
                       alpha : Optional[.Float] = 0.015) : () => .Float
                
                	 = .mathops.Sqrt(.observable.EW.Var(source,alpha))
            
            @label = "RSD_{\\alpha=%(alpha)s}_{%(source)s}"
            def RelStdDev(source : Optional[.IObservable[.Float]] = .const(),
                          alpha : Optional[.Float] = 0.15) : .IObservable[.Float]
                
                	 = (source-.observable.EW.Avg(source,alpha))/.observable.EW.StdDev(source,alpha)
        }
        
        
        package Cumulative {
            @label = "Avg_{cumul}(%(source)s)"
            @python.intrinsic("moments.cma.CMA_Impl")
            def Avg(source : Optional[.IObservable[.Float]] = .const()) : () => .Float
                
            
            @label = "\\sigma^2_{cumul}(%(source)s)"
            @python.intrinsic("moments.cmv.Variance_Impl")
            def Var(source : Optional[.IObservable[.Float]] = .const()) : () => .Float
                
            
            @label = "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}"
            def StdDev(source : Optional[.IObservable[.Float]] = .const()) : () => .Float
                
                	 = .mathops.Sqrt(.observable.Cumulative.Var(source))
            
            @label = "RSD_{cumul}_{%(source)s}"
            def RelStdDev(source : Optional[.IObservable[.Float]] = .const()) : .IObservable[.Float]
                
                	 = (source-.observable.Cumulative.Avg(source))/.observable.Cumulative.StdDev(source)
        }
        
        
        package Moving {
            @label = "Avg_{n=%(timeframe)s}(%(source)s)"
            @python.intrinsic("moments.ma.MA_Impl")
            def Avg(source : Optional[.IObservable[.Float]] = .const(),
                    timeframe : Optional[.Float] = 100.0) : () => .Float
                
            
            @label = "\\sigma^2_{n=%(timeframe)s}(%(source)s)"
            @python.intrinsic("moments.mv.MV_Impl")
            def Var(source : Optional[.IObservable[.Float]] = .const(),
                    timeframe : Optional[.Float] = 100.0) : .IFunction[.Float]
                
                	 = .observable.Max(.const(0),.observable.Moving.Avg(source*source,timeframe)-.observable.Sqr(.observable.Moving.Avg(source,timeframe)))
            
            @label = "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}"
            def StdDev(source : Optional[.IObservable[.Float]] = .const(),
                       timeframe : Optional[.Float] = 100.0) : () => .Float
                
                	 = .mathops.Sqrt(.observable.Moving.Var(source))
            
            @label = "RSD_{n=%(timeframe)s}_{%(source)s}"
            def RelStdDev(source : Optional[.IObservable[.Float]] = .const(),
                          timeframe : Optional[.Float] = 100.0) : .IObservable[.Float]
                
                	 = (source-.observable.Moving.Avg(source,timeframe))/.observable.Moving.StdDev(source,timeframe)
        }
        
    }
    
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt : Optional[.Float] = 1.0,
                  x : Optional[.IFunction[.Float]] = .constant()) : .IObservable[.Float]
        
    
    @label = "min{%(x)s, %(y)s}"
    @python.observable()
    def Min(x : Optional[.IFunction[.Float]] = .constant(),
            y : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
        
        	 = if x<y then x else y
    
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(source : Optional[.IObservable[.Float]] = .const(),
                      timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
        
        	 = .observable.Observable(.observable.Max(.const(0.0),.observable.Lagged(source,timeframe)-source))
    
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    @python.intrinsic("observable.lagged.Lagged_Impl")
    def Lagged(source : Optional[.IObservable[.Float]] = .const(),
               timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
        
    
    
    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source : Optional[.IFunction[.Float]] = .constant(1.0)) : .IObservable[.Float]
        
    
    @label = "max{%(x)s, %(y)s}"
    @python.observable()
    def Max(x : Optional[.IFunction[.Float]] = .constant(),
            y : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
        
        	 = if x>y then x else y
    
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(source : Optional[.IObservable[.Float]] = .const(),
                    timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
        
        	 = .observable.Observable(.observable.Max(.const(0.0),source-.observable.Lagged(source,timeframe)))
    
    @category = "Pow/Log"
    @label = "{%(x)s}^2"
    @python.observable()
    def Sqr(x : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
        
        	 = x*x
    
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(book : Optional[.IOrderBook] = .observable.orderbook.OfTrader(),
            timeframe : Optional[.Float] = 10.0,
            alpha : Optional[.Float] = 0.015) : .IObservable[.Float]
        
        	 = .const(100.0)-.const(100.0)/(.const(1.0)+.observable.rsi.Raw(.observable.orderbook.MidPrice(book),timeframe,alpha))
    
    @label = "[%(x)s]"
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    def ObservableVolume(x : Optional[.IFunction[.Float]] = .const() : .IFunction[.Float]) : .IObservable[.Volume]
        
    
    /** A discrete signal with user-defined increments.
     */
    @label = "%(name)s"
    @python.intrinsic("observable.randomwalk._RandomWalk_Impl")
    def RandomWalk(/** initial value of the signal */ initialValue : Optional[.Float] = 0.0,
                   /** increment function */ deltaDistr : Optional[() => .Float] = .mathutils.rnd.normalvariate(0.0,1.0),
                   /** intervals between signal updates */ intervalDistr : Optional[() => .Float] = .mathutils.rnd.expovariate(1.0),
                   name : Optional[.String] = "-random-") : .IObservable[.Float]
        
    
    @label = "[%(x)s]"
    @python.intrinsic("observable.on_every_dt._ObservableSide_Impl")
    def ObservableSide(x : Optional[.IFunction[.Side]] = .side.Sell() : .IFunction[.Side]) : .IObservable[.Side]
        
    
    @label = "%(ticker)s"
    @python.intrinsic("observable.quote.Quote_Impl")
    def Quote(ticker : Optional[.String] = "^GSPC",
              start : Optional[.String] = "2001-1-1",
              end : Optional[.String] = "2010-1-1") : .IObservable[.Price]
        
    
    @label = "Candles_{%(source)s}"
    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    def CandleSticks(source : Optional[.IObservable[.Float]] = .const(),
                     timeframe : Optional[.Float] = 10.0) : .IObservable[.CandleStick]
        
    
    @label = "[%(x)s]"
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    def ObservablePrice(x : Optional[.IFunction[.Float]] = .const() : .IFunction[.Float]) : .IObservable[.Price]
        
    
    @label = "[%(x)s]"
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    def Observable(x : Optional[.IFunction[.Float]] = .const() : .IFunction[.Float]) : .IObservable[.Float]
        
}

@python = "no"
package trash {
    package types {
        package  {
            package  {type U : T, R
            }
            type T
            type R : T
        }
        type T1 = T
    }
    
    
    package in1 {
        package in2 {
            
            def S1(y : Optional[.String] = "abc") : .String
                
                	 = y
            
            
            def F(x : Optional[.IFunction[.Float]] = .trash.in1.in2.IntFunc() : .IFunction[.Float]) : .IFunction[.Float]
                
                	 = x
            
            
            def A(x : Optional[.IFunction[.Float]] = .constant(),
                  y : Optional[.IFunction[.Float]] = if 3>x+2 then x else x*2) : () => .trash.types.T
                
            
            
            def IntObs() : .IObservable[.Int]
                
            
            
            def IntFunc() : .IFunction[.Int]
                
            
            
            def C(x : .IFunction[.CandleStick],
                  p : Optional[List[.Float]] = [12,23.2,0]) : List[.Float]
                
                	 = p
            
            
            def S2() : Optional[.String]
                
                	 = .trash.in1.in2.S1()
            
            
            def O(x : Optional[.IObservable[.Float]] = .trash.in1.in2.IntObs() : .IObservable[.Float]) : .IObservable[.Float]
                
                	 = x
        }
        
        
        def A(x : () => .trash.types.T1 = .trash.A()) : () => .trash.types.U
            
    }
    
    
    def A(x : Optional[() => .trash.types.T] = .trash.in1.in2.A()) : () => .trash.types.R
        
}
@category = "Basic"
package  {
    @label = "C=%(x)s"
    def constant(x : Optional[.Float] = 1.0) : .IFunction[.Float]
        
        	 = .const(x)
    
    @label = "False"
    @python.intrinsic.function("_constant._False_Impl")
    def false() : .IObservable[.Boolean]
        
    
    
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => .Float
        
    
    @label = "%(source)s"
    @python.intrinsic("timeserie._ToRecord_Impl")
    def TimeSerie(source : Optional[.IObservable[Any]] = .const(0.0) : .IObservable[Any],
                  graph : Optional[.IGraph] = .veusz.Graph(),
                  _digitsToShow : Optional[.Int] = 4) : .ITimeSerie
        
    
    @label = "C=%(x)s"
    @python.intrinsic.function("_constant._Constant_Impl")
    def const(x : Optional[.Float] = 1.0) : .IObservable[.Float]
        
    
    @label = "True"
    @python.intrinsic.function("_constant._True_Impl")
    def true() : .IObservable[.Boolean]
        
    
    @label = "\\frac{d%(x)s}{dt}"
    @python.intrinsic("observable.derivative._Derivative_Impl")
    def Derivative(x : Optional[.IDifferentiable] = .observable.EW.Avg() : .IDifferentiable) : () => .Float
        
    
    @label = "If def(%(x)s) else %(elsePart)s"
    @python.observable()
    def IfDefined(x : Optional[.IFunction[.Float]] = .constant(),
                  elsePart : Optional[.IFunction[.Float]] = .constant()) : .IFunction[.Float]
        
        	 = if x<>.null() then x else elsePart
    
    @label = "%(source)s"
    @python.intrinsic("timeserie._VolumeLevels_Impl")
    def volumeLevels(source : Optional[.IObservable[Any]] = .const(0.0) : .IObservable[Any],
                     graph : Optional[.IGraph] = .veusz.Graph(),
                     _digitsToShow : Optional[.Int] = 4) : .ITimeSerie
        
    def EWMA = .observable.EW.Avg
}
type ITrader
type IGraph
type CandleStick
type Volume : Int
type Optional[T]
type IAccount
type Side
type Boolean
type Price : Float
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
type Order
type List[T]
type IDifferentiable : IFunction[Float]
type VolumeLevels
type ITimeSerie
type Any
type IOrderGenerator = IObservable[Order]
type String
