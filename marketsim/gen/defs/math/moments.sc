package math
{
    @category = "Statistics"
    package
    {
        @suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        package EW
        {
            /**
             *  Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (/** observable data source */ source = const (),
                     /** alpha parameter */        alpha = 0.015) : IDifferentiable

            /**
             *  Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var (       /** observable data source */ source = const (),
                            /** alpha parameter */        alpha = 0.015) => Float
            /**
             *  Exponentially weighted moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (    /** observable data source */ source = const (),
                            /** alpha parameter */        alpha = 0.015) = Sqrt(Var(source, alpha))

            /**
             *  Exponentially weighted moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev   (/** observable data source */ source = const (),
                             /** alpha parameter */        alpha = 0.015)
                = (source - Avg(source, alpha)) / StdDev(source, alpha)
        }

        @suffix = "_{cumul}(%(source)s)"
        package Cumulative
        {
            /**
             *  Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (/** observable data source */ source = const ()) => Float

            /**
             *  Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var (/** observable data source */ source = const ()) => Float

            /**
             *  Cumulative standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (/** observable data source */ source = const ())
                = Sqrt(Var(source))

            /**
             *  Cumulative relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(/** observable data source */ source = const ())
                = (source - Avg(source)) / StdDev(source)
        }

        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        package Moving
        {
            /**
             *  Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (/** observable data source */ source = const (),
                     /** sliding window size    */ timeframe = 100.0) => Float

            /**
             *  Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var (/** observable data source */ source = const (),
                     /** sliding window size    */ timeframe = 100.0)
                = math.Max(const(0), Avg(source*source, timeframe) - Sqr(Avg(source, timeframe)))

            /**
             *  Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (/** observable data source */ source = const (),
                        /** sliding window size    */ timeframe = 100.0) = Sqrt(Var(source))

            /**
             *  Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(  /** observable data source */ source = const (),
                            /** sliding window size    */ timeframe = 100.0)
                = (source - Avg(source, timeframe)) / StdDev(source, timeframe)
        }

    }
}