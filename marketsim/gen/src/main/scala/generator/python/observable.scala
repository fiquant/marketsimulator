package generator.python
import predef._

object observable extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function) extends base.Printer
    {
        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = observable.Parameter
        val name = f.name
        val alias = name

        def bind = Def("bind", "ctx", "self._ctx = ctx.clone()")

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
                ImportFrom("context", "marketsim")

        val ty = f.ret_type.returnTypeIfFunction.get.asCode

        override val base_class = s"Observable["||| ty |||"]" |||
                                    ImportFrom(ty.toString, "marketsim") |||
                                    ImportFrom("Observable", "marketsim.ops._all")


        override def init_body =
            base_class ||| ".__init__(self)" |
            super.init_body |
            "self.impl = self.getImpl()" |
            "event.subscribe(self.impl, _(self).fire, self)" |||
                ImportFrom("_", "marketsim") |||
                ImportFrom("event", "marketsim")

        override def call_body = "return self.impl()"

        override def body = super.body | internals | getImpl | bind | reset | call

        def getImpl = Def("getImpl", "", "return " ||| f.body.get.asCode)

        def internals = "_internals = ['impl']"
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.observable"
}
