package syntax.scala

class Printer() extends PrettyPrinter.Base {

    val crlf = "\r\n"

    def apply(x : Types.Base) = x match {
        case Types.`Float` => "Float"
        case Types.`Boolean` => "Boolean"
        case Types.Unit => "()"
        case Types.Tuple(lst) => pars(lst.mkString(","))
        case Types.Function(args, ret) =>
            (if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
    }

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

    def apply(x : AST.Type) = x match {
        case AST.SimpleType(x) => x
        case AST.UnitType => "()"
        case AST.TupleType(lst) => pars(lst.mkString(","))
        case AST.FunctionType(args, ret) => s"$args => $ret"
    }

    def apply(e : AST.BooleanExpr) = e match {
        case AST.Or(x, y) => x + " or " + y
        case AST.And(x, y) =>
            def wrap(z : AST.BooleanExpr) = pars(z, z.isInstanceOf[AST.Or])
            wrap(x) + " and " + wrap(y)
        case AST.Not(x) =>
            def wrap(z : AST.BooleanExpr) = pars(z, !z.isInstanceOf[AST.Condition])
            "not " + wrap(x)
        case AST.Condition(c, x, y) => x.toString + c + y
    }

    def apply(c : AST.CondSymbol) = c match {
        case AST.Less => "<"
        case AST.LessEqual => "<="
        case AST.Greater => ">"
        case AST.GreaterEqual => ">="
        case AST.Equal => "="
        case AST.NotEqual => "<>"
    }

    def priority(e : AST.Expr) = e match {
        case _ : AST.Const => 0
        case _ : AST.Var => 0
        case _ : AST.Neg => 0
        case _ : AST.FunCall => 0
        case AST.BinOp(AST.Mul, _, _) => 1
        case AST.BinOp(AST.Div, _, _) => 1
        case AST.BinOp(AST.Add, _, _) => 2
        case AST.BinOp(AST.Sub, _, _) => 2
        case _ : AST.IfThenElse => 3
    }

    def priority(e : Typed.Expr) = e match {
        case _ : Typed.FloatConst => 0
        case _ : Typed.ParamRef => 0
        case _ : Typed.Neg => 0
        case _ : Typed.FunctionCall => 0
        case Typed.BinOp(_,AST.Mul, _, _) => 1
        case Typed.BinOp(_,AST.Div, _, _) => 1
        case Typed.BinOp(_,AST.Add, _, _) => 2
        case Typed.BinOp(_,AST.Sub, _, _) => 2
        case _ : Typed.IfThenElse => 3
    }

    def need_brackets(x : AST.Expr, e : AST.Expr, rhs : Boolean) =
        priority(x) > priority(e) || priority(x) == priority(e) && rhs

    def need_brackets(x : Typed.Expr, e : Typed.Expr, rhs : Boolean) =
        priority(x) > priority(e) || priority(x) == priority(e) && rhs

    def wrap(x : AST.Expr, e : AST.Expr, rhs : Boolean) =
        pars(x, need_brackets(x, e, rhs))

    def wrap(x : Typed.Expr, e : Typed.Expr, rhs : Boolean) =
        pars(x, need_brackets(x, e, rhs))

    def wrap(x : AST.Expr, e : AST.Expr) : String = wrap(x, e, rhs = false)
    def wrap(x : Typed.Expr, e : Typed.Expr) : String = wrap(x, e, rhs = false)

    def apply(e : AST.Expr) = e match {
        case AST.BinOp(symbol, x, y) => wrap(x, e) + symbol + wrap(y, e, rhs = true)
        case AST.Neg(x) => "-" + wrap(x, e)
        case AST.IfThenElse(cond, x, y) => s"if $cond then ${wrap(x,e)} else ${wrap(y,e)}"
        case AST.FunCall(name, args) => name + pars(args.mkString(","))
        case AST.Const(x) => x.toString
        case AST.Var(s) => s
    }

    def apply(e : Typed.Expr) = e match {
        case Typed.BinOp(_, symbol, x, y) => wrap(x, e) + symbol + wrap(y, e, rhs = true)
        case Typed.Neg(_, x) => "-" + wrap(x, e)
        case Typed.IfThenElse(_, cond, x, y) => s"if $cond then ${wrap(x,e)} else ${wrap(y,e)}"
        case Typed.FunctionCall(name, args) => name + pars(args.mkString(","))
        case Typed.FloatConst(x) => x.toString
        case Typed.ParamRef(s) => s.name
    }

    def apply(s : AST.BinOpSymbol) = s match {
        case AST.Add => "+"
        case AST.Sub => "-"
        case AST.Mul => "*"
        case AST.Div => "/"
    }

    def prefixedIfSome[A](p : Option[A], prefix : String = "") =
        if (p.nonEmpty) prefix + p.get else ""

    def apply(p : AST.Parameter) =
    {
        import p._
        (annotations.map({ _ + " "}).mkString("")
            + name
            + prefixedIfSome(ty, " : ")
            + prefixedIfSome(initializer, " = "))
    }

    def apply(p : Typed.Parameter) =
    {
        import p._
        (name
         + " : " + ty
         + prefixedIfSome(initializer, " = "))
    }

    def apply(p : AST.QualifiedName) = p.names.mkString(".")

    def apply(p : AST.Annotation) =
        "@" + p.name + "(" + p.parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"

    def apply(p : AST.DocString) =
        ("/** " + p.brief
                + p.detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf
                + " */" + crlf)


    def apply(p : AST.FunDef) = {
        import p._
        (prefixedIfSome(docstring)
                + annotations.map({_ + crlf}).mkString("")
                + "def " + name
                + "(" + parameters.mkString(", ") + ")"
                + prefixedIfSome(ret_type, " : ")
                + prefixedIfSome(body, " = "))
    }

    def apply(p : Typed.Function) = {
        import p._
        (crlf + "def " + name
                + params.mkString("(", ",", ")")
                + " : " + ty //+ crlf + "\t"
                )

    }

    def apply(p : AST.Definitions) = p.definitions.map({_ + crlf + crlf}).mkString("")

    def apply(p : Typed.BooleanExpr) = ""
}
