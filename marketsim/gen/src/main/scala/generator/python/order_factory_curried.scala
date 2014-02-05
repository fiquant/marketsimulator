package generator.python

import generator.python.order_factory.{FactoryBase, curriedTypesAsList}
import predef._

object order_factory_curried
        extends gen.PythonGenerator
{
    case class FactoryParameter(p : Typed.Parameter) extends base.Parameter
    {
        def call_body_assign = s"$name = self.$name"

        def call_body_assign_arg = s"$name = $name" ||| assign_if_none

        def call_arg = s"$name = None"

        override def call = name
    }

    def lookupOriginal(args   : List[String],
                       f      : Typed.Function) =
    {
        f.parent getFunction args(0) match {
            case Some(x) => x
            case None    =>
                throw new Exception("cannot find original for curried factory " + f.name)
        }
    }


    class PartialFactory(val args   : List[String],
                         x          : Typed.Function)
            extends FactoryBase
    {
        val f = lookupOriginal(args, x)

        val original = gen.generationUnit(f).get match {
            case x : FactoryBase => x
            case _ => throw new Exception("original factory is not of appropriate type")
        }

        override type Parameter = FactoryParameter
        val parameters  = x.parameters map FactoryParameter
        override val curried = f.parameters filter { p => !(x.parameters contains p) }
        val curried_parameters =  curried map FactoryParameter

        override def name = (curried map { _.name } mkString "") + "_" + original.name
        override def alias = original.alias

        override def base_class = s"IFunction["||| original.interface |||", "||| curriedTypesAsList(curried) |||"]"
        override def interface = base_class
        override def base_classes = interface

        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)
        def call_body_assign_args = join_fields({ _.call_body_assign_arg }, crlf, curried_parameters)

        val original_module_infix = if (original.curried == Nil) "" else "curried._"

        override def call_body = call_body_assign_args |
                call_body_assignments |
                s"""return ${original.name}(${original.init_raw_fields})""" |||
                ImportFrom(original.name, "marketsim.gen._out.order._" + original_module_infix + original.name)

        override def call_args = join_fields({ _.call_arg }, ",", curried_parameters)
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new PartialFactory(args, f)
    }

    val name = "python.order.factory.curried"
}
