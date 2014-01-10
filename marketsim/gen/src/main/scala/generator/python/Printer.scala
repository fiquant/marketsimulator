package generator.python

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}

    trait Printable {
        def toPython : String
        def imports : List[predef.Importable]
    }

    object types {

        trait Bound extends Printable

        trait Unit extends Bound {
            def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
            def imports = Nil

        }

        trait Tuple extends Bound {
            val elems : List[Bound]
            def toPython = elems map { _.toPython } map { _ + "," } mkString ("(", "", ")")

            def imports = elems flatMap { _.imports }
        }

        trait Function extends Bound {
            val args : List[Bound]
            val ret : Bound
            def toPython = {
                val types = (ret :: args) map { _.toPython } mkString ","
                s"IFunction[$types]"
            }

            def imports = (predef.ImportFrom("IFunction", "marketsim") :: ret.imports) ++ (args flatMap { _.imports })
        }

        trait UsedDefined extends st.UsedDefined with Printable with Bound
        {
            self: TypesBound.UserDefined =>

            val builtins = Map("Float"  -> "float",
                               "Int"    -> "int",
                               "Boolean"-> "bool",
                               "String" -> "str")

            def imports =
                (if (builtins contains decl.name)
                    Nil
                 else
                    predef.ImportFrom(decl.name, "marketsim") :: Nil) ++ (genericArgs flatMap { _.imports })


            def toPython =
                builtins.getOrElse(decl.name, decl.name) +
                (if (genericArgs.isEmpty) "" else genericArgs map { _.toPython } mkString ("[", ",", "]"))
        }
    }

    trait PrintablePort extends Printable
    {
        def toScala : String
        override def toPython = toScala
    }

    trait Expr extends pp.Expr with predef.ScPyPrintable

    trait BinOp extends pp.BinOp[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }

    trait Cast extends Printable
    {
        val x : Expr
        def toPython = x.toPython
        def imports = x.imports
    }

    trait Neg extends pp.Neg[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports
    }

    trait IfThenElse extends pp.IfThenElse[Typed.Expr, Typed.Expr] with PrintablePort
    {
        override def toPython = s"($cond)[${wrap(x)}, ${wrap(y)}]"

        override def imports = x.imports ++ y.imports ++ cond.imports
    }

    trait StringLit extends pp.StringLit with PrintablePort
    {
        override def imports = Nil
    }

    trait IntLit extends pp.IntLit with PrintablePort
    {
        override def imports = Nil
    }

    trait And extends pp.And[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }
    trait Or extends pp.Or[Typed.Expr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    trait Not extends pp.Not[Typed.Expr, Typed.Expr] with PrintablePort {
        override def imports = x.imports
    }

    trait Condition extends pp.Condition[Typed.Expr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    type Priority_0 = pp.Priority_0

    trait FloatLit extends Expr with Priority_0 {
        self: Typed.FloatLit =>
        override def toPython = x.toString

        def imports = Nil
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        override def toPython = "self." + p.name

        def imports = Nil
    }

    trait FunctionRef extends Expr with Priority_0 {
        self: Typed.FunctionRef =>
        override def toPython = f.name

        def imports = importsOf(f) :: Nil
    }

    def moduleName(target : Typed.Function) = {
        val name = target.parent.qualifiedName.toString
        "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name
    }

    def importsOf(target : Typed.Function) =
        predef.ImportFrom(target.name, moduleName(target))

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>
        override def toPython =
            target + arguments.map({ _._2 }).mkString("(",",",")")

        override def imports =
            target.imports ++ (arguments flatMap { p => p._2.imports })
    }

}
