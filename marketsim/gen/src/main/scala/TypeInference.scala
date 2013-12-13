package object TypeInference
{
    private def floatRank(e: Typed.Expr) = e.ty match {
        case x if x canCastTo Types.`Float` => 0
        case x if x canCastTo Types.FloatObservable => 10
        case x if x canCastTo Types.FloatFunc => 1
        case t => throw new Exception(s"has wrong type $t")
    }

    private def unifyFloat(xs : Typed.Expr*) =
        (xs map floatRank).sum match {
            case x if x >= 10 => Types.FloatObservable
            case x if x >= 1 => Types.FloatFunc
            case 0 => Types.`Float`
        }

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
            val t = unifyFloat(x,y)
            if (t != Types.Float && (t cannotCastTo Types.FloatFunc))
                throw new Exception(s"Arguments of boolean expression must be casted to () => Float")
            Types.BooleanFunc
        }
    }
}