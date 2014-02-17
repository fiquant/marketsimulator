package generator.python

import generator.python.order_factory.{FactoryBase, curriedTypesAsList}
import predef._

object order_factory_curried
        extends gen.PythonGenerator
{
    trait ParameterBase extends base.Parameter
    {
        def call_body_assign = s"$name = self.$name"

        def call_body_assign_arg = s"$name = $name" ||| assign_if_none

        def call_arg = s"$name = None"

        override def call = name
    }

    case class FactoryParameter(p : Typed.Parameter) extends ParameterBase

    def lookupOriginal(args   : List[String],
                       f      : Typed.Function) =
    {
        f.parent getFunction args(0) match {
            case Nil    =>
                throw new Exception("cannot find original for curried factory " + f.name)
            case x :: Nil => x
            case x =>
                throw new Exception("cannot handle overloads for " + f.name)
        }
    }

    trait OriginalFactory extends base.Printer
    {
        val x : Typed.Function
        val f = lookupOriginal(args, x)

        val original = gen.generationUnit(f).get match {
            case x : FactoryBase => x
            case _ => throw new Exception("original factory is not of appropriate type")
        }
    }

    trait CurriedParameters extends base.Printer
    {
        val curried : List[Typed.Parameter]
        lazy val curried_parameters =  curried map mkParam
    }

    trait ParametersInX extends base.Printer
    {
        def x : Typed.Function
        override lazy val parameters  = x.parameters map mkParam
    }

    trait Call extends ParametersInX with CurriedParameters with OriginalFactory
    {
        override type Parameter <: ParameterBase

        def call_body_assignments = join_fields({ _.call_body_assign }, crlf)
        def call_body_assign_args = join_fields({ _.call_body_assign_arg }, crlf, curried_parameters)

        val original_module_infix = if (original.curried == Nil) "" else "curried._"

        override def call_body = call_body_assign_args |
                call_body_assignments |
                s"""return ${original.factoryName}($call_fields)""" |||
                ImportFrom(original.factoryName, "marketsim.gen._out.order._" + original_module_infix + original.factoryName.toLowerCase)

        override def call_args = join_fields({ _.call_arg }, ",", curried_parameters)
    }

    trait DecoratedNameInX extends base.Printer
    {
        def x : Typed.Function

        override def name = Printer.decoratedName(x)
    }

    case class PartialFactory(args   : List[String],
                              x      : Typed.Function)
            extends FactoryBase
            with    Call
            with    DecoratedNameInX
    {
        override type Parameter = FactoryParameter
        def mkParam(p : Typed.Parameter) = FactoryParameter(p)
        override val curried = f.parameters filter { p => !(x.parameters contains p) }

        override def factoryName = (curried map { _.name } mkString "") + "_" + original.factoryName

        def myBase = TypesBound.Function(curried map { _.ty }, original.interface)
        override def interface = myBase
        override def base_class_list = interface :: Nil

        override def call_fields = original.init_raw_fields
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new PartialFactory(args, f)
    }

    val name = "python.order.factory.curried"
}
