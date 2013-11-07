package object AST {

    val crlf = "\r\n"

    abstract class Type

    case class SimpleType(name : String) extends Type
    case class UnitType() extends Type
    case class TupleType(types : List[Type]) extends Type
    {
        assert(types.length > 1) // SimpleType or UnitType should be used in this case
        // we don't want to differentiate 1-tuple and SimpleType
    }

    case class FunctionType(arg_type : Type, ret_type : Type) extends Type

    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         annotations : List[Annotation])

    case class QualifiedName(names   : List[String])

    case class Annotation(name       : QualifiedName,
                          parameters : List[String])

    case class DocString(brief : String, detailed : String)

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation])

    case class Definitions(definitions : List[FunDef])

    abstract class BinOpSymbol(p : Int) {
        val priority = p
    }
    case class Add() extends BinOpSymbol(2)
    case class Sub() extends BinOpSymbol(2)
    case class Mul() extends BinOpSymbol(1)
    case class Div() extends BinOpSymbol(1)

    abstract class Expr(p : Int) {
        val priority  = p
    }

    case class Const(value: Double) extends Expr(0)
    case class Var(s : String) extends Expr(0)

    case class BinOp(symbol : BinOpSymbol, x: Expr, y: Expr) extends Expr(symbol.priority)

    case class Neg(x: Expr) extends Expr(0)

    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr) extends Expr(3)
    case class FunCall(name : QualifiedName, args : List[Expr]) extends Expr(0)

    abstract class CondSymbol()

    case class Less() extends CondSymbol()
    case class LessEqual() extends CondSymbol()
    case class Greater() extends CondSymbol()
    case class GreaterEqual() extends CondSymbol()
    case class Equal() extends CondSymbol()
    case class NotEqual() extends CondSymbol()

    sealed abstract class BooleanExpr

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr

    case class Or   (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr

    case class And  (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr

    case class Not  (x : BooleanExpr) extends BooleanExpr
}

