package object Typed
{
    import AST.BinOpSymbol
    import AST.CondSymbol
    import PrettyPrinter.Printable

    abstract class Expr(val ty : Types.Base) extends Printable

    case class Neg(t: Types.Base, x : Expr) extends Expr(t)
    case class BinOp(t : Types.Base, op : BinOpSymbol, x : Expr, y : Expr) extends Expr(t)
    case class IfThenElse(t : Types.Base, cond : BooleanExpr, x : Expr, y : Expr) extends Expr(t)
    case class FloatConst(x : Double) extends Expr(Types.`Float`)
    case class ParamRef(p : Parameter) extends Expr(p.ty)
    case class FunctionCall(target : Function, arguments : List[(Parameter, Expr)]) extends Expr(Types.nullaryFunction(target.ty))

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr]) extends Printable

    case class Function(name : String, params : List[Parameter], ty : Types.Base, body : Option[Expr]) extends Printable

    class BooleanExpr extends Expr(Types.BooleanFunc)

    case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class Not(x : BooleanExpr) extends BooleanExpr
    case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr
}