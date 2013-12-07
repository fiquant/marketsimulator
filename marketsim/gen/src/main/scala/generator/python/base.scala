package generator.python

import AST.PyPrintable
import predef._
import predef.Import
import predef.ImportFrom
import scala.Some

package object base {

    val tab = "    "
    val comma = ","

    abstract class Class extends PyPrintable with gen.GenerationUnit
    {
        def name : String
        def body : Code
        def registration : Code
        def imports : Code = ""
        def base_class : Code = "object"

        def toPython = {
            withImports(imports | nl | registration | s"class $name(" ||| base_class ||| "):" |> body).toString
        }
    }

    abstract class Function extends PyPrintable with gen.GenerationUnit
    {
        def name : String
    }


    def withImports(code: => predef.Code) : Code =
        new WithoutImports((code.imports map { _.repr + crlf } mkString "") + code)

    abstract class Parameter {

        val p : Typed.Parameter

        def name = p.name
        def ty = p.ty.asPython
        def s_initializer = if (p.initializer.nonEmpty) "= None" else ""

        def init = s"$name $s_initializer"
        def assign : Code = {
            s"self.$name = $name" |||
                    (p.initializer match {
                        case Some(x) => (s" if $name is not None else " + x.asPython) ||| Code.from(x.imports)
                        case None => ""})
        }

        def property = s"\'$name\' : $ty" ||| ImportFrom(ty, "marketsim")
        def repr = s"""$name = \"+repr(self.$name)+\" """
        def call = s"self.$name"
    }

    def Def(name : String, args : Code, body : Code) = {
        val a = if (args.toString == "") "" else ", " + args
        s"def $name(self$a):" |> withImports(body) | ""
    }

    def Prop(name : String, body : Code) =
        "@property" |
        s"def $name(self):" |> body | ""


    abstract class Printer extends Class {
        type Parameter <: base.Parameter
        def name        : String
        def docstring   : List[String]
        def alias       : String
        def category    : String
        def parameters  : List[Parameter]

        def registration = s"@registry.expose(['$category', '$alias'])" ||| ImportFrom("registry", "marketsim")

        def join_fields(p : Parameter => Code, sep : Code = ", ") : Code = Code.from(parameters map p, sep)

        def init_fields = join_fields({ _.init })
        def assign_fields = join_fields({ _.assign }, nl)
        def property_fields = join_fields({ _.property }, comma + nl)
        def repr_fields = join_fields({ _.repr })
        def call_fields = join_fields({ _.call })

        def impl_function = name

        def doc = s"""\"\"\" ${docstring.mkString(crlf)}$crlf\"\"\" """

        def init_body = assign_fields

        def init = Def("__init__", init_fields, init_body)

        def label = Prop("label", "return repr(self)")

        def properties = "_properties = {" |> property_fields | "}"

        def repr_body : Code = s"""return "$name($repr_fields)" """

        def repr = Def("__repr__", "", repr_body)

        def call_body : Code
        def call = Def("__call__", "*args, **kwargs", call_body)

        def body = doc | init | label | properties | repr
    }

    abstract class Intrinsic extends Printer
    {
        def impl_module : String

        def call_body : Code = s"""return $impl_module.$impl_function($call_fields)""" ||| Import(impl_module)
    }

}
