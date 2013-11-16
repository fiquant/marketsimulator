case class TypeChecker(lookupFunction : AST.QualifiedName => Typed.Function,
                       lookupVar: String => Typed.Parameter)
{
    def apply(e : AST.BooleanExpr) : Typed.BooleanExpr = e match {
        case AST.And(x, y) => Typed.And(apply(x), apply(y))
        case AST.Or(x, y) => Typed.Or(apply(x), apply(y))
        case AST.Not(x) => Typed.Not(apply(x))
        case AST.Condition(symbol, x, y) =>
            Typed.Condition(symbol, apply(x), apply(y))
    }

    def apply(e : AST.Expr) : Typed.ArithExpr = e match {
        case AST.BinOp(c, x, y) =>
            Typed.BinOp(c, apply(x), apply(y))

        case AST.Neg(x) => Typed.Neg(apply(x))

        case AST.IfThenElse(cond, x, y) =>
            Typed.IfThenElse(apply(cond), apply(x), apply(y))

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
