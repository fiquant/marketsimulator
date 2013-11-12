case class TypeChecker(lookupFunction : AST.QualifiedName => Typed.Function,
                       lookupVar: String => Typed.Parameter)
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

    def toTyped(e : AST.Expr) : Typed.Expr = e match {
        case AST.BinOp(c, x, y) => Typed.BinOp(unifyFloat(x, y), c, toTyped(x), toTyped(y))
        case AST.IfThenElse(cond, x, y) => Typed.IfThenElse(unifyFloat(x, y), toTyped(x), toTyped(y))
        case AST.Const(d) => Typed.FloatConst(d)
        case AST.Var(name) => Typed.ParamRef(lookupVar(name))
        case AST.FunCall(name, args) =>
            val fun_type = lookupFunction(name)
            val actual_args = args zip fun_type.params map {
                case (actual, declared) =>
                    val typed = toTyped(actual)
                    if (typed.ty != declared.ty) // TODO: support type casts and conversions
                        throw new Exception(s"Function $name is called with wrong argument $declared: $typed")
                    (declared, typed)
            }
            Typed.FunctionCall(fun_type, actual_args)
    }

    def apply(e : AST.Expr) : Types.Base = e match
    {
        case AST.Const(d) => Types.`Float`
        case AST.Var(name) => lookupVar(name).ty
        case AST.BinOp(_, x, y) => unifyFloat(x, y)
        case AST.Neg(x) => unifyFloat(x)

        case AST.IfThenElse(c, x, y) =>
            ensureBool(c)
            unifyFloat(x, y)

        case AST.FunCall(name, args) =>
            // TODO: type check for the arguments
            val fun_type = lookupFunction(name)
            Types.Function(List(Types.Unit), fun_type.ty)
    }
}
