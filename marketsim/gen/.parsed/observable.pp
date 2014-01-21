@category = "Basic"

package observable() {
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Float(x = const() : IFunction[Float]) : IObservable[Float]
        
    
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Price(x = const() : IFunction[Float]) : IObservable[Price]
        
    
    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Volume(x = const() : IFunction[Float]) : IObservable[Volume]
        
    
    @python.intrinsic("observable.on_every_dt._ObservableSide_Impl")
    @label = "[%(x)s]"
    def Side(x = side.Sell() : IFunction[Side]) : IObservable[Side]
        
    
    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    def OnEveryDt(dt = 1.0,
                  x = constant()) : IObservable[Float]
        
    
    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(ticker = "^GSPC",
              start = "2001-1-1",
              end = "2010-1-1") : IObservable[Price]
        
    
    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source = constant(1.0)) : IObservable[Float]
        
}
