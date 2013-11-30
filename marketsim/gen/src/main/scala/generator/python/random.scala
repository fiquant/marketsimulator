package generator.python
import predef._

object random extends gen.PythonGenerator
{
    import base.Def

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(f : Typed.Function) extends base.Intrinsic
    {
        val name = f.name
        val parameters = f.parameters map Parameter
        val alias = f.docstring.get.brief
        val docstring = f.docstring.get.detailed
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"

        type Parameter = random.Parameter

        def casts_to = Def("_casts_to", "dst", s"return $name._types[0]._casts_to(dst)")

        val impl_module = "random"

        override val imports  : Code =
            "from marketsim import registry, types, ops" |
            "import random"

        override def body = super.body | call | casts_to
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(f)
    }

    val name = "python.random"

}
