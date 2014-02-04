package generator.python

import predef.PyPrintable
import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_observable extends gen.PythonGenerator
{
    import base.{Def, Prop}

    class Import(args : List[String], f : Typed.Function)
            extends intrinsic_function.Common(args, f)
            with    intrinsic_function.BaseClass_Intrinsic
    {
        val observe_args = (f tryGetAttribute "observe_args") != Some("no")

        class Parameter_(p: Typed.Parameter) extends intrinsic_function.Parameter(p)
        {
            def subscribe : Code =
                if (observe_args)
                    s"if isinstance($name, types.IEvent):" |>
                        s"event.subscribe(self.$name, self.fire, self)" |||
                    ImportFrom("event", "marketsim") |||
                    ImportFrom("types", "marketsim")
                else ""
        }


        override val parameters  = f.parameters map { new Parameter(_) }

        override type Parameter = Parameter_

        val subscriptions = join_fields({ _.subscribe }, nl)

        override def base_class = implementationBase

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
