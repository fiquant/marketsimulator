package object TypeChecker
{
    def infer(e : AST.Expr, g : TypeTable.Impl, locals : Map[String, Types.Base]) : Types.Base = e match
    {
        case AST.Const(d) => Types.`Float`
        case AST.Var(name) => locals.get(name) match {
            case Some(t) => t
            case None => throw new Exception(s"cannot find type for variable $name")
        }
        case AST.BinOp(_, x, y) =>
            val xt = infer(x, g, locals)
            val yt = infer(y, g, locals)
            (xt, yt) match {
                case (Types.`Float`, Types.`Float`) => Types.`Float`
            }
    }
}
