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
    {   self =>

        val observe_args = (f tryGetAttribute "observe_args") != Some("no")

        class Parameter_(p: Typed.Parameter)
                extends intrinsic_function.Parameter(p)
                with    base.SubscribeParameter
        {
            override def observe_args = self.observe_args
        }

        override val parameters  = f.parameters map { new Parameter(_) }

        override type Parameter = Parameter_

        override def base_class = implementationBase
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.intrinsic.observable"
}
