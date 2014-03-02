package math
{
    @category = "Statistics"
    package {

        abstract type IStatDomain(source = .const(0.))
        {
            /**
             *  Standard deviation
             */
            def StdDev = Var~>Sqrt

            /**
             *  Relative standard deviation
             */
            def RelStdDev = (source - Avg) / StdDev
        }

        type Cumulative() : IStatDomain
        {
            /**
             *  Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            def Avg : IDifferentiable

            /**
             *  Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            def Var => Float
        }

        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            /**
             *  Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            def Avg : IDifferentiable

            /**
             *  Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            def Var => Float
        }

        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.) : IStatDomain
        {
            /**
             *  Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            def Avg : IDifferentiable

            /**
             *  Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            def Var => Float
        }
    }
}