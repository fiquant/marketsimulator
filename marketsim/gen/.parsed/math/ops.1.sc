
package math() {
    @python.intrinsic.observable("ops._DivImpl")
    @label = "\\frac{%(x)s}{%(y)s}"
    def Div(x = constant(1.0),
            y = constant(1.0)) : IObservable[Float]
        
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package () {
        @python.intrinsic.observable("ops._MulImpl")
        @symbol = "*"
        def Mul(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
        
        @python.intrinsic.observable("ops._AddImpl")
        @symbol = "+"
        def Add(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
        
        @python.intrinsic.observable("ops._SubImpl")
        @symbol = "-"
        def Sub(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
    }
}
