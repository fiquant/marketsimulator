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

    case class ParameterOfRandom(name : String, initializer : Double) extends ParameterBase
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
        val filename    : String

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
        |$tab@property
        |${tab}def label(self):
        |$tab${tab}return repr(self)
        |""".stripMargin

        def properties = s"""
        |${tab}_properties = {
        |${tab}${tab}$property_fields
        |$tab}
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

        def prologue : String

        override def toString = s"""$header$doc$init$label$properties$repr"""

    }

    case class ImportRandom(name        : String,
                            params      : List[(String, Double)],
                            alias       : String,
                            docstring   : String) extends Printer()
    {
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"
        val parameters = params.map({ p => ParameterOfRandom(p._1,p._2) })
        val filename = "defs/rnd.py"

        type Parameter = ParameterOfRandom

        def casts_to = s"""
        |${tab}def _casts_to(self, dst):
        |$tab${tab}return $name._types[0]._casts_to(dst)
        |""".stripMargin

        val impl_module = "random"

        val prologue =
            """
              |from marketsim import registry, types, ops
              |import random
            """.stripMargin

        override def toString = super.toString + s"""$call$casts_to"""
    }

    def getRandoms(lst : List[Option[Printer]])  = lst.flatMap({
        case s @ Some(_) => s
        case _ => None
    })

    case class ParameterOfMathops(name : String, initializer : Double) extends ParameterBase
    {
        val ty = "float"
        val s_initializer = initializer.toString

        override def assign = s"""self.$name = $name
        |$tab${tab}if isinstance($name, types.IEvent):
        |$tab${tab}${tab}event.subscribe(self.$name, self.fire, self)""".stripMargin

        def nullable = s"""$name = self.$name()
                |$tab${tab}if $name is None: return None""".stripMargin
    }

    case class ImportMathops(name        : String,
                             category    : String,
                             override val impl_function : String,
                             label_tmpl  : Option[String],
                             params      : List[(String, Double)],
                             docstring   : String) extends Printer()
    {
        type Parameter = ParameterOfMathops
        val impl_module = "math"
        val alias = name
        val parameters = params.map({ p => ParameterOfMathops(p._1,p._2) })
        val filename = "defs/mathops.py"

        override def repr_body = s"""$tab${tab}return "$label_tmpl" % self.__dict__"""

        override val base_class = "Observable[float]"

        override def init_body = s"""$tab${tab}Observable[float].__init__(self)
        |${super.init_body}""".stripMargin

        def nullable_fields = join_fields({ _.nullable}, crlf + tab + tab)

        override def call_body = s"$tab$tab$nullable_fields" + crlf + super.call_body

        override def toString = super.toString + s"""$call"""

        val prologue =
            """
              |from marketsim import registry, types, event
              |import math
              |from _all import Observable, Constant
            """.stripMargin
    }
}
