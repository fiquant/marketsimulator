@category = "Basic"
package observable
{
    /**
     *  Discretizes function *x* at even time steps *dt*
     */
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    def OnEveryDt( /** time discretization step */
                   dt = 1.0,
                   /** function to discretize */
                   x = constant(1.)) : IObservable[Float]

    /**
     *  Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker*
     *  and follows the price in scale 1 model unit of time = 1 real day
     */
    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(/** defines quotes to download */
              ticker = "^GSPC",
              /** defines first day to download in form YYYY-MM-DD */
              start = "2001-1-1",
              /** defines last day to download in form YYYY-MM-DD */
              end = "2010-1-1") : IObservable[Price]

    /**
     *  Observable listening to *source*
     *  When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
     */
    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source = constant(1.)) : IObservable[Float]

    /**
     * Down casts function *x* to IObservable[Float].
     * Needed since generic functions aren't implemented yet
     */
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Float(x = const(1.) : IFunction[Float]) : IObservable[Float]

    /**
     * Down casts function *x* to IObservable[Price].
     * Needed since generic functions aren't implemented yet
     */
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Price(x = const(1.) : IFunction[Float]) : IObservable[Price]

    /**
     * Down casts function *x* to IObservable[Volume].
     * Needed since generic functions aren't implemented yet
     */
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Volume(x = const(1.) : IFunction[Float]) : IObservable[Volume]

    /**
     * Down casts function *x* to IObservable[Side].
     * Needed since generic functions aren't implemented yet
     */
    @python.intrinsic("observable.on_every_dt._ObservableSide_Impl")
    @label = "[%(x)s]"
    def Side(x = side.Sell() : IFunction[Side]) : IObservable[Side]
}