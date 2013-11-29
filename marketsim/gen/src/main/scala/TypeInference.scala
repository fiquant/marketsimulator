package object TypeInference
{
    private def floatRank(e: Typed.Expr) = e.ty match {
        case Types.`Float` => 0
        case Types.FloatFunc => 1
        case t => throw new Exception(s"has wrong type $t")
    }

    private def unifyFloat(xs : Typed.Expr*) =
        if ((xs map floatRank).sum > 0) Types.FloatFunc else Types.`Float`

    trait Neg {
        self: Typed.Neg =>
        def ty = unifyFloat(x)
    }

    trait BinOp {
        self: Typed.BinOp =>
        def ty = unifyFloat(x,y)
    }

    trait IfThenElse {
        self: Typed.IfThenElse =>
        def ty = unifyFloat(x,y)
    }

    trait FloatConst {
        def ty = Types.`Float`
    }

    trait ParamRef {
        self: Typed.ParamRef =>
        def ty = p.ty
    }

    trait FunctionCall {
        self: Typed.FunctionCall =>
        def ty = target.ret_type
    }

    trait BooleanExpr {
        val ty = Types.BooleanFunc
    }

    trait Condition extends BooleanExpr {
        self: Typed.Condition =>
        override val ty = {
            if (unifyFloat(x,y) != Types.FloatFunc)
                throw new Exception(s"Arguments of boolean expression must be casted to () => Float")
            Types.BooleanFunc
        }
    }
}