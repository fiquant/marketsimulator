package generator.python

import AST.PyPrintable
import predef._

package object base {

    val tab = "    "
    val comma = ","

    object Annotations
    {
        import Typed.Annotations._

        override def toString = registry.toString()

        // TODO: non-intrusive registration
        register(random)
        register(mathops)
    }

    abstract class Class extends PyPrintable
    {
        def name : String
        def body : Any
        def registration :  Any
        def imports : String
        def base_class : String  = "object"

        def toPython = imports | nl | registration.toString | s"class $name($base_class):" |> body | nl
    }

    abstract class Parameter {

        val p : Typed.Parameter

        def name = p.name
        def ty = p.ty.asPython
        def s_initializer = if (p.initializer.nonEmpty) " = " + p.initializer.get.asPython else ""

        def init = s"$name $s_initializer"
        def assign = s"self.$name = $name"
        def property = s"\'$name\' : $ty"
        def repr = s"""$name = \"+repr(self.$name)+\" """
        def call = s"self.$name"
    }

    def Def(name : => String, args : => String, body : => Any) = {
        val a = if (args == "") "" else ", " + args
        s"def $name(self$a):" |> body | nl
    }

    def Prop(name : => String, body : => Any) =
        "@property" |
        s"def $name(self):" |>
            body |
        nl


    abstract class Printer extends Class {
        type Parameter <: base.Parameter
        def name        : String
        def docstring   : List[String]
        def alias       : String
        def category    : String
        def parameters  : List[Parameter]

        def registration = s"@registry.expose(['$category', '$alias'])"

        def join_fields(p : Parameter => String, sep : String = ", ") = parameters map p mkString sep

        def init_fields = join_fields({ _.init })
        def assign_fields = join_fields({ _.assign }, crlf)
        def property_fields = join_fields({ _.property }, comma + crlf)
        def repr_fields = join_fields({ _.repr })
        def call_fields = join_fields({ _.call })

        def impl_function = name

        def doc = s"""\"\"\" ${docstring.mkString(crlf)}$crlf\"\"\" """

        def init_body = assign_fields

        def init = Def("__init__", init_fields, init_body)

        def label = Prop("label", "return repr(self)")

        def properties = "_properties = {" |> property_fields | "}" | nl

        def repr_body = s"""return "$name($repr_fields)" """

        def repr = Def("__repr__", "", repr_body)

        def impl_module : String

        def call_body = s"""return $impl_module.$impl_function($call_fields)"""

        def call = Def("__call__", "*args, **kwargs", call_body)

        def body = doc | init | label | properties | repr | nl
    }


}
