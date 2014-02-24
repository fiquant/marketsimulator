package math
{
    @category = "Statistics"
    package
    {
        @suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        @kind = "EW"
        package EW
        {
            /**
             *  Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg (/** observable data source */ source = const (1.),
                     /** alpha parameter */        alpha = 0.015) : IDifferentiable

            /**
             *  Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var (       /** observable data source */ source = const (1.),
                            /** alpha parameter */        alpha = 0.015) => Float
            /**
             *  Exponentially weighted moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev (    /** observable data source */ source = const (1.),
                            /** alpha parameter */        alpha = 0.015) = source~>EW_Var(alpha)~>Sqrt

            /**
             *  Exponentially weighted moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev   (/** observable data source */ source = const (1.),
                             /** alpha parameter */        alpha = 0.015)
                = (source - source~>EW_Avg(alpha)) / source~>EW_StdDev(alpha)
        }

        @suffix = "_{cumul}(%(source)s)"
        @kind = "Cumulative"
        package Cumulative
        {
            /**
             *  Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg (/** observable data source */ source = const (1.)) : IDifferentiable

            /**
             *  Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var (/** observable data source */ source = const (1.)) => Float

            /**
             *  Cumulative standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev (/** observable data source */ source = const (1.))
                = Sqrt(Var(source))

            /**
             *  Cumulative relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(/** observable data source */ source = const (1.))
                = (source - Avg(source)) / StdDev(source)
        }

        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        @kind = "Moving"
        package Moving
        {
            /**
             *  Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg (/** observable data source */ source = const (1.),
                     /** sliding window size    */ timeframe = 100.0) : IDifferentiable

            /**
             *  Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var (/** observable data source */ source = const (1.),
                     /** sliding window size    */ timeframe = 100.0)
                = math.Max(const(0), Avg(source*source, timeframe) - Sqr(Avg(source, timeframe)))

            /**
             *  Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev (/** observable data source */ source = const (1.),
                        /** sliding window size    */ timeframe = 100.0) = Sqrt(Var(source))

            /**
             *  Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(  /** observable data source */ source = const (1.),
                            /** sliding window size    */ timeframe = 100.0)
                = (source - Avg(source, timeframe)) / StdDev(source, timeframe)
        }

    }
}