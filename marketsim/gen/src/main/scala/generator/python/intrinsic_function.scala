package generator.python

import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    class Parameter(val p : Typed.Parameter) extends base.Parameter

    abstract class Common(val args : List[String], val f : Typed.Function) extends base.Printer
    {
        val name = f.name
        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_class)" + "\r\n" + "In function " + f)

        val last_dot_idx = args(0).lastIndexOf(".")
        val implementation_module =args(0).substring(0, last_dot_idx)
        val implementation_class  =args(0).substring(last_dot_idx + 1)

        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        val alias = name

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def repr = if (label_tmpl != "N/A") super.repr else ""

        def call_body = ""  // TODO: remove from the base class
    }


    class Import(args : List[String], f : Typed.Function) extends Common(args, f)
    {
        override val parameters  = f.parameters map { new Parameter(_) }

        override type Parameter = intrinsic_function.Parameter

        def base_class_function : Code =
            f.ret_type.returnTypeIfFunction match {
                case Some(t) => s"Function[${t.asPython}], " |||
                                ImportFrom("Function", "marketsim.ops._function") |||
                                Code.from(t.imports)
                case None => ""
        }

        override def base_class = base_class_function |||
                                  implementation_class |||
                                  ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")

        override def init_body = super.init_body | s"$implementation_class.__init__(self)"
    }


    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        if (f.ret_type canCastTo Types.FloatFunc)
            new Import(args, f)
        else
            new Import(args, f)
    }

    val name = "python.intrinsic.function"
}
