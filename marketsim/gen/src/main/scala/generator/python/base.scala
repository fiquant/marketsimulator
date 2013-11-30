package generator.python

import AST.PyPrintable
import predef._

package object base {

    val tab = "    "
    val comma = ","

    abstract class Class extends PyPrintable
    {
        def name : String
        def body : Code
        def registration : Code
        def imports : Code
        def base_class : String  = "object"

        def toPython = {
            val code = imports | nl | registration | s"class $name($base_class):" |> body
            val prologue = code.imports map { _.repr } mkString crlf
            prologue + crlf + code
        }
    }

    abstract class Parameter {

        val p : Typed.Parameter

        def name = p.name
        def ty = p.ty.asPython
        def s_initializer = if (p.initializer.nonEmpty) "= None" else ""

        def init = s"$name $s_initializer"
        def assign : Code = {
            s"self.$name = $name" +
                    (p.initializer match {
                        case Some(x) => s" if $name is not None else " + x.asPython
                        case None => ""})
        }

        def property = s"\'$name\' : $ty"
        def repr = s"""$name = \"+repr(self.$name)+\" """
        def call = s"self.$name"
    }

    def Def(name : String, args : Code, body : Code) = {
        val a = if (args.toString == "") "" else ", " + args
        s"def $name(self$a):" |> body | ""
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

        def registration = s"@registry.expose(['$category', '$alias'])"

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

        def repr_body = s"""return "$name($repr_fields)" """

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
