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

        def call_arg = s"$name = None"
    }


    class PartialFactory(curried  : List[Typed.Parameter],
                         rest     : List[Typed.Parameter],
                         original : FactoryBase)
            extends FactoryBase(original.f)
    {
        override type Parameter = PartialFactoryParameter
        val parameters  = rest map PartialFactoryParameter
        val curried_parameters = curried map PartialFactoryParameter

        override def name = (curried map { _.name } mkString "") + "_" + original.name
        override def alias = original.alias

        override def registration = super.registration |
            "@types.sig("||| curriedTypes(curried) |||", IOrderGenerator)" |||
            ImportFrom("types", "marketsim")

        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)
        def call_body_assign_args = join_fields({ _.call_body_assign_arg }, crlf, curried_parameters)

        override def call_body = call_body_assign_args |
                call_body_assignments |
                s"""return ${original.name}(${original.call_fields})"""

        override def call_args = join_fields({ _.call_arg }, ",", curried_parameters)
    }

    case class PartialFactoryOnProtoParameter(curried   : List[Typed.Parameter],
                                              p         : Typed.Parameter)
            extends base.Parameter
    {
        val proto = "proto"
        val isProto = name == "proto"

        val prefix = curried map { _.name } mkString ""

        def prefixize(x : ImportFrom) = x.copy(what = prefix + "_" + x.what)

        override def assign_if_none: predef.Code =
            if (isProto) initializer match {
                case Some(x) => (s" if $name is not None else ${prefix}_" + x.asPython) ||| prefixize(x.imports(0).asInstanceOf[ImportFrom])
                case None => ""
            } else super.assign_if_none

        def call_args = curried map { _.name } mkString ","

        override def call = if (isProto) s"self.$proto($call_args)" else super.call

        override def property = s"\'$name\' : " |||
                (if (isProto) s"meta.function("||| curriedTypes(curried) |||", IOrderGenerator)" |||
                        ImportFrom("meta", "marketsim") |||
                        ImportFrom("IOrderGenerator", "marketsim")
                else ty)

        def call_body_assign = s"$name = self.$name"

        def call_body_assign_arg = s"$name = $name" ||| assign_if_none

        def call_arg = s"$name = None"
    }


    def paramTypesInPython(curried: List[Typed.Parameter]) = {
        if (curried.length == 1)
            curried(0).ty
        else
            TypesBound.Tuple(curried map { _.ty })
    }

    def curriedTypes(curried : List[Typed.Parameter]) = {
        val curr_types = TypesBound.Tuple(curried map { _.ty })

        curr_types.toPython ||| Code.from(curr_types.imports)
    }

    class PartialFactoryOnProto(curried  : List[Typed.Parameter],
                                original : FactoryBase)
            extends FactoryBase(original.f)
    {
        override type Parameter = PartialFactoryOnProtoParameter
        val parameters  = original.f.parameters map { PartialFactoryOnProtoParameter(curried, _) }

        val prefix = curried map { _.name } mkString ""
        override def name = prefix + "_" + original.name
        override def alias = original.alias

        override def registration = super.registration |
            "@sig("||| curriedTypes(curried) |||", IOrderGenerator)" |||
            ImportFrom("sig", "marketsim.types") |||
            ImportFrom("IFunction", "marketsim")


        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)

        override def call_body =
                call_body_assignments |
                s"""return ${original.name}($call_fields)"""

        override def call_args =
            join_fields(
                { _.call_arg }, ",",
                curried map { PartialFactoryOnProtoParameter(curried, _) }
            )
    }

    class WithSignedOpt(args : List[String], f : Typed.Function) extends gen.GenerationUnit
    {
        val original = new Factory(args, f)

        def name = original.name

        def extract(names : List[String], parameters : List[Typed.Parameter])
            : Option[(List[Typed.Parameter], List[Typed.Parameter])] = names match
        {
            case Nil =>
                Some((Nil, parameters))

            case n :: tl =>

                val (curried, rest_0) = parameters partition { _.name == n}

                if (curried.length == 1) {
                    extract(tl, rest_0) match {
                        case Some((c_1, r_1)) => Some((curried(0) :: c_1, r_1))
                        case None             => None
                    }
                }
                else
                    None
        }

        def hasProto(parameters : List[Typed.Parameter]) = parameters exists { _.name == "proto" }

        def createParam(name : String, ty : TypesBound.Base = Types.floatFunc) =
            Typed.Parameter(name, ty, None, Nil)

        val sideParam = createParam("side", Types.sideFunc)
        val volumeParam = createParam("volume")
        val priceParam = createParam("price")

        def partialFactory(curried  : List[Typed.Parameter],
                           base     : FactoryBase = original) =
            extract(curried map { _.name }, f.parameters) match {
                case Some((cr, rest)) =>
                    Some(new PartialFactory(cr, rest, base))
                case _ =>
                    if (hasProto(f.parameters))
                        Some(new PartialFactoryOnProto(curried,base))
                    else
                        None
            }

        val signedFactory =
            extract(List("side", "volume"), f.parameters) match {
                case Some((side :: volume :: Nil, rest)) =>
                    Some(new SignedFactory(side, volume, rest, original))
                case _ => None
            }

        def ifSome[A](x : Option[A]) = if (x.nonEmpty) x.get.toString + crlf else ""

        override def toString = original.toString + crlf +
                ifSome(signedFactory) +
                ifSome(partialFactory(sideParam :: Nil)) +
                ifSome(partialFactory(volumeParam :: Nil)) +
                ifSome(partialFactory(priceParam :: Nil)) +
                ifSome(partialFactory(sideParam :: priceParam :: Nil))
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new WithSignedOpt(args, f)
    }

    val name = "python.order.factory"
}
