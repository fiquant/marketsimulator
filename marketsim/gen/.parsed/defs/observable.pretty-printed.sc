@category = "Basic"

package observable {
    // defined at defs\observable.sc: 4.5
    /** Discretizes function *x* at even time steps *dt*
     */
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    def OnEveryDt(/** time discretization step */ dt = 1.0,
                  /** function to discretize */ x = constant(1.0)) : IObservable[Float]
    
    // defined at defs\observable.sc: 15.5
    /** Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker*
     *  and follows the price in scale 1 model unit of time = 1 real day
     */
    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(/** defines quotes to download */ ticker = "^GSPC",
              /** defines first day to download in form YYYY-MM-DD */ start = "2001-1-1",
              /** defines last day to download in form YYYY-MM-DD */ end = "2010-1-1") : IObservable[Price]
    
    // defined at defs\observable.sc: 28.5
    /** Observable listening to *source*
     *  When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
     */
    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source = constant(1.0)) : IObservable[Float]
}
