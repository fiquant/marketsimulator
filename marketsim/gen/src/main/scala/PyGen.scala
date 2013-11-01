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

        def join_fields(p : Parameter => String, sep : String) = parameters.map(p).mkString(sep)

        def init_fields = join_fields({ _.init }, ",")
        def assign_fields = join_fields({ _.assign }, crlf + tab + tab)

        def header = s"""
        |$registration
        |class $name($base_class):
        |""".stripMargin

        def doc = s"""
        |
        |$tab\"\"\" $docstring
        |$tab\"\"\"
        |""".stripMargin

        def init_body = s"""
        |
        |$tab$tab$assign_fields
        |""".stripMargin

        def init = s"""
        |
        |${tab}def __init__(self, $init_fields):
        |$init_body
        |""".stripMargin

        def label = s"""
        |
        |${tab}@property
        |${tab}def label(self):
        |$tab${tab}return repr(self)
        |""".stripMargin
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
        |
        |${tab}def _casts_to(self, dst):
        |$tab${tab}return $name._types[0]._casts_to(dst)
        |""".stripMargin


//        @cached_property
//        def callfields(self):
//        return self.joinfields("self.%(name)s")

        val impl_module = "random"




        override def toString = {
            ""
        }
    }

    def getRandoms(lst : List[Option[ImportRandom]])  = lst.flatMap({ s => s })
}
