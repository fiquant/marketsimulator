package generator.python
import predef._

object mathops extends gen.PythonGenerator
{
    case class Parameter(p : Typed.Parameter) extends base.Parameter
    {
        override def assign =
            super.assign |
            s"if isinstance($name, types.IEvent):" |>
                s"event.subscribe(self.$name, self.fire, self)" |||
            ImportFrom("event", "marketsim") |||
            ImportFrom("types", "marketsim")


        def nullable =
            s"$name = self.$name()" |
            s"if $name is None: return None"

        override def call = name

    }

    case class Import(args : List[String], f : Typed.Function) extends base.Intrinsic
    {
        val name = f.name

        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_function)" + "\r\n" + "In function " + f)

        override val impl_function = args(0)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring.get.detailed

        type Parameter = mathops.Parameter
        val impl_module = "math"
        val alias = name

        override val base_class = "Observable[float]" ||| ImportFrom("Observable", "marketsim.ops._all")

        override def init_body = base_class ||| ".__init__(self)" | super.init_body

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
