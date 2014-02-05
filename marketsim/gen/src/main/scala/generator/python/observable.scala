package generator.python
import predef._

object observable extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.BaseClass_Observable
            with    base.Bind
            with    base.HasImpl
    {
        val parameters  = f.parameters map Parameter

        type Parameter = observable.Parameter

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
                ImportFrom("context", "marketsim")


        override def init_body =
            base_class ||| ".__init__(self)" |
            super.init_body |
            "self.impl = self.getImpl()" |
            "event.subscribe(self.impl, _(self).fire, self)" |||
                ImportFrom("_", "marketsim") |||
                ImportFrom("event", "marketsim")

        override def body = super.body | internals | getImpl | bind | reset | call
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.observable"
}
