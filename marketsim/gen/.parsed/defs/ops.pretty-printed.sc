@category = "Ops"

package ops {@label = "-%(x)s"
    
    package  {
        // defined at defs\ops.sc: 6.9
        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 9.9
        @python.intrinsic.observable("ops._Negate_Impl")
        def Negate(x = const(1.0)) : IObservable[Float]
    }
    @label = "\\frac{%(x)s}{%(y)s}"
    
    package  {
        // defined at defs\ops.sc: 15.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.0),
                y = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 18.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.0),
                y = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 21.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = constant(1.0),
                y = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 24.9
        @python.intrinsic.observable("ops._Div_Impl")
        def Div(x = const(1.0),
                y = constant(1.0)) : IObservable[Float]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {@symbol = "*"
        
        package  {
            // defined at defs\ops.sc: 33.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 36.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 39.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 42.13
            @python.intrinsic.observable("ops._Mul_Impl")
            def Mul(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
        @symbol = "+"
        
        package  {
            // defined at defs\ops.sc: 48.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 51.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 54.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 57.13
            @python.intrinsic.observable("ops._Add_Impl")
            def Add(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
        @symbol = "-"
        
        package  {
            // defined at defs\ops.sc: 63.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.0),
                    y = constant(1.0)) : IFunction[Float]
            
            // defined at defs\ops.sc: 66.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 69.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = constant(1.0),
                    y = const(1.0)) : IObservable[Float]
            
            // defined at defs\ops.sc: 72.13
            @python.intrinsic.observable("ops._Sub_Impl")
            def Sub(x = const(1.0),
                    y = constant(1.0)) : IObservable[Float]
        }
    }
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    package  {
        // defined at defs\ops.sc: 79.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = constant(1.0),
                      elsepart = constant(1.0)) : IFunction[Float]
        
        // defined at defs\ops.sc: 84.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = const(1.0),
                      elsepart = constant(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 89.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = constant(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 94.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = const(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 99.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]
        
        // defined at defs\ops.sc: 104.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.observableSell(),
                      elsepart = side.Buy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 109.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.Sell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 114.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true() : IFunction[Boolean],
                      ifpart = side.observableSell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 119.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = constant(1.0),
                      elsepart = constant(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 124.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = const(1.0),
                      elsepart = constant(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 129.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = constant(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 134.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = const(1.0),
                      elsepart = const(1.0)) : IObservable[Float]
        
        // defined at defs\ops.sc: 139.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.Sell(),
                      elsepart = side.Buy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 144.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.observableSell(),
                      elsepart = side.Buy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 149.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.Sell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
        
        // defined at defs\ops.sc: 154.9
        @python.intrinsic.observable("ops._Condition_Impl")
        def Condition(cond = true(),
                      ifpart = side.observableSell(),
                      elsepart = side.observableBuy()) : IObservable[Side]
    }
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    
    package  {@symbol = "=="
        
        package  {
            // defined at defs\ops.sc: 166.13
            @python.intrinsic.observable("ops._Equal_Impl")
            def Equal(x = constant(1.0),
                      y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 169.13
            @python.intrinsic.observable("ops._Equal_Impl")
            def Equal(x = const(1.0),
                      y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 172.13
            @python.intrinsic.observable("ops._Equal_Impl")
            def Equal(x = constant(1.0),
                      y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 175.13
            @python.intrinsic.observable("ops._Equal_Impl")
            def Equal(x = const(1.0),
                      y = const(1.0)) : IObservable[Boolean]
        }
        @symbol = "<>"
        
        package  {
            // defined at defs\ops.sc: 181.13
            @python.intrinsic.observable("ops._NotEqual_Impl")
            def NotEqual(x = constant(1.0),
                         y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 184.13
            @python.intrinsic.observable("ops._NotEqual_Impl")
            def NotEqual(x = const(1.0),
                         y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 187.13
            @python.intrinsic.observable("ops._NotEqual_Impl")
            def NotEqual(x = constant(1.0),
                         y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 190.13
            @python.intrinsic.observable("ops._NotEqual_Impl")
            def NotEqual(x = const(1.0),
                         y = const(1.0)) : IObservable[Boolean]
        }
        @symbol = "<"
        
        package  {
            // defined at defs\ops.sc: 196.13
            @python.intrinsic.observable("ops._Less_Impl")
            def Less(x = constant(1.0),
                     y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 199.13
            @python.intrinsic.observable("ops._Less_Impl")
            def Less(x = const(1.0),
                     y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 202.13
            @python.intrinsic.observable("ops._Less_Impl")
            def Less(x = constant(1.0),
                     y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 205.13
            @python.intrinsic.observable("ops._Less_Impl")
            def Less(x = const(1.0),
                     y = const(1.0)) : IObservable[Boolean]
        }
        @symbol = ">"
        
        package  {
            // defined at defs\ops.sc: 211.13
            @python.intrinsic.observable("ops._Greater_Impl")
            def Greater(x = constant(1.0),
                        y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 214.13
            @python.intrinsic.observable("ops._Greater_Impl")
            def Greater(x = const(1.0),
                        y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 217.13
            @python.intrinsic.observable("ops._Greater_Impl")
            def Greater(x = constant(1.0),
                        y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 220.13
            @python.intrinsic.observable("ops._Greater_Impl")
            def Greater(x = const(1.0),
                        y = const(1.0)) : IObservable[Boolean]
        }
        @symbol = "<="
        
        package  {
            // defined at defs\ops.sc: 226.13
            @python.intrinsic.observable("ops._LessEqual_Impl")
            def LessEqual(x = constant(1.0),
                          y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 229.13
            @python.intrinsic.observable("ops._LessEqual_Impl")
            def LessEqual(x = const(1.0),
                          y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 232.13
            @python.intrinsic.observable("ops._LessEqual_Impl")
            def LessEqual(x = constant(1.0),
                          y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 235.13
            @python.intrinsic.observable("ops._LessEqual_Impl")
            def LessEqual(x = const(1.0),
                          y = const(1.0)) : IObservable[Boolean]
        }
        @symbol = ">="
        
        package  {
            // defined at defs\ops.sc: 241.13
            @python.intrinsic.observable("ops._GreaterEqual_Impl")
            def GreaterEqual(x = constant(1.0),
                             y = constant(1.0)) : IFunction[Boolean]
            
            // defined at defs\ops.sc: 244.13
            @python.intrinsic.observable("ops._GreaterEqual_Impl")
            def GreaterEqual(x = const(1.0),
                             y = constant(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 247.13
            @python.intrinsic.observable("ops._GreaterEqual_Impl")
            def GreaterEqual(x = constant(1.0),
                             y = const(1.0)) : IObservable[Boolean]
            
            // defined at defs\ops.sc: 250.13
            @python.intrinsic.observable("ops._GreaterEqual_Impl")
            def GreaterEqual(x = const(1.0),
                             y = const(1.0)) : IObservable[Boolean]
        }
    }
}
