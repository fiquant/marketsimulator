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

        def check_none_aux(name : String) : Code = name match {
            case "volume" =>
                s"if abs($name) < 1: return None" |
                s"$name = int($name)"
            case "signedVolume" =>
                s"side = Side.Buy if signedVolume > 0 else Side.Sell" |
                s"volume = abs(signedVolume)" |
                check_none_aux("volume")

            case _ => ""
        }

        def nullable =
            s"$name = self.$name()" |
            s"if $name is None: return None" |
            check_none_aux(name)


        override def call = p.name match {
            case "signedVolume" => "side, volume"
            case _ => name
        }

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

    class WithSignedOpt(args : List[String], f : Typed.Function) extends gen.GenerationUnit
    {
        val original = new Import(args, f)

        def name = original.name

        override def toString = original.toString + crlf + (f.parameters match {
                    case s :: v :: tl if s.name == "side" && v.name == "volume" =>
                        new Import(
                            args,
                            Typed.Function(
                                f.parent,
                                f.name + "Signed",
                                Typed.Parameter(
                                    "signedVolume",
                                    v.ty,
                                    v.initializer,
                                    v.comment) :: tl,
                                f.ret_type,
                                f.body,
                                f.docstring,
                                f.annotations,
                                f.attributes
                            )).toString
                    case _ => ""
                })
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new WithSignedOpt(args, f)
    }

    val name = "python.order.factory"
}
