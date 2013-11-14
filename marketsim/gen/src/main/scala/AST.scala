package object AST {

    val crlf = "\r\n"

    import PrettyPrinter.Printable

    sealed abstract class Type extends Printable

    case class SimpleType   (name : String)                          extends Type
    case object UnitType                                             extends Type
    case class FunctionType (arg_type : List[Type], ret_type : Type) extends Type
    case class TupleType    (types : List[Type])                     extends Type
    {
        assert(types.length > 1) // SimpleType or UnitType should be used in this case
    }


    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         annotations : List[Annotation]) extends Printable

    case class QualifiedName(names   : List[String]) extends Printable
    {
        def ++(s : String) = QualifiedName(names :+ s)
    }

    case class Annotation(name       : QualifiedName,
                          parameters : List[String]) extends Printable

    case class DocString(brief : String, detailed : String) extends Printable

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation]) extends Printable

    case class Definitions(definitions : List[FunDef]) extends Printable

    sealed abstract class BinOpSymbol extends Printable
    case object Add extends BinOpSymbol
    case object Sub extends BinOpSymbol
    case object Mul extends BinOpSymbol
    case object Div extends BinOpSymbol

    sealed abstract class Expr extends Printable

    case class Const     (value: Double)                            extends Expr
    case class Var       (s : String)                               extends Expr
    case class Neg       (x: Expr)                                  extends Expr
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)   extends Expr
    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr)   extends Expr
    case class FunCall   (name : QualifiedName, args : List[Expr])  extends Expr

    sealed abstract class CondSymbol extends Printable

    case object Less           extends CondSymbol
    case object LessEqual      extends CondSymbol
    case object Greater        extends CondSymbol
    case object GreaterEqual   extends CondSymbol
    case object Equal          extends CondSymbol
    case object NotEqual       extends CondSymbol

    sealed abstract class BooleanExpr extends Printable

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends BooleanExpr
    case class Or       (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr
    case class And      (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr
    case class Not      (x : BooleanExpr)                           extends BooleanExpr
}

