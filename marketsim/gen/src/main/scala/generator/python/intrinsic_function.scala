package generator.python

import AST.PyPrintable
import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

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

        type Parameter = intrinsic_function.Parameter
        val alias = name

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def repr = if (label_tmpl != "N/A") super.repr else ""

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

        def call_body = ""  // TODO: remove from the base class
    }

    class ImportFunction(args : List[String], f : Typed.Function) extends PyPrintable with gen.GenerationUnit
    {
        if (args.length != 3)
            throw new Exception(s"Annotation $name should have 3 arguments in" +
                    " form (category, label_template, implementation_class)" + "\r\n" + "In function " + f)

        val category = args(0)
        val label_tmpl = args(1)
        val last_dot_idx = args(2).lastIndexOf(".")
        val implementation_module    =args(2).substring(0, last_dot_idx)
        val implementation_function  =args(2).substring(last_dot_idx + 1)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = intrinsic_function.Parameter
        val name = f.name
        val alias = name

        def registration = s"@registry.expose(['$category', '$alias'])" ||| ImportFrom("registry", "marketsim")

        def join_fields(p : Parameter => Code, sep : Code = ", ") : Code = Code.from(parameters map p, sep)

        def init_fields = join_fields({ _.init })
        def assign_fields = join_fields({ _.assign }, nl)

        def doc = s"""\"\"\" ${docstring.mkString(crlf)}$crlf\"\"\" """

        def init_body = assign_fields
        def init = Def(name, init_fields, init_body | call_body)

        def call_fields = join_fields({ _.call })
        def call_body : Code = s"""return $implementation_function($call_fields)""" |||
                ImportFrom(implementation_function, "marketsim.gen._intrinsic." + implementation_module)

        def toPython = base.withImports(registration | init).toString
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
