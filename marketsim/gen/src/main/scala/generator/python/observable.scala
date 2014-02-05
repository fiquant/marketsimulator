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
        def mkParam(p : Typed.Parameter) = observable.Parameter(p)
        type Parameter = observable.Parameter

        override def init_body =
            super.init_body |
            "event.subscribe(self.impl, _(self).fire, self)" |||
                ImportFrom("_", "marketsim") |||
                ImportFrom("event", "marketsim")
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.observable"
}
