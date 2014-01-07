package generator.python

object intrinsic extends gen.PythonGenerator
{
    val name = "python.intrinsic"

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        if (f.ret_type canCastTo Typed.topLevel.floatObservable)
            intrinsic_observable.generatePython(args)(f)
        else
            intrinsic_function.generatePython(args)(f)
    }
}
