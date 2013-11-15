package syntax.scala

package object Printer
{
    val crlf = "\r\n"
    val tab = "\t"
    
    trait Printable {
        def toScala : String
    }

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

    def prefixedIfSome[A](p : Option[A], prefix : String = "") =
        if (p.nonEmpty) prefix + p.get else ""

    object ast {

        trait Definitions extends Printable {
            self: AST.Definitions =>
            def toScala = definitions.map({_ + crlf + crlf}).mkString("")
        }
        trait Function extends Printable {
            self: AST.FunDef =>
            def toScala =
                (prefixedIfSome(docstring)
                        + annotations.map({_ + crlf}).mkString("")
                        + "def " + name
                        + "(" + parameters.mkString(", ") + ")"
                        + prefixedIfSome(ret_type, " : ")
                        + prefixedIfSome(body, " = "))
        }

        trait DocString extends Printable {
            self: AST.DocString =>
            def toScala =
                ("/** " + brief
                        + detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf
                        + " */" + crlf)

        }

        trait Annotation extends Printable {
            self: AST.Annotation =>
            def toScala =
                "@" + name + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
        }

        trait QualifiedName extends Printable {
            self: AST.QualifiedName =>
            def toScala = names.mkString(".")
        }

        trait Parameter extends Printable {
            self: AST.Parameter =>
            def toScala =
                (annotations.map({ _ + " "}).mkString("")
                        + name
                        + prefixedIfSome(ty, " : ")
                        + prefixedIfSome(initializer, " = "))
        }

        trait BinOpSymbol extends Printable {
            val priority : Int
        }

        trait Add extends BinOpSymbol {
            def toScala = "+"
            val priority = 2
        }
        trait Sub extends BinOpSymbol {
            def toScala = "-"
            val priority = 2
        }
        trait Mul extends BinOpSymbol {
            def toScala = "*"
            val priority = 1
        }
        trait Div extends BinOpSymbol {
            def toScala = "/"
            val priority = 1
        }

        trait Expr extends Printable {
            val priority : Int

            def wrap(x : Expr, rhs : Boolean = false) =
                pars(x, need_brackets(x, rhs))

            def need_brackets(x : Expr, rhs : Boolean) =
                x.priority > priority || x.priority == priority && rhs
        }

        trait Const extends Expr {
            self: AST.Const =>
            def toScala = value.toString
            val priority = 0
        }

        trait Var extends Expr {
            self: AST.Var =>
            def toScala = s
            val priority = 0
        }

        trait FunCall extends Expr {
            self: AST.FunCall =>
            def toScala = name + pars(args.mkString(","))
            val priority = 0
        }

        trait BinOp extends Expr {
            self: AST.BinOp =>
            def toScala = wrap(x) + symbol + wrap(y, rhs = true)
            val priority = symbol.priority
        }

        trait Neg extends Expr {
            self: AST.Neg =>
            def toScala = "-" + wrap(x)
            val priority = 0
        }

        trait IfThenElse extends Expr {
            self: AST.IfThenElse =>
            def toScala = s"if $cond then ${wrap(x)} else ${wrap(y)}"
            val priority = 3
        }

        trait Or extends Printable {
            self: AST.Or =>
            def toScala = s"$x or $y"
        }

        trait And extends Printable {
            self: AST.And =>
            def wrap(z : AST.BooleanExpr) = pars(z, z.isInstanceOf[AST.Or])
            def toScala = wrap(x) + " and " + wrap(y)
        }

        trait Not extends Printable {
            self: AST.Not =>
            def wrap(z : AST.BooleanExpr) = pars(z, !z.isInstanceOf[AST.Condition])
            def toScala = "not " + wrap(x)
        }

        trait Condition extends Printable {
            self: AST.Condition =>
            def toScala = x.toString + symbol + y
        }

        trait Less extends Printable {
            def toScala = "<"
        }
        trait LessEqual extends Printable {
            def toScala = "<="
        }
        trait Greater extends Printable {
            def toScala = ">"
        }
        trait GreaterEqual extends Printable {
            def toScala = ">="
        }
        trait Equal extends Printable {
            def toScala = "="
        }
        trait NotEqual extends Printable {
            def toScala = "<>"
        }

        trait SimpleType extends Printable {
            self: AST.SimpleType =>
            def toScala = name
        }

        trait UnitType extends Printable {
            def toScala = "()"
        }

        trait TupleType extends Printable {
            self: AST.TupleType =>
            def toScala = pars(types.mkString(","))
        }

        trait FunctionType extends Printable {
            self: AST.FunctionType =>
            def toScala = s"$arg_type => $ret_type"
        }
    }

    object types {

        trait Unit extends ast.UnitType

        trait `Float` extends Printable {
            def toScala = "Float"
        }

        trait `Boolean` extends Printable {
            def toScala = "Boolean"
        }

        trait Tuple extends Printable {
            self: Types.Tuple =>
            def toScala = pars(elems.mkString(","))
        }

        trait Function extends Printable {
            self: Types.Function =>
            def toScala = (if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
        }
    }

    object typed {

        trait Parameter extends Printable {
            self: Typed.Parameter =>

            def toScala =
                (name
                    + " : " + ty
                    + prefixedIfSome(initializer, " = "))

        }

        trait Annotation extends Printable {
            self: Typed.Annotation =>

            def toScala = "@" + target.name + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
        }

        trait Function extends Printable {
            self: Typed.Function =>

            def toScala =
                (crlf + prefixedIfSome(docstring)
                        + annotations.map({_ + crlf}).mkString("")
                        + "def " + name
                        + parameters.mkString("(", ", ", ")")
                        + " : " + ret_type
                        + prefixedIfSome(body, crlf + tab + " = ")
                        )
        }

        trait Or extends Printable {
            self: Typed.Or =>
            def toScala = s"$x or $y"
        }

        trait And extends Printable {
            self: Typed.And =>
            def wrap(z : Typed.BooleanExpr) = pars(z, z.isInstanceOf[Typed.Or])
            def toScala = wrap(x) + " and " + wrap(y)
        }

        trait Not extends Printable {
            self: Typed.Not =>
            def wrap(z : Typed.BooleanExpr) = pars(z, !z.isInstanceOf[Typed.Condition])
            def toScala = "not " + wrap(x)
        }

        trait Condition extends Printable {
            self: Typed.Condition =>
            def toScala = x.toString + symbol + y
        }

        type Expr = ast.Expr

        trait BinOp extends Expr {
            self: Typed.BinOp =>
            def toScala = wrap(x) + op + wrap(y, rhs = true)
            val priority = op.priority
        }

        trait Neg extends Expr {
            self: Typed.Neg =>
            def toScala = "-" + wrap(x)
            val priority = 0
        }

        trait IfThenElse extends Expr {
            self: Typed.IfThenElse =>
            def toScala = s"if $cond then ${wrap(x)} else ${wrap(y)}"
            val priority = 3
        }

        trait FloatConst extends Expr {
            self: Typed.FloatConst =>
            def toScala = x.toString
            val priority = 0
        }

        trait ParamRef extends Expr {
            self: Typed.ParamRef =>
            def toScala = p.name
            val priority = 0
        }

        trait FunCall extends Expr {
            self: Typed.FunctionCall =>
            def toScala = target.name + arguments.map({ _._2 }).mkString("(",",",")")
            val priority = 0
        }
    }
}

