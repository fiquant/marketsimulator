/**
object PrettyPrinter {

    def priority(e : Expr) = e match {
        case Const(_) => 0
        case Var(_) => 0
        case Neg(_) => 0
        case FunCall(_, _) => 0

        case Mul(_,_) => 1
        case Div(_,_) => 1

        case Add(_,_) => 2
        case Sub(_,_) => 2

        case IfThenElse(_,_,_) => 3
    }

    def apply(e : Expr) : String = e match {
        case Const(x) => x.toString
        case Var(x) => x
        case Neg(x) => s"-(${apply(x)})"
        case Add(x,y) => s"(${apply(x)}) + (${apply(y)})"
        case Sub(x,y) => s"(${apply(x)}) - (${apply(y)})"
    }

}
*/