package generator.python

object intrinsic extends gen.PythonGenerator
{
    val name = "python.intrinsic"

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        if (f.ret_type canCastTo Types.floatObservable)
            intrinsic_observable(args)(f)
        else
            intrinsic_function(args)(f)
    }
}
