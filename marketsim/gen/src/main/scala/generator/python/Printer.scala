package generator.python
import predef._

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}
    import predef.{Code, Combine, ImportFrom}

    trait Printable
    {
        def asCode : Code
    }

    object types {

        type Printable = Printer.Printable

        trait Unit extends Printable {
            def asCode : Code =
                throw new Exception("Unit types are not supported yet for python generation")
        }

        trait Nothing extends Printable {
            def asCode : Code =
                throw new Exception("Nothing types are not supported for python generation")
        }

        trait Any_ extends Printable {
            def asCode : Code = "object"
        }

        trait Optional extends Printable {
            def x : Printable
            def asCode = x.asCode
        }

        trait List_ extends Printable {
            def x : Printable
            def asCode = s"listOf("||| x.asCode |||")" |||  ImportFrom("listOf", "marketsim")
        }

        trait Tuple extends Printable {
            val elems : List[Printable]

            def asCode = "(" ||| Code.from(elems map { _.asCode ||| "," }, "") ||| ")"
        }

        trait Function extends Printable {
            val args : List[Printable]
            val ret : Printable

            def asCode = {
                val x = "IFunction" ||| ret.asCode ||| Code.from(args map { _.asCode  })

                val m = mangle(x.toString)

                m ||| ImportFrom(m.toString, "marketsim.gen._out._ifunction._" + m.toLowerCase)
            }

        }

        trait ImplementationClass extends Printable
        {
            self : TypesBound.ImplementationClass =>

            def asCode = name |||
                        ImportFrom(name, s"marketsim.gen._intrinsic.$module")
        }

        trait UsedDefined extends Printable
        {
            def genericArgs : List[Printable]
            def decl : Typed.TypeDeclaration

            val builtins = Map("Float"  -> "float",
                               "Int"    -> "int",
                               "Boolean"-> "bool",
                               "String" -> "str")

            def asCode = {

                def impl(xs : List[Printable]) : Code = xs match {
                    case Nil => stop
                    case x :: Nil => x.asCode
                    case x :: y => x.asCode ||| impl(y)
                }

                builtins get decl.name match {
                    case Some(x) => x
                    case None =>
                        val x = decl.name |||
                                (if (genericArgs.isEmpty) stop else impl(genericArgs))

                        val m = mangle(x.toString) ||| Code.from(x.imports.toList)

                        m ||| ImportFrom(m.toString, moduleName(decl, m.toString))
                }
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
        def asCode = qualifiedCall(f)
    }

    def qualifiedCall(f : Typed.Function) =
        fullImportName(f) ||| (importsOf(f) as fullImportName(f))

    def parametersMangled(parameters : List[Typed.Parameter]) =
        typesMangled(parameters map { _.ty })

    def mangle(p : String) =
        "[].()=> ,".toList.foldLeft(p) { case (z, s) => z.replace(s.toString, "") }.replace("Optional", "").replace("\n","").replace("\r","")

    def typesMangled(ts : List[Any]) =
        ts map { a => mangle(a.toString) }  mkString ""

    def decoratedName(f : Typed.Function) =
        f.name + "_" + parametersMangled(f.parameters)


    def moduleName(target : Typed.FunctionDecl) = {
        val name = target.parent.qualifiedName.toString
        "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name.toLowerCase
    }

    def moduleName(target : Typed.TypeDeclaration, nameToImport : String) = {
        val name = target.parent.qualifiedName.toString
        if (nameToImport == target.name)
            "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name.toLowerCase
        else
            "marketsim.gen._out" + name.splitAt(0)._2 + "._" + target.name.toLowerCase + "._" + nameToImport.toLowerCase
    }

    def fullImportName(f : Typed.Function) =
        (f.qualifiedName mkString "_") + "_" + parametersMangled(f.parameters)

    def importsOf(target : Typed.Function) =
        predef.ImportFrom(decoratedName(target), moduleName(target))

    def pubImportsOf(target : Typed.FunctionDecl) =
        predef.ImportFrom(target.name, moduleName(target))

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>

        def asCode =
            target.asCode ||| makeCodeString(arguments map { _.asCode}, "(",",",")")
    }

}
