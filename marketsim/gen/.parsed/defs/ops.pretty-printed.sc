@category = "Ops"

package ops {
    // defined at defs\ops.sc: 4.5
    @label = "-%(x)s"
    @python.intrinsic.observable("ops._Negate_Impl")
    def Negate(x = constant(1.0)) : IFunction[Float]
    
    // defined at defs\ops.sc: 8.5
    @label = "\\frac{%(x)s}{%(y)s}"
    @python.intrinsic.observable("ops._Div_Impl")
    def Div(x = constant(1.0),
            y = constant(1.0)) : IFunction[Float]
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {
        // defined at defs\ops.sc: 15.9
        @symbol = "*"
        @python.intrinsic.observable("ops._Mul_Impl")
        def Mul(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 19.9
        @symbol = "+"
        @python.intrinsic.observable("ops._Add_Impl")
        def Add(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 23.9
        @symbol = "-"
        @python.intrinsic.observable("ops._Sub_Impl")
        def Sub(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
    }
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    package  {
        // defined at defs\ops.sc: 30.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = constant(1.0),
                      elsepart = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 35.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {
        // defined at defs\ops.sc: 46.9
        @symbol = "=="
        @python.intrinsic.observable("ops._Equal_Impl")
        def Equal(x = constant(1.0),
                  y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 50.9
        @symbol = "<>"
        @python.intrinsic.observable("ops._NotEqual_Impl")
        def NotEqual(x = constant(1.0),
                     y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 54.9
        @symbol = "<"
        @python.intrinsic.observable("ops._Less_Impl")
        def Less(x = constant(1.0),
                 y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 58.9
        @symbol = ">"
        @python.intrinsic.observable("ops._Greater_Impl")
        def Greater(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 62.9
        @symbol = "<="
        @python.intrinsic.observable("ops._LessEqual_Impl")
        def LessEqual(x = constant(1.0),
                      y = constant(1.0)) : IFunction[Boolean]
        
        // defined at defs\ops.sc: 66.9
        @symbol = ">="
        @python.intrinsic.observable("ops._GreaterEqual_Impl")
        def GreaterEqual(x = constant(1.0),
                         y = constant(1.0)) : IFunction[Boolean]
    }
}
