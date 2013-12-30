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

        override def call = name
    }

    class Factory(val args   : List[String],
                  val f      : Typed.Function)
            extends base.Printer
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

    class SignedFactory(side        : Typed.Parameter,
                        volume      : Typed.Parameter,
                        rest        : List[Typed.Parameter],
                        original    : Factory)
            extends Factory(original.args, original.f)
    {
        override def call_fields = original.call_fields

        override val parameters  = (Typed.Parameter("signedVolume",
                                                    volume.ty,
                                                    volume.initializer,
                                                    volume.comment) :: rest) map Parameter

        override val name = original.name + "Signed"
        override val alias = name
    }

    class WithSignedOpt(args : List[String], f : Typed.Function) extends gen.GenerationUnit
    {
        val original = new Factory(args, f)

        def name = original.name

        def extractSideVolume(parameters : List[Typed.Parameter]) =
        {
            val (side, rest_0) = parameters.partition({ _.name == "side"})
            val (volume, rest_1) = rest_0.partition({ _.name == "volume" })

            if (side.length == 1 && volume.length == 1)
                Some((side(0), volume(0), rest_1))
            else
                None
        }

        def extractSide(parameters : List[Typed.Parameter]) =
        {
            val (side, rest_0) = parameters.partition({ _.name == "side"})

            if (side.length == 1)
                Some((side(0), rest_0))
            else
                None
        }

        override def toString = original.toString + crlf + (extractSideVolume(f.parameters) match {
                    case Some((side, volume, rest)) =>
                        new SignedFactory(side, volume, rest, original).toString
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
