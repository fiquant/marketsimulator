@category = "Ops"

package ops() {
    @python.intrinsic.observable("ops._Negate_Impl")
    @label = "-%(x)s"
    def Negate(x = constant(1.0)) : IObservable[Float]
        
    
    @python.intrinsic.observable("ops._Div_Impl")
    @label = "\\frac{%(x)s}{%(y)s}"
    def Div(x = constant(1.0),
            y = constant(1.0)) : IObservable[Float]
        
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package () {
        @python.intrinsic.observable("ops._Mul_Impl")
        @symbol = "*"
        def Mul(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
        
        @python.intrinsic.observable("ops._Add_Impl")
        @symbol = "+"
        def Add(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
        
        @python.intrinsic.observable("ops._Sub_Impl")
        @symbol = "-"
        def Sub(x = constant(1.0),
                y = constant(1.0)) : IObservable[Float]
            
    }
    
    @python.intrinsic.observable("ops._ConditionFloat_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Float(cond = true() : IFunction[Boolean],
                        ifpart = constant(1.0),
                        elsepart = constant(1.0)) : IObservable[Float]
        
    
    @python.intrinsic.observable("ops._ConditionSide_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Side(cond = true() : IFunction[Boolean],
                       ifpart = side.Sell(),
                       elsepart = side.Buy()) : IObservable[Side]
        
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package () {
        @python.intrinsic.observable("ops._Equal_Impl")
        @symbol = "=="
        def Equal(x = constant(1.0),
                  y = constant(1.0)) : IObservable[Boolean]
            
        
        @python.intrinsic.observable("ops._NotEqual_Impl")
        @symbol = "<>"
        def NotEqual(x = constant(1.0),
                     y = constant(1.0)) : IObservable[Boolean]
            
        
        @python.intrinsic.observable("ops._Less_Impl")
        @symbol = "<"
        def Less(x = constant(1.0),
                 y = constant(1.0)) : IObservable[Boolean]
            
        
        @python.intrinsic.observable("ops._LessEqual_Impl")
        @symbol = "<="
        def LessEqual(x = constant(1.0),
                      y = constant(1.0)) : IObservable[Boolean]
            
        
        @python.intrinsic.observable("ops._Greater_Impl")
        @symbol = ">"
        def Greater(x = constant(1.0),
                    y = constant(1.0)) : IObservable[Boolean]
            
        
        @python.intrinsic.observable("ops._GreaterEqual_Impl")
        @symbol = ">="
        def GreaterEqual(x = constant(1.0),
                         y = constant(1.0)) : IObservable[Boolean]
            
    }
}
