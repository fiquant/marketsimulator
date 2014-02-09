@category = "Ops"

package ops {
    // defined at defs\ops.sc: 4.5
    @python.intrinsic.observable("ops._Negate_Impl")
    @label = "-%(x)s"
    def Negate(x = constant(1.0)) : IObservable[Float]
    
    // defined at defs\ops.sc: 8.5
    @python.intrinsic.observable("ops._Div_Impl")
    @label = "\\frac{%(x)s}{%(y)s}"
    def Div(x = constant(1.0),
            y = constant(1.0)) : IFunction[Float]
    
    // defined at defs\ops.sc: 12.5
    @python.intrinsic.observable("ops._Div_Impl")
    @label = "\\frac{%(x)s}{%(y)s}"
    def Div(x = const(1.0),
            y = const(1.0)) : IObservable[Float]
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {
        // defined at defs\ops.sc: 19.9
        @python.intrinsic.observable("ops._Mul_Impl")
        @symbol = "*"
        def Mul(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 23.9
        @python.intrinsic.observable("ops._Add_Impl")
        @symbol = "+"
        def Add(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 27.9
        @python.intrinsic.observable("ops._Sub_Impl")
        @symbol = "-"
        def Sub(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
    }
    
    // defined at defs\ops.sc: 32.5
    @python.intrinsic.observable("ops._Condition_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Float(cond = true() : IFunction[Boolean],
                        ifpart = constant(1.0),
                        elsepart = constant(1.0)) : IFunction[Float]
    
    // defined at defs\ops.sc: 38.5
    @python.intrinsic.observable("ops._Condition_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Side(cond = true() : IFunction[Boolean],
                       ifpart = side.Sell(),
                       elsepart = side.Buy()) : IFunction[Side]
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {
        // defined at defs\ops.sc: 47.9
        @python.intrinsic.observable("ops._Equal_Impl")
        @symbol = "=="
        def Equal(x = constant(1.0),
                  y = constant(1.0)) : IObservable[Boolean]
        
        // defined at defs\ops.sc: 51.9
        @python.intrinsic.observable("ops._NotEqual_Impl")
        @symbol = "<>"
        def NotEqual(x = constant(1.0),
                     y = constant(1.0)) : IObservable[Boolean]
        
        // defined at defs\ops.sc: 55.9
        @python.intrinsic.observable("ops._Less_Impl")
        @symbol = "<"
        def Less(x = constant(1.0),
                 y = constant(1.0)) : IObservable[Boolean]
        
        // defined at defs\ops.sc: 59.9
        @python.intrinsic.observable("ops._LessEqual_Impl")
        @symbol = "<="
        def LessEqual(x = constant(1.0),
                      y = constant(1.0)) : IObservable[Boolean]
        
        // defined at defs\ops.sc: 63.9
        @python.intrinsic.observable("ops._Greater_Impl")
        @symbol = ">"
        def Greater(x = constant(1.0),
                    y = constant(1.0)) : IObservable[Boolean]
        
        // defined at defs\ops.sc: 67.9
        @python.intrinsic.observable("ops._GreaterEqual_Impl")
        @symbol = ">="
        def GreaterEqual(x = constant(1.0),
                         y = constant(1.0)) : IObservable[Boolean]
    }
}
