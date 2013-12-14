case class TypeChecker(ctx : TypingExprCtx)
{
    def asBoolean(e : AST.BooleanExpr) : Typed.BooleanExpr = e match {
        case AST.And(x, y) => Typed.And(asBoolean(x), asBoolean(y))
        case AST.Or(x, y) => Typed.Or(asBoolean(x), asBoolean(y))
        case AST.Not(x) => Typed.Not(asBoolean(x))
        case AST.Condition(symbol, x, y) =>
            promote_opt(Typed.Condition(symbol, asArith(x), asArith(y)))
    }

    def promote_literal(e : Typed.ArithExpr) =
        e match {
            case Typed.FloatConst(d) =>
                val f = ctx.lookupFunction(AST.QualifiedName("const" :: Nil))
                val r = Typed.FunctionCall(f, (f.parameters(0), e) :: Nil)
                r
            case x => x
        }

    def promote_opt(e : Typed.ArithExpr) =
        if (e.ty canCastTo Types.FloatFunc) e match {
            case Typed.BinOp(c, x, y) => Typed.BinOp(c, promote_literal(x), promote_literal(y))
            case Typed.IfThenElseArith(cond, x, y) => Typed.IfThenElseArith(cond, promote_literal(x), promote_literal(y))
            case x => x
        } else e

    def promote_opt(e : Typed.BooleanExpr) = e match {
            case Typed.Condition(symbol, x, y) => Typed.Condition(symbol, promote_literal(x), promote_literal(y))
            case x => x
        }


    def asArith(e : AST.Expr) : Typed.ArithExpr = e match {
        case AST.BinOp(c, x, y) =>
            promote_opt(Typed.BinOp(c, asArith(x), asArith(y)))

        case AST.Neg(x) => Typed.Neg(asArith(x))

        case AST.IfThenElse(cond, x, y) =>
            promote_opt(Typed.IfThenElseArith(asBoolean(cond), asArith(x), asArith(y)))

        case AST.Const(d) => Typed.FloatConst(d)
        case AST.Var(name) => Typed.ParamRef(ctx.lookupVar(name))

        case AST.FunCall(name, args) =>
            val fun_type = ctx.lookupFunction(name)
            val actual_args = args zip fun_type.parameters map {
                case (actual, declared) =>
                    val typed = asArith(actual)
                    if (typed.ty cannotCastTo declared.ty)
                        throw new Exception(s"Function '$name' is called with wrong argument of"+
                                            s" type '${typed.ty}' when type '${declared.ty}' is expected")
                    (declared, typed)
            }
            Typed.FunctionCall(fun_type, actual_args)
    }


}




trait TypingExprCtx
{
    def lookupFunction(name : AST.QualifiedName) : Typed.Function
    def lookupVar(name : String) : Typed.Parameter
}
