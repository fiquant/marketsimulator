
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

    def apply(s : BinOpSymbol) = s match {
        case Mul() => "*"
        case Div() => "/"
        case Add() => "+"
        case Sub() => "-"
    }

    def apply(s : CondSymbol) = s match {
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

    def apply[T](x : T) : String = x match {
        case s : String => s
        case e : Expr => apply(e)
    }


    def apply[T](lst : List[T], sep : String = ",") : String = lst match {
        case Nil => ""
        case hd :: Nil => s"${apply(hd)}"
        case hd :: tl => s"${apply(hd)}$sep${apply(tl, sep)}"
    }

    def apply(e : Expr) : String = e match {
        case Const(x) => x.toString
        case Var(x) => x
        case Neg(x) => s"-${wrap(x, e)}"
        case BinOp(s, x,y) => s"${wrap(x, e)}${apply(s)}${wrap(y, e, true)}"
        case IfThenElse(c,x,y) => s"if ${apply(c)} then ${wrap(x, e)} else ${wrap(y, e)}"
        case FunCall(name, args) => s"${apply(name.names, ".")}(${apply(args, ",")})"
    }

    def wrap(x : BooleanExpr, e : And) = x match {
        case y : Or => s"(${apply(y)})"
        case y => apply(y)
    }

    def wrap(x : BooleanExpr, e : Not) = x match {
        case Condition(_,_,_) => apply(x)
        case _ => s"(${apply(x)})"
    }


    def apply(e : BooleanExpr) : String = e match {
        case Condition(s, x, y) => s"${apply(x)}${apply(s)}${apply(y)}"
        case Or(x, y) => s"${apply(x)} or ${apply(y)}"
        case a @ And(x, y) => s"${wrap(x, a)} and ${wrap(y, a)}"
        case a @ Not(x) =>  s"not ${wrap(x, a)}"
    }

}
