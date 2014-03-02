package math
{
    @category = "Statistics"
    package {

        type IStatDomain(source = .const(0.))

        type Cumulative() : IStatDomain
        {
            /**
             *  Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            def Avg () : IDifferentiable

            /**
             *  Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            def Var () => Float

            /**
             *  Cumulative standard deviation
             */
            def StdDev () = Var~>Sqrt

            /**
             *  Cumulative relative standard deviation
             */
            def RelStdDev() = (source - Avg) / StdDev
        }

        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            /**
             *  Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            def Avg() : IDifferentiable

            /**
             *  Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            def Var() => Float

            /**
             *  Exponentially weighted moving standard deviation
             */
            def StdDev() = Var~>Sqrt

            /**
             *  Exponentially weighted moving relative standard deviation
             */
            def RelStdDev() = (source - Avg) / StdDev
        }

        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.) : IStatDomain
        {
            /**
             *  Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            def Avg () : IDifferentiable

            /**
             *  Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            def Var () => Float

            /**
             *  Simple moving standard deviation
             */
            def StdDev () = Var~>Sqrt

            /**
             *  Simple moving relative standard deviation
             */
            def RelStdDev() = (source - Avg) / StdDev
        }
    }
}