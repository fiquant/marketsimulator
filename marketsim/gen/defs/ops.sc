@category = "Ops"
package ops
{
    @label = "-%(x)s"
    @python.intrinsic.observable("ops.Negate_Impl")
    def Negate(x = constant(1.)) : IFunction[Float]

    @label = "\\frac{%(x)s}{%(y)s}"
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x = constant(1.), y = constant(1.)) : IFunction[Float]

    @label = "({%(x)s}{{symbol}}{%(y)s})"
    package {

        @symbol = "*"
        @python.intrinsic.observable("ops.Mul_Impl")
        def Mul(x = constant(1.), y = constant(1.)) : IFunction[Float]

        @symbol = "+"
        @python.intrinsic.observable("ops.Add_Impl")
        def Add(x = constant(1.), y = constant(1.)) : IFunction[Float]

        @symbol = "-"
        @python.intrinsic.observable("ops.Sub_Impl")
        def Sub(x = constant(1.), y = constant(1.)) : IFunction[Float]
    }

    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    package {
        @python.intrinsic.observable("ops.Condition_Impl")
        def Condition(cond     = true(),
                            ifpart   = constant(1.),
                            elsepart = constant(1.)) : IFunction[Float]

        @python.intrinsic.observable("ops.Condition_Impl")
        def Condition(cond     = true(),
                      ifpart   = side.Sell(),
                      elsepart = side.Buy()) : IFunction[Side]

    }


    @label = "({%(x)s}{{symbol}}{%(y)s})"
    package {

        @symbol = "=="
        @python.intrinsic.observable("ops.Equal_Impl")
        def Equal(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @symbol = "<>"
        @python.intrinsic.observable("ops.NotEqual_Impl")
        def NotEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @symbol = "<"
        @python.intrinsic.observable("ops.Less_Impl")
        def Less(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @symbol = ">"
        @python.intrinsic.observable("ops.Greater_Impl")
        def Greater(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @symbol = "<="
        @python.intrinsic.observable("ops.LessEqual_Impl")
        def LessEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]

        @symbol = ">="
        @python.intrinsic.observable("ops.GreaterEqual_Impl")
        def GreaterEqual(x = constant(1.), y = constant(1.)) : IFunction[Boolean]
    }

}