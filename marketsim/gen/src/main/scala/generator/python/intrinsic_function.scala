package generator.python

import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    abstract class Common(val args : List[String], val f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.IntrinsicEx
    {
        override def repr = if (label_tmpl.toString != "N/A") super.repr else ""

        override def call_body = ""  // TODO: remove from the base class
    }

    trait BaseClass_Intrinsic extends Common
    {
        override def init_body = super.init_body | s"$implementation_class.__init__(self)"

        def implementationBase =
            implementation_class |||
                  ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")

        override def base_class_list = implementationBase :: super.base_class_list
    }


    class Import(args : List[String], f : Typed.Function)
            extends Common(args, f)
            with    base.BaseClass_Function
            with    BaseClass_Intrinsic
    {
        override type Parameter = intrinsic_function.Parameter
        def mkParam(p : Typed.Parameter) = intrinsic_function.Parameter(p)
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        if (f.ret_type canCastTo Typed.topLevel.floatFunc)
            new Import(args, f)
        else
            new Import(args, f)
    }

    val name = "python.intrinsic.function"
}
