package generator.python

import AST.PyPrintable
import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_observable extends gen.PythonGenerator
{
    import base.{Def, Prop}

    class Parameter(p: Typed.Parameter) extends intrinsic_function.Parameter(p)
    {
        def subscribe =
            s"if isinstance($name, types.IEvent):" |>
                s"event.subscribe(self.$name, self.fire, self)" |||
            ImportFrom("event", "marketsim") |||
            ImportFrom("types", "marketsim")
    }

    class Import(args : List[String], f : Typed.Function) extends intrinsic_function.Common(args, f)
    {
        override val parameters  = f.parameters map { new Parameter(_) }

        override type Parameter = intrinsic_observable.Parameter

        val subscriptions = join_fields({ _.subscribe }, nl)

        override def base_class = s"$implementation_class" |||
                                ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")

        override def init_body =    super.init_body |
                                    s"$implementation_class.__init__(self)" |
                                    subscriptions
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.intrinsic.observable"
}
