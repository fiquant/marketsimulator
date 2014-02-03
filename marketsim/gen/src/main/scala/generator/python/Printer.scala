package generator.python
import predef._

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}
    import predef.{Code, Combine, ImportFrom}

    trait Printable {
        def asPython : String
        def imports : List[predef.Importable]
        def asCode  = new Combine(asPython, Code.from(imports))
    }

    object types {

        trait Bound extends Printable

        trait Unit extends Bound {
            protected def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
            def imports = Nil
        }

        trait Nothing extends Bound {
            protected def toPython =
                throw new Exception("Nothing types are not supported for python generation")
            def imports = Nil
        }

        trait Any_ extends Bound {
            protected def toPython = "object"
            def imports = Nil
        }

        trait Optional extends Bound {
            def x : Bound
            protected def toPython = x.toString
            def imports = x.imports
        }

        trait List_ extends Bound {
            def x : Bound
            protected def toPython = s"listOf($x)"
            def imports = ImportFrom("listOf", "marketsim") :: x.imports
        }

        trait Tuple extends Bound {
            val elems : List[Bound]
            protected def toPython = elems map { _.toString } map { _ + "," } mkString ("(", "", ")")

            def imports = elems flatMap { _.imports }
        }

        trait Function extends Bound {
            val args : List[Bound]
            val ret : Bound
            protected def toPython = {
                val types = (ret :: args) map { _.toString } mkString ","
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


            protected def toPython =
                builtins.getOrElse(decl.name, decl.name) +
                (if (genericArgs.isEmpty) "" else genericArgs map { _.toString } mkString ("[", ",", "]"))
        }
    }

    trait Expr extends pp.Expr with predef.ScPyPrintable

    trait BinOp extends pp.BinOp[Typed.Expr]
    {
        def wr(x : Expr, rhs : Boolean) =
            pars(x.asCode, need_brackets(x, rhs))
        def imports = x.imports ++ y.imports
        protected def toPython = toScala
        def asCode = "(" ||| wr(x, false) ||| symbol.toString ||| wr(y, true) ||| ")"
    }

    trait Cast extends Printable
    {
        val x : Expr
        protected def toPython = x.toString
        def imports = x.imports
    }

    trait List_ extends Printable
    {
        val xs : List[Expr]
        protected def toPython = xs mkString ("[", ",", "]")
        def imports = xs flatMap { _.imports }
    }

    trait Neg extends pp.Neg[Typed.Expr]
    {
        def imports = x.imports
        protected def toPython = toScala
        def asCode = predef.toLazy("-") ||| x.asCode
    }

    trait IfThenElse extends pp.IfThenElse[Typed.Expr, Typed.Expr]
    {
        def wr(x : Expr) =
            pars(x.asCode, need_brackets(x, false))

        protected def toPython = s"($cond)[${wrap(x)}, ${wrap(y)}]"

        def imports = x.imports ++ y.imports ++ cond.imports

        def asCode =  "(" ||| cond.asCode ||| ")[" ||| wr(x) ||| ", " ||| wr(y) ||| "]"
    }

    trait StringLit extends pp.StringLit
    {
        def imports = Nil
        protected def toPython = toScala

        def asCode : Code = toScala
    }

    trait IntLit extends pp.IntLit
    {
        def imports = Nil
        protected def toPython = toScala

        def asCode : Code = toScala
    }

    trait And extends pp.And[Typed.Expr]
    {
        def imports = x.imports ++ y.imports
        protected def toPython = toScala

        def asCode = x.asCode ||| " and " ||| y.asCode
    }

    trait Or extends pp.Or[Typed.Expr] {
        def imports = x.imports ++ y.imports
        protected def toPython = toScala

        def asCode = x.asCode ||| " or " ||| y.asCode
    }

    trait Not extends pp.Not[Typed.Expr, Typed.Expr] {
        protected def toPython = toScala
        def imports = x.imports
        def asCode = "not " ||| x.asCode
    }

    trait Condition extends pp.Condition[Typed.Expr] {
        protected def toPython = toScala
        def imports = x.imports ++ y.imports

        def asCode = x.asCode ||| symbol.toString ||| y.asCode
    }

    type Priority_0 = pp.Priority_0

    trait FloatLit extends Expr with Priority_0 {
        self: Typed.FloatLit =>
        protected def toPython = x.toString

        def imports = Nil

        def asCode = x.toString
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        protected def toPython = "self." + p.name

        def imports = Nil

        def asCode = "self." + p.name
    }

    trait FunctionRef extends Expr with Priority_0 {
        self: Typed.FunctionRef =>
        protected def toPython = fullImportName(f.qualifiedName)

        def imports = (importsOf(f) as fullImportName(f.qualifiedName)) :: Nil

        def asCode = fullImportName(f.qualifiedName) ||| (importsOf(f) as fullImportName(f.qualifiedName))
    }

    def moduleName(target : Typed.Function) = {
        val name = target.parent.qualifiedName.toString
        "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name
    }

    def fullImportName(n : AST.QualifiedName) =
        n.names mkString "_"

    def importsOf(target : Typed.Function) =
        predef.ImportFrom(target.name, moduleName(target))

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>
        protected def toPython =
            target + arguments.mkString("(",",",")")

        override def imports =
            target.imports ++ (arguments flatMap { _.imports })


        def asCode =
            (target.asCode ||| makeCodeString(arguments map { _.asCode}, "(",",",")")) |||
                Code.from(target.imports ++ (arguments flatMap { _.imports }))
    }

}
