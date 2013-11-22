package generator.python

object mathops extends Typed.AnnotationHandler
{
    import PyGen.{tab, crlf}

    case class ParameterOfMathops(name : String, initializer : Double) extends PyGen.ParameterBase
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
                             parameters  : List[ParameterOfMathops],
                             docstring   : String) extends PyGen.Printer()
    {
        type Parameter = ParameterOfMathops
        val impl_module = "math"
        val alias = name
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

    def apply(f : Typed.Function) = ("","",Nil)
    val name = "python.mathops"
}
