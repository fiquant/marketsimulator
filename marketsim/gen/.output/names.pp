@category = "Side"

package side {
    @python.intrinsic("side._Sell_Impl")
    def Sell() : () => Side
        
    
    @python.intrinsic("side._Buy_Impl")
    def Buy() : () => Side
        
    
    @python.intrinsic("side._Buy_Impl")
    def Nothing() : () => Side
        
}

package mathops {@category = "Trigonometric"
    
    package  {
        /** Arc tangent of x, in radians.
         *
         */
        @python.mathops("atan")
        def Atan(x = constant(0.0)) : () => Float
            
    }
    @category = "Log/Pow"
    
    package  {
        /** Exponent of x
         *
         */
        @python.mathops("exp")
        @label = "e^{%(x)s}"
        def Exp(x = constant(1.0)) : () => Float
            
        
        /** Natural logarithm of x (to base e)
         *
         */
        @python.mathops("log")
        @label = "log(%(x)s)"
        def Log(x = constant(1.0)) : () => Float
            
        
        /** Square root of x
         *
         */
        @python.mathops("sqrt")
        @label = "\\sqrt{%(x)s}"
        def Sqrt(x = constant(1.0)) : () => Float
            
        
        /** Return *x* raised to the power *y*.
         *
         * Exceptional cases follow Annex F of the C99 standard as far as possible.
         * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
         * even when *x* is a zero or a NaN.
         * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
         * ``pow(x, y)`` is undefined, and raises ``ValueError``.
         */
        @python.mathops("pow")
        @label = "%(base)s^{%(power)s}"
        def Pow(base = constant(1.0),
                power = constant(1.0)) : () => Float
            
    }
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
        def side_ImmediateOrCancel(proto = .order._.side.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.curried("price_Limit")
        def volume_price_Limit(side = .side.Sell()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("Iceberg")
        def sidevolume_Iceberg(lotSize = .const(10.0),
                               proto = .order._.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def sidevolume_WithExpiry(expiry = .const(10.0),
                                  proto = .order._.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_StopLoss")
        def side_price_StopLoss(maxloss = .const(0.1),
                                proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("Iceberg")
        def price_Iceberg(lotSize = .const(10.0),
                          proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def sideprice_FloatingPrice(floatingPrice = .constant(10.0),
                                    proto = .order._.side.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("StopLoss")
        def price_StopLoss(maxloss = .const(0.1),
                           proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def price_ImmediateOrCancel(proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_WithExpiry")
        def volume_price_WithExpiry(expiry = .const(10.0),
                                    proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("StopLoss")
        def sideprice_StopLoss(maxloss = .const(0.1),
                               proto = .order._.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def volumeprice_FloatingPrice(floatingPrice = .constant(10.0),
                                      proto = .order._.volume.price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_Peg")
        def volume_price_Peg(proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("Iceberg")
        def side_Iceberg(lotSize = .const(10.0),
                         proto = .order._.side.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_WithExpiry")
        def sidevolume_price_WithExpiry(expiry = .const(10.0),
                                        proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("Peg")
        def volume_Peg(proto = .order._.volume.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sidevolume_ImmediateOrCancel(proto = .order._.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.curried("FixedBudget")
        def side_FixedBudget(budget = .constant(1000.0)) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.curried("Limit")
        def sideprice_Limit(volume = .constant(1.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Peg")
        def sideprice_Peg(proto = .order._.side.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Peg")
        def sidevolume_Peg(proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Peg")
        def side_Peg(proto = .order._.side.price.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.curried("LimitSigned")
        def signedVolume_LimitSigned(price = .constant(100.0)) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_Iceberg")
        def side_price_Iceberg(lotSize = .const(10.0),
                               proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("WithExpiry")
        def volumeprice_WithExpiry(expiry = .const(10.0),
                                   proto = .order._.volume_price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def side_price_ImmediateOrCancel(proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def volumeprice_ImmediateOrCancel(proto = .order._.volume_price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def side_WithExpiry(expiry = .const(10.0),
                            proto = .order._.side.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("StopLoss")
        def side_StopLoss(maxloss = .const(0.1),
                          proto = .order._.side.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_StopLoss")
        def sidevolume_price_StopLoss(maxloss = .const(0.1),
                                      proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("StopLoss")
        def pricevolume_StopLoss(maxloss = .const(0.1),
                                 proto = .order._.price_volume.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def pricevolume_ImmediateOrCancel(proto = .order._.price_volume.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Peg")
        def pricevolume_Peg(proto = .order._.volume.price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Peg")
        def price_Peg(proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("StopLoss")
        def volume_StopLoss(maxloss = .const(0.1),
                            proto = .order._.volume.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.curried("Limit")
        def volumeprice_Limit(side = .side.Sell()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.curried("price_Limit")
        def sidevolume_price_Limit() : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("StopLoss")
        def sidevolume_StopLoss(maxloss = .const(0.1),
                                proto = .order._.side_volume.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Iceberg")
        def volumeprice_Iceberg(lotSize = .const(10.0),
                                proto = .order._.volume_price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def volume_WithExpiry(expiry = .const(10.0),
                              proto = .order._.volume.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def sideprice_WithExpiry(expiry = .const(10.0),
                                 proto = .order._.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def volume_ImmediateOrCancel(proto = .order._.volume.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def volume_FloatingPrice(floatingPrice = .constant(10.0),
                                 proto = .order._.volume.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.curried("Market")
        def volume_Market(side = .side.Sell()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_StopLoss")
        def volume_price_StopLoss(maxloss = .const(0.1),
                                  proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def volume_price_ImmediateOrCancel(proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("Limit")
        def side_Limit(price = .constant(100.0),
                       volume = .constant(1.0)) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def side_price_FloatingPrice(floatingPrice = .constant(10.0),
                                     proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def side_FloatingPrice(floatingPrice = .constant(10.0),
                               proto = .order._.side.price.Limit()) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Iceberg")
        def pricevolume_Iceberg(lotSize = .const(10.0),
                                proto = .order._.price_volume.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_WithExpiry")
        def side_price_WithExpiry(expiry = .const(10.0),
                                  proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("price_Limit")
        def side_price_Limit(volume = .constant(1.0)) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("Limit")
        def pricevolume_Limit(side = .side.Sell()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Iceberg")
        def volume_Iceberg(lotSize = .const(10.0),
                           proto = .order._.volume.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def volume_price_FloatingPrice(floatingPrice = .constant(10.0),
                                       proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("Market")
        def side_Market(volume = .constant(1.0)) : (() => .Side) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def price_FloatingPrice(floatingPrice = .constant(10.0),
                                proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def sidevolume_FloatingPrice(floatingPrice = .constant(10.0),
                                     proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("StopLoss")
        def volumeprice_StopLoss(maxloss = .const(0.1),
                                 proto = .order._.volume_price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def price_WithExpiry(expiry = .const(10.0),
                             proto = .order._.price.Limit()) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_Iceberg")
        def volume_price_Iceberg(lotSize = .const(10.0),
                                 proto = .order._.volume.price.Limit()) : (() => .Float) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def sidevolume_price_FloatingPrice(floatingPrice = .constant(10.0),
                                           proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("Peg")
        def volumeprice_Peg(proto = .order._.volume.price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def sidevolume_price_ImmediateOrCancel(proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("Market")
        def sidevolume_Market() : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.curried("Limit")
        def price_Limit(side = .side.Sell(),
                        volume = .constant(1.0)) : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.curried("Limit")
        def sidevolume_Limit(price = .constant(100.0)) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("Iceberg")
        def sideprice_Iceberg(lotSize = .const(10.0),
                              proto = .order._.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_Peg")
        def sidevolume_price_Peg(proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("MarketSigned")
        def signedVolume_MarketSigned() : (() => .Float) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("FloatingPrice")
        def pricevolume_FloatingPrice(floatingPrice = .constant(10.0),
                                      proto = .order._.volume.price.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sideprice_ImmediateOrCancel(proto = .order._.side_price.Limit()) : ((() => .Side),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("WithExpiry")
        def pricevolume_WithExpiry(expiry = .const(10.0),
                                   proto = .order._.price_volume.Limit()) : ((() => .Float),(() => .Float)) => .IOrderGenerator
            
        
        @python.order.factory.on_proto("price_Peg")
        def side_price_Peg(proto = .order._.side.price.Limit()) : (() => .Side) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.on_proto("price_Iceberg")
        def sidevolume_price_Iceberg(lotSize = .const(10.0),
                                     proto = .order._.side_volume.price.Limit()) : ((() => .Side),(() => .Float)) => ((() => .Float) => .IOrderGenerator)
            
        
        @python.order.factory.curried("Limit")
        def volume_Limit(side = .side.Sell(),
                         price = .constant(100.0)) : (() => .Float) => .IOrderGenerator
            
    }
    
    @python.order.factory("order.limit.Order_Impl")
    def Limit(side = side.Sell(),
              price = constant(100.0),
              volume = constant(1.0)) : IOrderGenerator
        
    
    @python.order.factory("order.market.Order_Impl")
    def MarketSigned(/**signed volume*/ signedVolume : () => Float = constant(1.0)) : .IOrderGenerator
        
    
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.market.Order_Impl")
    def Market(side = side.Sell(),
               volume = constant(1.0)) : IOrderGenerator
        
    
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(maxloss = const(0.1),
                 proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(expiry = const(10.0),
                   proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(floatingPrice = constant(10.0),
                      proto = _.price.Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(lotSize = const(10.0),
                proto = Limit()) : IOrderGenerator
        
    
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(side = side.Sell(),
                    budget = constant(1000.0)) : IOrderGenerator
        
    
    @python.order.factory("order.limit.Order_Impl")
    def LimitSigned(/**signed volume*/ signedVolume : () => Float = constant(1.0),
                    price = constant(100.0)) : .IOrderGenerator
        
    
    @python.order.factory("order.meta.peg.Factory_Impl")
    def Peg(proto = _.price.Limit()) : IOrderGenerator
        
}
@category = "Strategy"

package strategy {
    @python.intrinsic("strategy.combine._Combine_Impl")
    def Combine(A = Noise(),
                B = Noise()) : ISingleAssetStrategy
        
    
    def RSI_linear(orderFactory = order._.signedVolume.MarketSigned(),
                   alpha = 1.0/14,
                   k = const(-0.04),
                   timeframe = 1.0)
         = Generic(orderFactory(observable.volumefunc.RSI_linear(alpha,k,timeframe)))
    
    /** Dependent price strategy believes that the fair price of an asset *A*
     * is completely correlated with price of another asset *B* and the following relation
     * should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     * It may be considered as a variety of a fundamental value strategy
     * with the exception that it is invoked every the time price of another
     * asset *B* changes.
     */
    def PairTrading(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                    /** order factory function*/ orderFactory = order._.side.Market(),
                    /** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn = observable.orderbook.OfTrader(),
                    /** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0)
         = Generic(orderFactory(observable.sidefunc.PairTrading(bookToDependOn,factor)),eventGen)
    
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    def Signal(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
               /** order factory function*/ orderFactory = order._.side.Market(),
               /** signal to be listened to */ signal = constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7)
         = Generic(orderFactory(observable.sidefunc.Signal(signal,threshold)),eventGen)
    
    /** Two averages strategy compares two averages of price of the same asset but
     * with different parameters ('slow' and 'fast' averages) and when
     * the first is greater than the second one it buys,
     * when the first is lower than the second one it sells
     */
    def CrossingAverages(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                         /** order factory function*/ orderFactory = order._.side.Market(),
                         /** parameter |alpha| for exponentially weighted moving average 1 */ ewma_alpha_1 = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ ewma_alpha_2 = 0.015,
                         /** threshold when the trader starts to act */ threshold = 0.0)
         = Generic(orderFactory(observable.sidefunc.CrossingAverages(ewma_alpha_1,ewma_alpha_2,threshold)),eventGen)
    
    /** Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    def TrendFollower(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                      /** order factory function*/ orderFactory = order._.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15,
                      /** threshold when the trader starts to act */ threshold = 0.0)
         = Generic(orderFactory(observable.sidefunc.TrendFollower(ewma_alpha,threshold)),eventGen)
    
    /** Fundamental value strategy believes that an asset should have some specific price
     * (*fundamental value*) and if the current asset price is lower than the fundamental value
     * it starts to buy the asset and if the price is higher it starts to sell the asset.
     */
    def FundamentalValue(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                         /** order factory function*/ orderFactory = order._.side.Market(),
                         /** defines fundamental value */ fundamentalValue = constant(100.0))
         = Generic(orderFactory(observable.sidefunc.FundamentalValue(fundamentalValue)),eventGen)
    
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
               /** order factory function*/ orderFactory = order._.side.Market(),
               /** parameter |alpha| for exponentially weighted moving average */ alpha = 1.0/14,
               timeframe = 1.0,
               threshold = 30.0)
         = Generic(orderFactory(observable.sidefunc.Signal(50.0-observable.RSI(observable.orderbook.OfTrader(),timeframe,alpha),50.0-threshold)),eventGen)
    
    /** Mean reversion strategy believes that asset price should return to its average value.
     * It estimates this average using some functional and
     * if the current asset price is lower than the average
     * it buys the asset and if the price is higher it sells the asset.
     */
    def MeanReversion(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                      /** order factory function*/ orderFactory = order._.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15)
         = Generic(orderFactory(observable.sidefunc.MeanReversion(ewma_alpha)),eventGen)
    
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                              /** order factory function*/ orderFactory = order._.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell(),
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = mathutils.rnd.lognormvariate(0.0,0.1))
         = Generic(orderFactory(side,observable.pricefunc.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    /** Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** order factory function*/ orderFactory = order.Limit(),
                /** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent) : ISingleAssetStrategy
        
    
    /** Noise strategy is a quite dummy strategy that randomly creates an order and sends it to the order book.
     */
    def Noise(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
              /** order factory function*/ orderFactory = order._.side.Market())
         = Generic(orderFactory(observable.sidefunc.Noise()),eventGen)
    
    def Bollinger_linear(orderFactory = order._.signedVolume.MarketSigned(),
                         alpha = 0.15,
                         k = const(0.5))
         = Generic(orderFactory(observable.volumefunc.Bollinger_linear(alpha,k)))
}
@category = "Basic"

package observable {@category = "Price function"
    
    package pricefunc {
        def LiquidityProvider(side = side.Sell(),
                              initialValue = 100.0,
                              priceDistr = mathutils.rnd.lognormvariate(0.0,0.1),
                              book = orderbook.OfTrader())
             = orderbook.SafeSidePrice(orderbook.Queue(book,side),constant(initialValue))*priceDistr
    }
    @category = "Side function"
    
    package sidefunc {
        def PairTrading(dependee = orderbook.OfTrader(),
                        factor = 1.0,
                        book = orderbook.OfTrader())
             = ObservableSide(FundamentalValue(orderbook.MidPrice(dependee)*factor,book))
        
        @python.observable()
        def Signal(signal = constant(),
                   threshold = 0.7)
             = if signal>threshold then side.Buy() else if signal<0-threshold then side.Sell() else side.Nothing()
        
        def CrossingAverages(alpha_1 = 0.015,
                             alpha_2 = 0.15,
                             threshold = 0.0,
                             book = orderbook.OfTrader())
             = Signal(EW.Avg(orderbook.MidPrice(book),alpha_1)-EW.Avg(orderbook.MidPrice(book),alpha_2),threshold)
        
        def TrendFollower(alpha = 0.015,
                          threshold = 0.0,
                          book = orderbook.OfTrader())
             = Signal(Derivative(EW.Avg(orderbook.MidPrice(book),alpha)),threshold)
        
        @python.observable()
        def FundamentalValue(fv = constant(200.0),
                             book = orderbook.OfTrader())
             = if orderbook.BidPrice(book)>fv then side.Sell() else if orderbook.AskPrice(book)<fv then side.Buy() else side.Nothing()
        
        def MeanReversion(alpha = 0.015,
                          book = orderbook.OfTrader())
             = FundamentalValue(EW.Avg(orderbook.MidPrice(book),alpha),book)
        
        def Noise(side_distribution = mathutils.rnd.uniform(0.0,1.0) : IFunction[Float])
             = if side_distribution>0.5 then side.Sell() else side.Buy()
    }
    
    package Cumulative {
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        def MinEpsilon(source = constant(),
                       epsilon = constant(0.01)) : IObservable[Float]
            
        
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        def MaxEpsilon(source = constant(),
                       epsilon = constant(0.01)) : IObservable[Float]
            
    }
    @category = "RSI"
    
    package rsi {
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(source = const(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
    @category = "MACD"
    
    package macd {
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
        def MACD(x = const(),
                 slow = 26.0,
                 fast = 12.0)
             = EW.Avg(x,2.0/(fast+1))-EW.Avg(x,2.0/(slow+1))
        
        @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Signal(x = const(),
                   slow = 26.0,
                   fast = 12.0,
                   timeframe = 9.0,
                   step = 1.0)
             = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2/(timeframe+1))
        
        @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
        def Histogram(x = const(),
                      slow = 26.0,
                      fast = 12.0,
                      timeframe = 9.0,
                      step = 1.0)
             = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
    }
    @category = "Trader's"
    
    package trader {
        @python.intrinsic("trader.props.Balance_Impl")
        def Balance(trader = SingleProxy()) : IObservable[Price]
            
        
        def RoughPnL(trader = SingleProxy())
             = Observable(Balance(trader)+orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader),Position(trader)))
        
        @python.intrinsic("trader.props.Position_Impl")
        def Position(trader = SingleProxy()) : IObservable[Volume]
            
        
        def Efficiency(trader = SingleProxy())
             = Observable(Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader)))
        
        @python.intrinsic("trader.proxy._Single_Impl")
        @label = "N/A"
        def SingleProxy() : ISingleAssetTrader
            
        
        def EfficiencyTrend(trader = SingleProxy(),
                            alpha = 0.15)
             = Derivative(EW.Avg(Efficiency(trader),alpha))
        
        @python.intrinsic("trader.props.PendingVolume_Impl")
        def PendingVolume(trader = SingleProxy()) : IObservable[Volume]
            
    }
    @category = "Volume function"
    
    package volumefunc {
        def DesiredPosition(desiredPosition = const(),
                            trader = trader.SingleProxy())
             = ObservableVolume(desiredPosition-trader.Position(trader)-trader.PendingVolume(trader))
        
        def Bollinger_linear(alpha = 0.15,
                             k = const(0.5),
                             trader = trader.SingleProxy())
             = DesiredPosition(OnEveryDt(1.0,EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)),alpha))*k,trader)
        
        def RSI_linear(alpha = 1.0/14.0,
                       k = const(-0.04),
                       timeframe = 1.0,
                       trader = trader.SingleProxy())
             = DesiredPosition(OnEveryDt(1.0,50.0-RSI(orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
    }
    @category = "Asset's"
    
    package orderbook {
        @python.observable()
        def SafeSidePrice(queue = Asks(),
                          defaultValue = constant(100.0))
             = ObservablePrice(IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue)))
        
        @label = "Price_{%(alpha)s}^{%(queue)s}"
        def WeightedPrice(queue = Asks(),
                          alpha = 0.015)
             = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
        
        @python.intrinsic("orderbook.props._TickSize_Impl")
        def TickSize(book = OfTrader()) : () => Price
            
        
        @label = "LastAsk_{%(book)s}"
        def AskLastPrice(book = OfTrader())
             = LastPrice(Asks(book))
        
        def BidLastTradePrice(book = OfTrader())
             = LastTradePrice(Bids(book))
        
        @label = "Ask_{%(alpha)s}^{%(book)s}"
        def AskWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Asks(book),alpha)
        
        def MidPrice(book = OfTrader())
             = ObservablePrice((AskPrice(book)+BidPrice(book))/2.0)
        
        @python.intrinsic("orderbook.queue._Asks_Impl")
        def Asks(book = OfTrader())
             = Queue(book,side.Sell())
        
        @label = "Bid_{%(alpha)s}^{%(book)s}"
        def BidWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Bids(book),alpha)
        
        @label = "Ask_{%(book)s}"
        def AskPrice(book = OfTrader())
             = BestPrice(Asks(book))
        
        @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue = Asks()) : IObservable[Volume]
            
        
        @label = "Bid^{%(book)s}"
        def BidPrice(book = OfTrader())
             = BestPrice(Bids(book))
        
        @python.intrinsic("orderbook.queue._Bids_Impl")
        def Bids(book = OfTrader())
             = Queue(book,side.Buy())
        
        @python.intrinsic("orderbook.props._BestPrice_Impl")
        def BestPrice(queue = Asks()) : IObservable[Price]
            
        
        @python.intrinsic("orderbook.queue._Queue_Impl")
        def Queue(book = OfTrader(),
                  side = side.Sell()) : IOrderQueue
            
        
        @python.intrinsic("orderbook.of_trader._OfTrader_Impl")
        @label = "N/A"
        def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
            
        
        def AskLastTradePrice(book = OfTrader())
             = LastTradePrice(Asks(book))
        
        @label = "LastBid^{%(book)s}"
        def BidLastPrice(book = OfTrader())
             = LastPrice(Bids(book))
        
        @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
        def CumulativePrice(book = OfTrader(),
                            depth = constant()) : IObservable[Price]
            
        
        @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
        @label = "VolumeLevels(%(queue)s)"
        def VolumeLevels(queue = Asks(),
                         volumeDelta = 30.0,
                         volumeCount = 10) : IFunction[VolumeLevels]
            
        
        @python.intrinsic("orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue = Asks()) : IObservable[Price]
            
        
        def NaiveCumulativePrice(book = OfTrader(),
                                 depth = constant())
             = ObservablePrice(if depth<0.0 then depth*AskPrice(book) else if depth>0.0 then depth*BidPrice(book) else 0.0)
        
        def Spread(book = OfTrader())
             = ObservablePrice(AskPrice(book)-BidPrice(book))
        
        @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue = Asks()) : IObservable[Price]
            
    }
    
    package Moving {
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        def Min(source = constant(),
                timeframe = 100.0) : IObservable[Float]
            
        
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        def Max(source = constant(),
                timeframe = 100.0) : IObservable[Float]
            
    }
    @category = "Statistics"
    
    package  {
        package EW {
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg_{\\alpha=%(alpha)s}(%(source)s)"
            def Avg(source = const(),
                    alpha = 0.015) : IDifferentiable
                
            
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}"
            def Var(source = const(),
                    alpha = 0.015) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}"
            def StdDev(source = const(),
                       alpha = 0.015)
                 = mathops.Sqrt(Var(source,alpha))
            
            @label = "RSD_{\\alpha=%(alpha)s}_{%(source)s}"
            def RelStdDev(source = const(),
                          alpha = 0.15)
                 = (source-Avg(source,alpha))/StdDev(source,alpha)
        }
        
        package Cumulative {
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg_{cumul}(%(source)s)"
            def Avg(source = const()) : () => Float
                
            
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2_{cumul}(%(source)s)"
            def Var(source = const()) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}"
            def StdDev(source = const())
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD_{cumul}_{%(source)s}"
            def RelStdDev(source = const())
                 = (source-Avg(source))/StdDev(source)
        }
        
        package Moving {
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg_{n=%(timeframe)s}(%(source)s)"
            def Avg(source = const(),
                    timeframe = 100.0) : () => Float
                
            
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2_{n=%(timeframe)s}(%(source)s)"
            def Var(source = const(),
                    timeframe = 100.0)
                 = Max(const(0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
            
            @label = "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}"
            def StdDev(source = const(),
                       timeframe = 100.0)
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD_{n=%(timeframe)s}_{%(source)s}"
            def RelStdDev(source = const(),
                          timeframe = 100.0)
                 = (source-Avg(source,timeframe))/StdDev(source,timeframe)
        }
    }
    
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    def OnEveryDt(dt = 1.0,
                  x = constant()) : IObservable[Float]
        
    
    @python.observable()
    @label = "min{%(x)s, %(y)s}"
    def Min(x = constant(),
            y = constant())
         = if x<y then x else y
    
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(source = const(),
                      timeframe = 10.0)
         = Observable(Max(const(0.0),Lagged(source,timeframe)-source))
    
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable[Float]
        
    
    @python.observable()
    @label = "max{%(x)s, %(y)s}"
    def Max(x = constant(),
            y = constant())
         = if x>y then x else y
    
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(source = const(),
                    timeframe = 10.0)
         = Observable(Max(const(0.0),source-Lagged(source,timeframe)))
    
    @python.observable()
    @category = "Pow/Log"
    @label = "{%(x)s}^2"
    def Sqr(x = constant())
         = x*x
    
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(book = orderbook.OfTrader(),
            timeframe = 10.0,
            alpha = 0.015)
         = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha))
    
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def ObservableVolume(x = const() : IFunction[Float]) : IObservable[Volume]
        
    
    @python.intrinsic("observable.on_every_dt._ObservableSide_Impl")
    @label = "[%(x)s]"
    def ObservableSide(x = side.Sell() : IFunction[Side]) : IObservable[Side]
        
    
    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(ticker = "^GSPC",
              start = "2001-1-1",
              end = "2010-1-1") : IObservable[Price]
        
    
    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    def CandleSticks(source = const(),
                     timeframe = 10.0) : IObservable[CandleStick]
        
    
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def ObservablePrice(x = const() : IFunction[Float]) : IObservable[Price]
        
    
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Observable(x = const() : IFunction[Float]) : IObservable[Float]
        
}
@python = "no"

package trash {
    package types {
        package  {
            package  {
                type U : T, R
            }
        }
        
        package  {
            type R : T
        }
        
        package  {
            type T
        }
        
        type T1 = T
    }
    
    package in1 {
        package in2 {
            def S1(y = "abc")
                 = y
            
            def F(x = IntFunc() : IFunction[Float])
                 = x
            
            def A(x = constant(),
                  y = if 3>x+2 then x else x*2) : () => types.T
                
            
            def IntObs() : IObservable[Int]
                
            
            def IntFunc() : IFunction[Int]
                
            
            def C(x : IFunction[CandleStick])
                 = x
            
            def S2() : Optional[String]
                 = S1()
            
            def O(x = IntObs() : IObservable[Float])
                 = x
        }
        
        def A(x : () => .trash.types.T1 = .trash.A()) : () => types.U
            
    }
    
    def A(x = in1.in2.A()) : () => types.R
        
}
@category = "Basic"

package  {
    def EWMA = observable.EW.Avg
    
    @label = "C=%(x)s"
    def constant(x = 1.0) : IFunction[Float]
         = const(x)
    
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => Float
        
    
    @python.intrinsic.function("_constant._Constant_Impl")
    @label = "C=%(x)s"
    def const(x = 1.0) : IObservable[Float]
        
    
    @python.intrinsic("observable.derivative._Derivative_Impl")
    @label = "\\frac{d%(x)s}{dt}"
    def Derivative(x = EWMA() : IDifferentiable) : () => Float
        
    
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(),
                  elsePart = constant())
         = if x<>null() then x else elsePart
}

type CandleStick

type Volume : Int

type Optional[T]

type Side

type Boolean

type Price : Float

type IOrderQueue

type Float

type Int : Float

type IOrderBook

type IEvent

type IObservable[U] : IFunction[U], IEvent

type IFunction[T] = () => T

type ISingleAssetStrategy

type ISingleAssetTrader

type Order

type IDifferentiable : IFunction[Float]

type VolumeLevels

type IOrderGenerator = IObservable[Order]

type String
