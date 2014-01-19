package observable
{
    @category = "Statistics"
    package
    {
        @suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        package EW(source = const (), alpha = 0.015)
        {
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg () : IDifferentiable

            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var () => Float

            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev () = mathops.Sqrt(Var(source, alpha))

            @label = "RSD{{suffix}}"
            def RelStdDev()
                = (source - Avg(source, alpha)) / StdDev(source, alpha)
        }

        @suffix = "_{cumul}(%(source)s)"
        package Cumulative
        {
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (source = const ()) => Float

            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var (source = const ()) => Float

            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (source = const ()) = mathops.Sqrt(Var(source))

            @label = "RSD{{suffix}}"
            def RelStdDev(source = const ())
                = (source - Avg(source)) / StdDev(source)
        }

        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        package Moving
        {
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            def Avg (source = const (), timeframe = 100.0) => Float

            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var (source = const (), timeframe = 100.0)
                = observable.Max(const(0), Avg(source*source, timeframe) - Sqr(Avg(source, timeframe)))

            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev (source = const (), timeframe = 100.0) = mathops.Sqrt(Var(source))

            @label = "RSD{{suffix}}"
            def RelStdDev(source = const (), timeframe = 100.0)
                = (source - Avg(source, timeframe)) / StdDev(source, timeframe)
        }

    }
}