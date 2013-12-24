package generator.python

import predef._
import predef.ImportFrom
import scala.Some

object order_factory extends gen.PythonGenerator
{
    case class Parameter(p : Typed.Parameter) extends base.Parameter
    {
        override def assign =
            super.assign |
            s"if isinstance($name, types.IEvent):" |>
                s"event.subscribe(self.$name, self.fire, self)" |||
            ImportFrom("event", "marketsim") |||
            ImportFrom("types", "marketsim")

        def check_none : Code = p.name match {
            case "volume" => s"if $name is None or abs($name) < 1: return None" | s"$name = int($name)"
            case _ => s"if $name is None: return None"
        }

        def nullable =
            s"$name = self.$name()" |
            check_none


        override def call = name

    }

    case class Import(args : List[String], f : Typed.Function) extends base.Printer
    {
        val name = f.name

        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_class)" + "\r\n" + "In function " + f)

        val last_dot_idx = args(0).lastIndexOf(".")
        val implementation_module =args(0).substring(0, last_dot_idx)
        val implementation_class  =args(0).substring(last_dot_idx + 1)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = order_factory.Parameter
        val alias = name

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        val ty = f.ret_type.returnTypeIfFunction.get.asPython

        override val base_class = s"Observable[$ty]" |||
                                    ImportFrom(ty, "marketsim") |||
                                    ImportFrom("Observable", "marketsim.ops._all")

        override val base_classes = "IOrderGenerator, " ||| ImportFrom("IOrderGenerator", "marketsim") ||| base_class

        override def init_body = base_class ||| ".__init__(self)" | super.init_body

        def nullable_fields = join_fields({ _.nullable}, crlf)

        override def call_body = nullable_fields |
                s"""return $implementation_class($call_fields)""" |||
                ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")


        override def body = super.body | call
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.order.factory"
}
