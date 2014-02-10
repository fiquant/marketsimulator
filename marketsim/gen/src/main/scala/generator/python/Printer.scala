package generator.python
import predef._

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}
    import predef.{Code, Combine, ImportFrom}

    trait Printable

    object types {

        trait Bound extends Printable
        {
            def asCode : Code
        }

        trait Unit extends Bound {
            def asCode : Code =
                throw new Exception("Unit types are not supported yet for python generation")
        }

        trait Nothing extends Bound {
            def asCode : Code =
                throw new Exception("Nothing types are not supported for python generation")
        }

        trait Any_ extends Bound {
            def asCode : Code = "object"
        }

        trait Optional extends Bound {
            def x : Bound
            def asCode = x.asCode
        }

        trait List_ extends Bound {
            def x : Bound
            def asCode = s"listOf("||| x.asCode |||")" |||  ImportFrom("listOf", "marketsim")
        }

        trait Tuple extends Bound {
            val elems : List[Bound]

            def asCode = "(" ||| Code.from(elems map { _.asCode ||| "," }) ||| ")"
        }

        trait Function extends Bound {
            val args : List[Bound]
            val ret : Bound

            def asCode =
                "IFunction[" ||| ret.asCode ||| Code.from(args map { "," ||| _.asCode  }) ||| "]" ||| ImportFrom("IFunction", "marketsim")
        }

        trait UsedDefined extends st.UsedDefined with Printable with Bound
        {
            self: TypesBound.UserDefined =>

            val builtins = Map("Float"  -> "float",
                               "Int"    -> "int",
                               "Boolean"-> "bool",
                               "String" -> "str")

            def asCode = {
                def impl(xs : List[Bound]) : Code = xs match {
                    case Nil => stop
                    case x :: Nil => x.asCode
                    case x :: y => x.asCode ||| "," ||| impl(y)
                }
                val name = builtins.getOrElse(decl.name, decl.name)
                name ||| ImportFrom(name, "marketsim") |||
                (if (genericArgs.isEmpty) stop else "[" ||| impl(genericArgs) ||| "]")
            }
        }
    }

    trait Expr extends pp.Expr with predef.ScPyPrintable

    trait BinOp extends pp.BinOp[Typed.Expr]
    {
        def wr(x : Expr, rhs : Boolean) =
            pars(x.asCode, need_brackets(x, rhs))
        def asCode = "(" ||| wr(x, false) ||| symbol.toString ||| wr(y, true) ||| ")"
    }

    trait Cast extends Printable
    {
        val x : Expr

        def asCode = x.asCode
    }

    trait List_ extends Printable
    {
        val xs : List[Expr]

        def asCode = {
            def impl(lst : List[Expr]) : Code = lst match {
                case Nil => stop
                case x :: Nil => x.asCode
                case x :: y => x.asCode ||| "," ||| impl(y)
            }
            "[" ||| impl(xs) ||| "]"
        }
    }

    trait Neg extends pp.Neg[Typed.Expr]
    {
        def asCode = predef.toLazy("-") ||| x.asCode
    }

    trait IfThenElse extends pp.IfThenElse[Typed.Expr, Typed.Expr]
    {
        def wr(x : Expr) =
            pars(x.asCode, need_brackets(x, false))

        def asCode =  "(" ||| cond.asCode ||| ")[" ||| wr(x) ||| ", " ||| wr(y) ||| "]"
    }

    trait StringLit extends pp.StringLit
    {
        def asCode : Code = toScala
    }

    trait IntLit extends pp.IntLit
    {
        def asCode : Code = toScala
    }

    trait And extends pp.And[Typed.Expr]
    {
        def asCode = x.asCode ||| " and " ||| y.asCode
    }

    trait Or extends pp.Or[Typed.Expr] {
        def asCode = x.asCode ||| " or " ||| y.asCode
    }

    trait Not extends pp.Not[Typed.Expr, Typed.Expr] {
        def asCode = "not " ||| x.asCode
    }

    trait Condition extends pp.Condition[Typed.Expr] {
        def asCode = x.asCode ||| symbol.toString ||| y.asCode
    }

    type Priority_0 = pp.Priority_0

    trait FloatLit extends Expr with Priority_0 {
        self: Typed.FloatLit =>
        def asCode = x.toString
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        def asCode = "self." + p.name
    }

    trait FunctionRef extends Expr with Priority_0 {
        self: Typed.FunctionRef =>
        def asCode = fullImportName(f.qualifiedName) ||| (importsOf(f) as fullImportName(f.qualifiedName))
    }

    def decoratedName(f : Typed.Function) =
        f.name + "_" +
                (f.parameters map { p =>
                    "[].()=> ,".toList.foldLeft(p.ty.toString){case (z, s) => z.replace(s.toString, "")}.replace("Optional","")
                } mkString "")


    def moduleName(target : Typed.Function) = {
        val name = target.parent.qualifiedName.toString
        "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name.toLowerCase
    }

    def fullImportName(n : AST.QualifiedName) =
        n.names mkString "_"

    def importsOf(target : Typed.Function) =
        predef.ImportFrom(target.name, moduleName(target))

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>

        def asCode =
            target.asCode ||| makeCodeString(arguments map { _.asCode}, "(",",",")")
    }

}
