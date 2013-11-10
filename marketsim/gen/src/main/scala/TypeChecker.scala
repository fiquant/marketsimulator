class TypeChecker(globals : TypeTable.Impl, locals : Map[String, Types.Base])
{
    private def floatRank(e : AST.Expr) = apply(e) match {
        case Types.`Float` => 0
        case Types.FloatFunc => 1
        case t => throw new Exception(s"operand $e has wrong type $t")
    }

    private def unifyFloat(xs : AST.Expr*) =
        if ((xs map floatRank).sum > 0) Types.FloatFunc else Types.`Float`

    private def ensureBool(e : AST.BooleanExpr) : Unit = e match {
        case AST.Or(x, y) => ensureBool(x); ensureBool(y)
        case AST.And(x, y) => ensureBool(x); ensureBool(y)
        case AST.Not(x) => ensureBool(x)
        case AST.Condition(_, x, y) => unifyFloat(x, y)
    }

    def apply(e : AST.Expr) : Types.Base = e match
    {
        case AST.Const(d) => Types.`Float`
        case AST.Var(name) => locals.get(name) match {
            case Some(t) => t
            case None => throw new Exception(s"cannot find type for variable $name")
        }
        case AST.BinOp(_, x, y) => unifyFloat(x, y)
        case AST.Neg(x) => unifyFloat(x)

        case AST.IfThenElse(c, x, y) =>
            ensureBool(c)
            unifyFloat(x, y)

        case AST.FunCall(name, args) =>
            // TODO: type check for the arguments
            globals.lookup(name)
    }
}
