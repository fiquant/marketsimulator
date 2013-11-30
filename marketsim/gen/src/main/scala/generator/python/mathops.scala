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

        override def call = s"self.$name()"

    }

    case class Import(args : List[String], f : Typed.Function) extends base.Intrinsic
    {
        if (args.length != 3)
            throw new Exception(s"Annotation python.mathops should have 3 arguments in" +
                    " form (category, implementation_function, label_template)" + "\r\n" + "In function " + f)

        val category = args(0)
        override val impl_function = args(1)
        val label_tmpl = args(2)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring.get.detailed

        type Parameter = mathops.Parameter
        val impl_module = "math"
        val name = f.name
        val alias = name

        override def repr_body = s"""return "$label_tmpl" % self.__dict__""" |||
                ImportFrom("IObservable", "marketsim") |||
                ImportFrom("IFunction", "marketsim") |||
                ImportFrom("Observable", "marketsim.ops._all") |||
                ImportFrom("constant", "marketsim.ops._all")

        override val base_class = "Observable[float]"

        override def init_body = "Observable[float].__init__(self)" | super.init_body

        def nullable_fields = join_fields({ _.nullable}, crlf)

        override def call_body = nullable_fields | super.call_body

        override def body = super.body | call
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.mathops"
}
