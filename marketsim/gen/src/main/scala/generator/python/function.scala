package generator.python
import predef._

object function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.BaseClass_Function
            with    base.Bind
            with    base.HasImpl
    {
        def mkParam(p : Typed.Parameter) = function.Parameter(p)
        type Parameter = function.Parameter
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.function"
}
