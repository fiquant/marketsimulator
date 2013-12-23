package object TypeInference
{
    def floatRank(e: Typed.Expr) = e.ty match {
        case x if x canCastTo Types.Float_ => 0
        case x if x canCastTo Types.FloatObservable => 10
        case x if x canCastTo Types.FloatFunc => 1
        case t => -1
    }

    def isFloat(e : Typed.Expr) = floatRank(e) >= 0

    private def floatRankStrict(e: Typed.Expr) = floatRank(e) match {
        case -1 => throw new Exception(s"Expression $e is expected to a float-like type")
        case x => x
    }

    private def unifyFloat(xs : Typed.Expr*) =
        (xs map floatRankStrict).sum match {
            case x if x >= 10 => Types.FloatObservable
            case x if x >= 1 => Types.FloatFunc
            case 0 => Types.Float_
        }

    trait Neg {
        self: Typed.Neg =>
        val ty = unifyFloat(x)
    }

    trait BinOp {
        self: Typed.BinOp =>
        val ty = unifyFloat(x,y)
    }

    trait IfThenElse {
        self: Typed.IfThenElse =>
        val ty = {
            if (isFloat(x) && isFloat(y))
                unifyFloat(x,y)
            else {
                if (x.ty canCastTo y.ty) y.ty else
                if (y.ty canCastTo x.ty) x.ty else
                    throw new Exception("Cannot unify if-then-else branches in expression " + self)
            }
        }
    }

    trait FloatConst {
        val ty = Types.Float_
    }

    trait StringLit {
        val ty = Types.String_
    }

    trait ParamRef {
        self: Typed.ParamRef =>
        val ty = p.ty
    }

    trait FunctionCall {
        self: Typed.FunctionCall =>
        val ty = target.ret_type
    }

    def checkBoolean(e : Typed.Expr) = {
        if (e.ty cannotCastTo Types.BooleanFunc)
            throw new Exception(s"Expression $e is supposed to have () => Boolean type")
        e.ty
    }

    trait UnaryBoolean {
        val x : Typed.Expr
        val ty = checkBoolean(x)
    }

    trait BinaryBoolean extends UnaryBoolean {
        val y : Typed.Expr
        override val ty = checkBoolean(x); checkBoolean(y)
    }

    trait Condition {
        self: Typed.Condition =>
        val ty = {
            val t = unifyFloat(x,y)
            if (t != Types.Float_ && (t cannotCastTo Types.FloatFunc))
                throw new Exception(s"Arguments of boolean expression must be casted to () => Float")
            Types.BooleanFunc
        }
    }
}