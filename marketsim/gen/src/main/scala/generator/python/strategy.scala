package generator.python
import predef._

object strategy extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.Bind
            with    base.HasImpl
    {
        def mkParam(p : Typed.Parameter) = strategy.Parameter(p)
        type Parameter = strategy.Parameter

        override def init_body = super.init_body |
                "self.on_order_created = event.Event()" |
                "event.subscribe(self.impl.on_order_created, _(self)._send, self)" |||
                ImportFrom("event", "marketsim") |||
                ImportFrom("_", "marketsim")

        def myBase = "ISingleAssetStrategy" ||| ImportFrom("ISingleAssetStrategy", "marketsim")

        override def base_class_list = myBase :: Nil

        def send = Def("_send", "order, source", "self.on_order_created.fire(order, self)")

        override def body = super.body | send
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.strategy"
}
