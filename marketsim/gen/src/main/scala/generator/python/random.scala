package generator.python
import predef._

object random extends gen.PythonGenerator
{
    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class ImportRandom(name        : String,
                            parameters  : List[Parameter],
                            alias       : String,
                            docstring   : String) extends base.Printer()
    {
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"
        val filename = "defs/rnd.py"

        type Parameter = random.Parameter

        def casts_to = indent {
            "def _casts_to(self, dst):" |> {
                s"return $name._types[0]._casts_to(dst)"
            }
        }

        val impl_module = "random"

        val prologue =
            "from marketsim import registry, types, ops" |
            "import random" | nl

        override def toString = super.toString + s"""$call$casts_to"""
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        val params = f.parameters map Parameter
        val x = new ImportRandom(f.name, params, f.docstring.get.brief, f.docstring.get.detailed)

        x.prologue.toString + x
    }

    val name = "python.random"

}
