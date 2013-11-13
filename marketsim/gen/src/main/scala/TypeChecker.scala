case class TypeChecker(lookupFunction : AST.QualifiedName => Typed.Function,
                       lookupVar: String => Typed.Parameter)
{
    private def floatRank(e : AST.Expr) = apply(e).ty match {
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

    def apply(e : AST.BooleanExpr) : Typed.BooleanExpr = e match {
        case AST.And(x, y) => Typed.And(apply(x), apply(y))
        case AST.Or(x, y) => Typed.Or(apply(x), apply(y))
        case AST.Not(x) => Typed.Not(apply(x))
        case AST.Condition(symbol, x, y) =>
            if (unifyFloat(x,y) != Types.FloatFunc)
                throw new Exception(s"Arguments of boolean expression $e must be casted to () => Float")
            Typed.Condition(symbol, apply(x), apply(y))
    }

    def apply(e : AST.Expr) : Typed.Expr = e match {
        case AST.BinOp(c, x, y) =>
            Typed.BinOp(unifyFloat(x, y), c, apply(x), apply(y))

        case AST.Neg(x) => Typed.Neg(unifyFloat(x), apply(x))

        case AST.IfThenElse(cond, x, y) =>
            Typed.IfThenElse(unifyFloat(x, y), apply(cond), apply(x), apply(y))

        case AST.Const(d) => Typed.FloatConst(d)
        case AST.Var(name) => Typed.ParamRef(lookupVar(name))

        case AST.FunCall(name, args) =>
            val fun_type = lookupFunction(name)
            val actual_args = args zip fun_type.parameters map {
                case (actual, declared) =>
                    val typed = apply(actual)
                    if (typed.ty != declared.ty) // TODO: support type casts and conversions
                        throw new Exception(s"Function '$name' is called with wrong argument of"+
                                            s" type '${typed.ty}' when type '${declared.ty}' is expected")
                    (declared, typed)
            }
            Typed.FunctionCall(fun_type, actual_args)
    }
}
