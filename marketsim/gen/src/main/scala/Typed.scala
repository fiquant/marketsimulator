package object Typed
{
    abstract class Expr(val ty : Types.Base)

    import AST.BinOpSymbol
    import AST.CondSymbol

    case class Neg(t: Types.Base, x : Expr) extends Expr(t)
    case class BinOp(t : Types.Base, op : BinOpSymbol, x : Expr, y : Expr) extends Expr(t)
    case class IfThenElse(t : Types.Base, cond : BooleanExpr, x : Expr, y : Expr) extends Expr(t)
    case class FloatConst(x : Double) extends Expr(Types.`Float`)
    case class ParamRef(p : Parameter) extends Expr(p.ty)
    case class FunctionCall(target : Function, arguments : List[(Parameter, Expr)]) extends Expr(target.ty)

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr])

    case class Function(name : String, params : List[Parameter], ty : Types.Base)

    class BooleanExpr extends Expr(Types.BooleanFunc)

    case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class Not(x : BooleanExpr) extends BooleanExpr
    case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr
}