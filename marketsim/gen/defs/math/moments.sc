package math
{
    @category = "Statistics"
    package {

        type IStatDomain(source = .const(0.))

        type Cumulative() : IStatDomain

        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            /**
             *  Exponentially weighted moving relative standard deviation
             */
            def RelStdDev() = (x~>Source - x~>Avg) / x~>StdDev
        }

        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.) : IStatDomain

        /**
         *  Exponentially weighted moving average
         */
        @python.intrinsic("moments.ewma.EWMA_Impl")
        def Avg(x = EW()) : IDifferentiable

        /**
         *  Cumulative average
         */
        @python.intrinsic("moments.cma.CMA_Impl")
        def Avg (x = Cumulative()) : IDifferentiable

        /**
         *  Simple moving average
         */
        @python.intrinsic("moments.ma.MA_Impl")
        def Avg (x = Moving()) : IDifferentiable

        /**
         *  Exponentially weighted moving variance
         */
        @python.intrinsic("moments.ewmv.EWMV_Impl")
        def Var(x = EW()) => Float

        /**
         *  Cumulative variance
         */
        @python.intrinsic("moments.cmv.Variance_Impl")
        def Var (x = Cumulative()) => Float

        /**
         *  Simple moving variance
         */
        @python.intrinsic("moments.mv.MV_Impl")
        def Var (x = Moving()) => Float

        /**
         *  Exponentially weighted moving standard deviation
         */
        def StdDev(x = EW()) = x~>Var~>Sqrt

        /**
         *  Cumulative standard deviation
         */
        def StdDev (x = Cumulative()) = x~>Var~>Sqrt

        /**
         *  Simple moving standard deviation
         */
        def StdDev (x = Moving()) = x~>Var~>Sqrt

//        /**
//         *  Exponentially weighted moving relative standard deviation
//         */
//        def RelStdDev(x = EW()) = (x~>Source - x~>Avg) / x~>StdDev

        /**
         *  Cumulative relative standard deviation
         */
        def RelStdDev(x = Cumulative()) = (x~>Source - x~>Avg) / x~>StdDev

        /**
         *  Simple moving relative standard deviation
         */
        def RelStdDev(x = Moving()) = (x~>Source - x~>Avg) / x~>StdDev
    }
}