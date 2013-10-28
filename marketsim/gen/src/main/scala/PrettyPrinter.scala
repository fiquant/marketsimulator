
object PrettyPrinter {

    def priority(e : Expr) = e match {
        case Const(_) => 0
        case Var(_) => 0
        case Neg(_) => 0
        case FunCall(_, _) => 0

        case BinOp(Mul(), _, _) => 1
        case BinOp(Div(), _, _) => 1

        case BinOp(Add(), _, _) => 2
        case BinOp(Sub(), _, _) => 2

        case IfThenElse(_,_,_) => 3
    }

    def symbol(s : BinOpSymbol) = s match {
        case Mul() => "*"
        case Div() => "/"
        case Add() => "+"
        case Sub() => "-"
    }

    def symbol(s : CondSymbol) = s match {
        case Less() => "<"
        case LessEqual() => "<="
        case Greater() => ">"
        case GreaterEqual() => ">="
        case Equal() => "="
        case NotEqual() => "<>"
    }

    def need_brackets(x : Expr, e : Expr, rhs : Boolean = false) =
        priority(x) > priority(e) || (priority(x) == priority(e) && rhs)

    def wrap(x : Expr, e : Expr, rhs : Boolean = false) =
        if (need_brackets(x,e,rhs)) s"(${apply(x)})" else apply(x)

    def apply(e : Expr) : String = e match {
        case Const(x) => x.toString
        case Var(x) => x
        case Neg(x) => s"-${wrap(x, e)}"
        case BinOp(s, x,y) => s"${wrap(x, e)} ${symbol(s)} ${wrap(y, e, true)}"
        case IfThenElse(_,x,y) => s"if xxx then ${wrap(x, e)} else ${wrap(y, e)}"
        case FunCall(name, args) => s"$name($args)"
    }

}
