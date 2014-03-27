package generator.python

import generator.python.order_factory.{FactoryBase, curriedTypesAsList}
import predef._

object order_factory_on_proto
        extends gen.PythonGenerator
{
    case class PartialFactory(args   : List[String],
                              x      : Typed.Function)
            extends FactoryBase
            with    order_factory_curried.Call
            with    order_factory_curried.DecoratedNameInX
    {
        case class Parameter(fac_cur   : FactoryBase,
                             original  : FactoryBase,
                             p         : Typed.Parameter)
                extends order_factory_curried.ParameterBase
        {
            val proto = "proto"
            val isProto = name == "proto"

            val curried = fac_cur.curried

            val prefix =
                (curried map { _.name } mkString "") +
                (if (original.prefix != "") "_" + original.prefix else "")

            override def assign_if_none: predef.Code =
                if (isProto) initializer match {
                    case Some(x) =>
                        s" if $name is not None else " ||| x.asCode
                    case None => ""
                } else super.assign_if_none

            def call_args = curried map { _.name } mkString ","

            override def call = if (isProto) s"$proto($call_args)" else name

            def interface = fac_cur.interface

            override def property = s"\'$name\' : " |||
                    (if (isProto) interface.asCode else ty)
        }


        val factory_of_curried = x.parameters find { _.name == "proto" } match {
            case Some(Typed.Parameter(_, _, Some(Typed.FunctionCall(Typed.FunctionRef(f), _)), _)) =>
                val factory = gen.generationUnit(f).get match {
                    case x : FactoryBase => x
                    case _ => throw new Exception("original factory is not of appropriate type")
                }
                factory
            case None => throw new Exception("Here should be a parameter with name proto")
            case _ => throw new Exception("Here should be a parameter with function call as initializer")
        }
        def mkParam(p : Typed.Parameter) = Parameter(factory_of_curried, original, p)

        override val curried = factory_of_curried.curried

        override val prefix = curried map { _.name } mkString ""
        override def factoryName = x.name

        override def interface = x.ret_type

        override def base_class_list = interface :: Nil
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new PartialFactory(args, f)
    }

    val name = "python.order.factory.on_proto"
}
