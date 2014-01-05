package generator.python

import generator.python.order_factory.{FactoryBase, WithSignedOpt, curriedTypesAsList}
import predef._

object order_factory_on_proto
        extends gen.PythonGenerator
{
    case class FactoryParameter(curried   : List[Typed.Parameter],
                                original  : FactoryBase,
                                p         : Typed.Parameter)
            extends base.Parameter
    {
        val proto = "proto"
        val isProto = name == "proto"

        val prefix =
            (curried map { _.name } mkString "") +
            (if (original.prefix != "") "_" + original.prefix else "")

        override def assign_if_none: predef.Code =
            if (isProto) initializer match {
                case Some(x) =>
                    (s" if $name is not None else " + x.asPython) ||| Code.from(x.imports)
                case None => ""
            } else super.assign_if_none

        def call_args = curried map { _.name } mkString ","

        override def call = if (isProto) s"$proto($call_args)" else name

        def interface = s"IFunction["||| original.interface |||", "||| curriedTypesAsList(curried) |||"]"

        override def property = s"\'$name\' : " |||
                (if (isProto) interface else ty)

        def call_body_assign = s"$name = self.$name"

        def call_body_assign_arg = s"$name = $name" ||| assign_if_none

        def call_arg = s"$name = None"
    }
    
    import order_factory_curried.lookupOriginal

    class PartialFactory(args   : List[String],
                         x      : Typed.Function)
            extends FactoryBase(lookupOriginal(args, x))
    {
        val original = gen.generationUnit(f).get match {
            case x : FactoryBase => x
            case x : WithSignedOpt => x.original
            case _ => throw new Exception("original factory is not of appropriate type")
        }

        override type Parameter = FactoryParameter
        override val curried = x.parameters find { _.name == "proto" } match {
            case Some(p) =>
                val ini = p.initializer.get.asInstanceOf[Typed.FunctionCall].target
                val factory = gen.generationUnit(ini).get match {
                    case x : FactoryBase => x
                    case _ => throw new Exception("original factory is not of appropriate type")
                }
                factory.curried
            case None => throw new Exception("Here should be a parameter with name proto")
        }
        val curried_parameters = curried map { FactoryParameter(curried, original, _) }
        val parameters  = x.parameters map { FactoryParameter(curried, original, _) }

        override val prefix = curried map { _.name } mkString ""
        override def name = prefix + "_" + original.name
        override def alias = original.alias

        override def interface =
            s"IFunction["||| original.interface |||
            ", "||| curriedTypesAsList(curried) |||"]" |||
            ImportFrom("IFunction", "marketsim")

        override def base_classes = interface

        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)

        val original_module_infix = if (original.curried == Nil) "" else "curried._"

        override def call_body =
                call_body_assignments |
                s"""return ${original.name}($call_fields)"""  |||
                ImportFrom(original.name, "marketsim.gen._out.order._" + original_module_infix + original.name)

        override def call_args =
            join_fields(
                { _.call_arg }, ",",
                curried_parameters)
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new PartialFactory(args, f)
    }

    val name = "python.order.factory.on_proto"
}
