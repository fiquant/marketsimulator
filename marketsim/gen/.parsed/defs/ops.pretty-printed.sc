@category = "Ops"

package ops() {
    // defined at defs\ops.sc: 4.5
    @label = "-%(x)s"
    @python.intrinsic.observable("ops.Negate_Impl")
    def Negate(x = constant(1.0)) : IFunction[Float]
    
    // defined at defs\ops.sc: 8.5
    @label = "\\frac{%(x)s}{%(y)s}"
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x = constant(1.0),
            y = constant(1.0)) : IFunction[Float]
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package () {
        // defined at defs\ops.sc: 15.9
        @symbol = "*"
        @python.intrinsic.observable("ops.Mul_Impl")
        def Mul(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 19.9
        @symbol = "+"
        @python.intrinsic.observable("ops.Add_Impl")
        def Add(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 23.9
        @symbol = "-"
        @python.intrinsic.observable("ops.Sub_Impl")
        def Sub(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
    }
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    package () {
        // defined at defs\ops.sc: 30.9
        @python.intrinsic.observable("ops.Condition_Impl")
        def Condition(cond = true(),
                      ifpart = constant(1.0),
                      elsepart = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 35.9
        @python.intrinsic.observable("ops.Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]
        
        // defined at defs\ops.sc: 40.9
        @python.intrinsic.observable("ops.Condition_Impl")
        def Condition(cond = true(),
                      ifpart = true(),
                      elsepart = false()) : IFunction[Boolean]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package () {
        // defined at defs\ops.sc: 50.9
        @symbol = "=="
        @python.intrinsic.observable("ops.Equal_Impl")
        def Equal(x = constant(1.0),
                  y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 54.9
        @symbol = "<>"
        @python.intrinsic.observable("ops.NotEqual_Impl")
        def NotEqual(x = constant(1.0),
                     y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 58.9
        @symbol = "<"
        @python.intrinsic.observable("ops.Less_Impl")
        def Less(x = constant(1.0),
                 y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 62.9
        @symbol = ">"
        @python.intrinsic.observable("ops.Greater_Impl")
        def Greater(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 66.9
        @symbol = "<="
        @python.intrinsic.observable("ops.LessEqual_Impl")
        def LessEqual(x = constant(1.0),
                      y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 70.9
        @symbol = ">="
        @python.intrinsic.observable("ops.GreaterEqual_Impl")
        def GreaterEqual(x = constant(1.0),
                         y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 74.9
        @symbol = "and"
        @python.intrinsic.observable("ops.And_Impl")
        def And(x = true(),
                y = true()) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 78.9
        @symbol = "or"
        @python.intrinsic.observable("ops.Or_Impl")
        def Or(x = true(),
               y = true()) : IFunction[Boolean]
    }
}
