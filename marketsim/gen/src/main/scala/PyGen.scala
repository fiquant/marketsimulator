package object PyGen {

    val crlf = "\r\n"
    val tab = "    "
    val comma = ","

    abstract class ParameterBase {
        def name            : String
        def s_initializer   : String
        def ty              : String

        def init = s"$name = $s_initializer"
        def assign = s"self.$name = $name"
        def property = s"\'$name\' : $ty"
        def repr = s"""$name = \"+repr(self.$name)+\" """
        def call = s"self.$name"
    }

    case class ParameterFloat(name : String, initializer : Double) extends ParameterBase
    {
        val ty = "float"
        val s_initializer = initializer.toString
    }

    abstract class Printer() {
        type Parameter <: ParameterBase
        def name        : String
        def docstring   : String
        def alias       : String
        def category    : String
        def parameters  : List[Parameter]

        def registration = s"@registry.expose(['$category', '$alias'])"
        def base_class = "object"

        def join_fields(p : Parameter => String, sep : String = ", ") = parameters.map(p).mkString(sep)

        def init_fields = join_fields({ _.init })
        def assign_fields = join_fields({ _.assign }, crlf + tab + tab)
        def property_fields = join_fields({ _.property }, comma + crlf + tab + tab)
        def repr_fields = join_fields({ _.repr })
        def call_fields = join_fields({ _.call })

        def impl_function = name

        def header = s"""
        |$registration
        |class $name($base_class):
        |""".stripMargin

        def doc = s"""$tab\"\"\" ${docstring.replaceAll(crlf, crlf+tab)}$crlf$tab\"\"\" """

        def init_body = s"""$tab$tab$assign_fields"""

        def init = s"""
        |${tab}def __init__(self, $init_fields):
        |$init_body
        |""".stripMargin

        def label = s"""
        |${tab}@property
        |${tab}def label(self):
        |$tab${tab}return repr(self)
        |""".stripMargin

        def properties = s"""
        |${tab}_properties = {
        |${tab}${tab}$property_fields
        |${tab}}
        |""".stripMargin

        def repr_body = s"""$tab${tab}return "$name($repr_fields)" """

        def repr = s"""
        |${tab}def __repr__(self):
        |$repr_body
        |""".stripMargin

        def impl_module : String

        def call_body = s"""$tab${tab}return $impl_module.$impl_function($call_fields)"""

        def call = s"""
        |${tab}def __call__(self, *args, **kwargs):
        |$call_body
        |""".stripMargin

        override def toString = s"""$header$doc$init$label$properties$repr"""

    }

    case class ImportRandom(name        : String,
                            parameters  : List[ParameterFloat],
                            alias       : String,
                            docstring   : String) extends Printer()
    {
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"

        type Parameter = ParameterFloat

        def casts_to = s"""
        |${tab}def _casts_to(self, dst):
        |$tab${tab}return $name._types[0]._casts_to(dst)
        |""".stripMargin

        val impl_module = "random"

        override def toString = super.toString + s"""$call$casts_to"""
    }

    def getRandoms(lst : List[Option[ImportRandom]])  = lst.flatMap({ s => s })
}
