package syntax.scala

import Types._

class Printer() extends PrettyPrinter.Base {

    def apply(x : Type) = x match {
        case _ : `Float` => "Float"
        case _ : Unit => "()"
        case Tuple(lst) => pars(lst.mkString(","))
        case Function(args, ret) => s"$args => $ret"
    }

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

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
        case AST.Less() => "<"
        case AST.LessEqual() => "<="
        case AST.Greater() => ">"
        case AST.GreaterEqual() => ">="
        case AST.Equal() => "="
        case AST.NotEqual() => "<>"
    }

}
