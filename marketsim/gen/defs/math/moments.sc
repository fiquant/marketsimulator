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

                = (source~>Sqr~>Moving_Avg(timeframe) - source~>Moving_Avg(timeframe)~>Sqr)~>Max(0)

            /**
             *  Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev (/** observable data source */ source = const (1.),
                        /** sliding window size    */ timeframe = 100.0)

                = source~>Moving_Var(timeframe)~>Sqrt

            /**
             *  Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(  /** observable data source */ source = const (1.),
                            /** sliding window size    */ timeframe = 100.0)

                = (source - source~>Moving_Avg(timeframe)) / source~>Moving_StdDev(timeframe)
        }

        package impl
        {
//            @python.intrinsic("moments.tmp.Source_Impl")
//            def Source(x = .EW() : IStatDomain) : IObservable[Float]
//
//            @python.intrinsic.function("moments.tmp.Alpha_Impl")
//            def Alpha(x = .EW()) : Float
//
//            @python.intrinsic.function("moments.tmp.Timeframe_Impl")
//            def Timeframe(x = .Moving()) : Float
//
            def Avg(x = .EW())           = math.EW.Avg(x~>Source, x~>Alpha)
            def Avg(x = .Cumulative())   = math.Cumulative.Avg(x~>Source)
            def Avg(x = .Moving())       = math.Moving.Avg(x~>Source, x~>Timeframe)

            def Var(x = .EW())           = math.EW.Var(x~>Source, x~>Alpha)
            def Var(x = .Cumulative())   = math.Cumulative.Var(x~>Source)
            def Var(x = .Moving())       = math.Moving.Var(x~>Source, x~>Timeframe)

            def StdDev(x = .EW())           = math.EW.StdDev(x~>Source, x~>Alpha)
            def StdDev(x = .Cumulative())   = math.Cumulative.StdDev(x~>Source)
            def StdDev(x = .Moving())       = math.Moving.StdDev(x~>Source, x~>Timeframe)

            def RelStdDev(x = .EW())           = math.EW.RelStdDev(x~>Source, x~>Alpha)
            def RelStdDev(x = .Cumulative())   = math.Cumulative.RelStdDev(x~>Source)
            def RelStdDev(x = .Moving())       = math.Moving.RelStdDev(x~>Source, x~>Timeframe)
        }

    }
}