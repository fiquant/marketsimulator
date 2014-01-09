package generator.python

object intrinsic extends gen.PythonGenerator
{
    val name = "python.intrinsic"

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        (if (TypesBound.isObservable(f.ret_type))
            intrinsic_observable
        else
            intrinsic_function).generatePython(args)(f)
    }
}
