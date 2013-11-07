package object AST {

    val crlf = "\r\n"

    sealed abstract class Type {
        override def toString = PrettyPrinter.instance(this)
    }

    case class SimpleType   (name : String)                     extends Type
    case class UnitType     ()                                  extends Type
    case class FunctionType (arg_type : Type, ret_type : Type)  extends Type
    case class TupleType    (types : List[Type])                extends Type
    {
        assert(types.length > 1) // SimpleType or UnitType should be used in this case
    }


    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         annotations : List[Annotation])
    {
        override def toString = PrettyPrinter.instance(this)
    }

    case class QualifiedName(names   : List[String]){
        override def toString = PrettyPrinter.instance(this)
    }

    case class Annotation(name       : QualifiedName,
                          parameters : List[String])
    {
        override def toString = PrettyPrinter.instance(this)
    }

    case class DocString(brief : String, detailed : String)
    {
        override def toString = PrettyPrinter.instance(this)
    }

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation])
    {
        override def toString  = PrettyPrinter.instance(this)
    }

    case class Definitions(definitions : List[FunDef])
    {
        override def toString = PrettyPrinter.instance(this)
    }

    sealed abstract class BinOpSymbol {
        override def toString = PrettyPrinter.instance(this)
    }
    case class Add() extends BinOpSymbol
    case class Sub() extends BinOpSymbol
    case class Mul() extends BinOpSymbol
    case class Div() extends BinOpSymbol

    sealed abstract class Expr {
        override def toString = PrettyPrinter.instance(this)
    }

    case class Const     (value: Double)                            extends Expr
    case class Var       (s : String)                               extends Expr
    case class Neg       (x: Expr)                                  extends Expr
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)   extends Expr
    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr)   extends Expr
    case class FunCall   (name : QualifiedName, args : List[Expr])  extends Expr

    sealed abstract class CondSymbol {
        override def toString = PrettyPrinter.instance(this)
    }

    case class Less()           extends CondSymbol
    case class LessEqual()      extends CondSymbol
    case class Greater()        extends CondSymbol
    case class GreaterEqual()   extends CondSymbol
    case class Equal()          extends CondSymbol
    case class NotEqual()       extends CondSymbol

    sealed abstract class BooleanExpr {
        override def toString = PrettyPrinter.instance(this)
    }

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends BooleanExpr
    case class Or       (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr
    case class And      (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr
    case class Not      (x : BooleanExpr)                           extends BooleanExpr
}

