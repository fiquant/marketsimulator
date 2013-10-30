
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

    val crlf = "\r\n"

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

    def wrap_if_needed(x : Expr, e : Expr, rhs : Boolean = false) =
        if (need_brackets(x,e,rhs)) parens(apply(x)) else apply(x)

    def apply(x : QualifiedName) : String = x.names.mkString(".")

    def apply(e : Expr) : String = e match {
        case Const(x) => x.toString
        case Var(x) => x
        case Neg(x) => "-" + wrap_if_needed(x, e)
        case BinOp(s, x,y) => wrap_if_needed(x, e) + apply(s) + wrap_if_needed(y, e, rhs = true)
        case IfThenElse(c,x,y) => s"if ${apply(c)} then ${wrap_if_needed(x, e)} else ${wrap_if_needed(y, e)}"
        case FunCall(name, args) => apply(name) + parens(args.map(apply).mkString(","))
    }

    def parens(x : String) = "(" + x + ")"

    def wrap_if_needed(x : BooleanExpr, e : And) = x match {
        case y : Or => "(" + apply(y) + ")"
        case y => apply(y)
    }

    def wrap_if_needed(x : BooleanExpr, e : Not) = x match {
        case Condition(_,_,_) => apply(x)
        case _ => parens(apply(x))
    }

    def apply(e : BooleanExpr) : String = e match {
        case Condition(s, x, y) => apply(x) + apply(s) + apply(y)
        case Or(x, y) => apply(x) + " or " + apply(y)
        case a @ And(x, y) => wrap_if_needed(x, a) + " and " + wrap_if_needed(y, a)
        case a @ Not(x) =>  "not " +  wrap_if_needed(x, a)
    }

    def apply(x : Annotation) : String = "@" + apply(x.name) + parens(x.parameters.mkString(" "))

    def apply(x : Parameter) : String = x.annotations.map(apply).mkString(" ") + s" ${x.name} : ${x.ty}"

    def apply(x : FunDef) : String = x.annotations.map(apply).mkString(crlf) + x.name + parens(x.parameters.map(apply).mkString(","))

    def apply(x : List[FunDef]) : String = x.map(apply).mkString(crlf)
}
