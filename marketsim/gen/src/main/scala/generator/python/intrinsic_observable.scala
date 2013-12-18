package generator.python

import AST.PyPrintable
import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_observable extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter
    {
        def subscribe =
            s"if isinstance($name, types.IEvent):" |>
                s"event.subscribe(self.$name, self.fire, self)" |||
            ImportFrom("event", "marketsim") |||
            ImportFrom("types", "marketsim")
    }

    case class Import(args : List[String], f : Typed.Function) extends base.Printer
    {
        if (args.length != 3)
            throw new Exception(s"Annotation $name should have 3 arguments in" +
                    " form (category, label_template, implementation_class)" + "\r\n" + "In function " + f)

        val label_tmpl = args(1)
        val last_dot_idx = args(2).lastIndexOf(".")
        val implementation_module =args(2).substring(0, last_dot_idx)
        val implementation_class  =args(2).substring(last_dot_idx + 1)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = intrinsic_observable.Parameter
        val name = f.name
        val alias = name

        val subscriptions = join_fields({ _.subscribe }, nl)

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def base_class = s"$implementation_class" |||
                                ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")

        override def init_body =    super.init_body |
                                    s"$implementation_class.__init__(self)" |
                                    subscriptions

        def call_body = ""  // TODO: remove from the base class
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.intrinsic.observable"
}
