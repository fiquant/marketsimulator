package math
{
    @python.intrinsic.observable("ops._Div_Impl")
    @label = "\\frac{%(x)s}{%(y)s}"
    def Div(x = constant(1.), y = constant(1.)) : IObservable[Float]

    @label = "({%(x)s}{{symbol}}{%(y)s})"
    package {

        @python.intrinsic.observable("ops._Mul_Impl")
        @symbol = "*"
        def Mul(x = constant(1.), y = constant(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Add_Impl")
        @symbol = "+"
        def Add(x = constant(1.), y = constant(1.)) : IObservable[Float]

        @python.intrinsic.observable("ops._Sub_Impl")
        @symbol = "-"
        def Sub(x = constant(1.), y = constant(1.)) : IObservable[Float]
    }

    @python.intrinsic.observable("ops._ConditionFloat_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Float(cond     = true() : IFunction[Boolean],
                        ifpart   = constant(1.),
                        elsepart = constant(1.)) : IObservable[Float]

    @python.intrinsic.observable("ops._ConditionSide_Impl")
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    def Condition_Side(cond     = true() : IFunction[Boolean],
                       ifpart   = side.Sell(),
                       elsepart = side.Buy()) : IObservable[Side]
}