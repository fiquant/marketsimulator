package generator.python

import predef._

object intrinsic_function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function) extends base.Printer
    {
        if (args.length != 3)
            throw new Exception(s"Annotation $name should have 3 arguments in" +
                    " form (category, label_template, implementation_class)" + "\r\n" + "In function " + f)

        val category = args(0)
        val label_tmpl = args(1)
        val last_dot_idx = args(2).lastIndexOf(".")
        val implementation_module =args(2).substring(0, last_dot_idx)
        val implementation_class  =args(2).substring(last_dot_idx + 1)

        val parameters  = f.parameters map Parameter
        val docstring  = f.docstring match {
            case Some(d) => d.detailed
            case None => Nil
        }

        type Parameter = intrinsic_function.Parameter
        val name = f.name
        val alias = name

        override def repr_body = s"""return "$label_tmpl" % self.__dict__"""

        override def base_class = s"Function[float], $implementation_class"

        override def registration = super.registration |||
                        ImportFrom("IObservable", "marketsim") |||
                        ImportFrom("IFunction", "marketsim") |||
                        ImportFrom("Function", "marketsim.ops._function") |||
                        ImportFrom(implementation_class, s"marketsim.gen._intrinsic.$implementation_module")

        override def init_body = super.init_body | s"$implementation_class.__init__(self)"

        def call_body = ""
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.intrinsic.function"
}
