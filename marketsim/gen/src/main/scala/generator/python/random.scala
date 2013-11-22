package generator.python

object random extends gen.PythonGenerator
{
    import PyGen.tab

    case class ParameterOfRandom(p : Typed.Parameter) extends PyGen.ParameterBase
    {
        val name = p.name
        val ty = "float"
        val s_initializer = p.initializer.toString
    }

    case class ImportRandom(name        : String,
                            parameters  : List[ParameterOfRandom],
                            alias       : String,
                            docstring   : String) extends PyGen.Printer()
    {
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"
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

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        val params = f.parameters map ParameterOfRandom
        val x = new ImportRandom(f.name, params, f.docstring.get.brief, f.docstring.get.detailed)

        x.prologue + x
    }

    val name = "python.random"

}
