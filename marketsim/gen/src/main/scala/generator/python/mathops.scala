package generator.python
import predef._

object mathops extends gen.PythonGenerator
{

    case class Import(args : List[String], f : Typed.Function)
            extends base.Intrinsic
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.BaseClass_Observable
    {
        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_function)" + "\r\n" + "In function " + f)

        override val impl_function = args(0)
        def mkParam(p : Typed.Parameter) = Parameter(p)

        case class Parameter(p : Typed.Parameter) extends base.SubscribeParameter
        {
            def nullable =
                s"$name = self.$name()" |
                s"if $name is None: return None"

            override def call = name
        }

        val impl_module = "math"

        def nullable_fields = join_fields({ _.nullable}, crlf)

        override def call_body = nullable_fields | super.call_body

        override def body = super.body | call
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.mathops"
}
