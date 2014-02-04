package generator.python
import predef._

object strategy extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
    {
        val parameters  = f.parameters map Parameter

        type Parameter = strategy.Parameter
        val name = base.decoratedName(f)
        val alias = f.name

        override def init_body = super.init_body |
                "self.impl = self.getImpl()"|
                "self.on_order_created = event.Event()" |
                "event.subscribe(self.impl.on_order_created, _(self)._send, self)" |||
                ImportFrom("event", "marketsim") |||
                ImportFrom("_", "marketsim")

        override def base_class = "ISingleAssetStrategy" ||| ImportFrom("ISingleAssetStrategy", "marketsim")

        def bind = Def("bind", "ctx", "self._ctx = ctx.clone()")

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
            ImportFrom("context", "marketsim")

        def send = Def("_send", "order, source", "self.on_order_created.fire(order, self)")

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def body = super.body | internals | getImpl | bind | reset | send

        def getImpl = Def("getImpl", "", "return " ||| f.body.get.asCode)

        def internals = "_internals = ['impl']"
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.strategy"
}
