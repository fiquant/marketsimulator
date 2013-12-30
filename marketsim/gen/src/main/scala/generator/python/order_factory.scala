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

    abstract class FactoryBase(val f : Typed.Function)
        extends base.Printer
    {
        def name = f.name

        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        def alias = name

        def ty = f.ret_type.returnTypeIfFunction.get.asPython

        override def body = super.body | call
    }

    class Factory(val args  : List[String],
                  _f        : Typed.Function)
            extends FactoryBase(_f)
    {
        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_class)" + "\r\n" + "In function " + f)

        val last_dot_idx = args(0).lastIndexOf(".")
        val implementation_module =args(0).substring(0, last_dot_idx)
        val implementation_class  =args(0).substring(last_dot_idx + 1)

        val parameters  = f.parameters map Parameter

        type Parameter = order_factory.Parameter

        override def base_class = s"Observable[$ty]" |||
                                    ImportFrom(ty, "marketsim") |||
                                    ImportFrom("Observable", "marketsim.ops._all")

        override def base_classes = "IOrderGenerator, " ||| ImportFrom("IOrderGenerator", "marketsim") ||| base_class

        override def init_body = base_class ||| ".__init__(self)" | super.init_body

        def nullable_fields = join_fields({ _.nullable}, crlf)

        override def call_body = nullable_fields |
                s"""return $implementation_class($call_fields)""" |||
                ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")
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

    case class PartialFactoryParameter(p : Typed.Parameter) extends base.Parameter
    {
        def call_body_assign = s"$name = self.$name"

        def call_body_assign_arg = s"$name = $name" ||| assign_if_none
    }


    class Side_Factory(side     : Typed.Parameter,
                       rest     : List[Typed.Parameter],
                       original : Factory)
            extends FactoryBase(original.f)
    {
        override type Parameter = PartialFactoryParameter
        val parameters  = rest map PartialFactoryParameter

        override def name = "Side_" + original.name
        override def alias = original.alias

        override def registration = super.registration |
            "@sig((IFunction[Side],), IOrderGenerator)" |||
            ImportFrom("sig", "marketsim.types")

        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)

        override def call_body = PartialFactoryParameter(side).call_body_assign_arg |
                call_body_assignments |
                s"""return ${original.name}(${original.call_fields})"""

        override def call_args = "side = None"
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

        override def toString = original.toString + crlf +
                (extractSideVolume(f.parameters) match {
                    case Some((side, volume, rest)) =>
                        new SignedFactory(side, volume, rest, original).toString
                    case _ => ""
                }) + crlf +
                (extractSide(f.parameters) match {
                    case Some((side, rest)) =>
                        new Side_Factory(side, rest, original).toString
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
