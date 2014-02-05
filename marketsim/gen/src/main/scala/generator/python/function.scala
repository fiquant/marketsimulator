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
        val parameters  = f.parameters map Parameter

        type Parameter = function.Parameter

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
            ImportFrom("context", "marketsim")

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def init_body =
            super.init_body |
            "self.impl = self.getImpl()"

        override def call_body = "return self.impl()"

        override def body = super.body | internals | getImpl | bind | reset | call
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.function"
}
