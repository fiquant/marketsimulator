package object AST {

    val crlf = "\r\n"

    import PrettyPrinter.Printable

    trait ScalaPrinter
    {
        def toScala : String
    }

    trait PP_Base
    {
        self : ScalaPrinter =>

        override def toString = toScala
    }

    sealed abstract class Type

    case class SimpleType   (name : String)                          extends Type with syntax.scala.PP.SimpleType with PP_Base
    case object UnitType                                             extends Type with syntax.scala.PP.UnitType with PP_Base
    case class FunctionType (arg_type : List[Type], ret_type : Type) extends Type with syntax.scala.PP.FunctionType with PP_Base
    case class TupleType    (types : List[Type])                     extends Type with syntax.scala.PP.TupleType with PP_Base
    {
        assert(types.length > 1) // SimpleType or UnitType should be used in this case
    }


    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         annotations : List[Annotation]) extends syntax.scala.PP.Parameter with PP_Base

    case class QualifiedName(names   : List[String]) extends syntax.scala.PP.QualifiedName with PP_Base
    {
        def ++(s : String) = QualifiedName(names :+ s)
    }

    case class Annotation(name       : QualifiedName,
                          parameters : List[String]) extends syntax.scala.PP.Annotation with PP_Base

    case class DocString(brief : String, detailed : String) extends syntax.scala.PP.DocString with PP_Base

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation]) extends syntax.scala.PP.Function with PP_Base

    case class Definitions(definitions : List[FunDef]) extends syntax.scala.PP.Definitions with PP_Base

    sealed abstract class BinOpSymbol extends syntax.scala.PP.BinOpSymbol
    case object Add extends BinOpSymbol with syntax.scala.PP.Add with PP_Base
    case object Sub extends BinOpSymbol with syntax.scala.PP.Sub with PP_Base
    case object Mul extends BinOpSymbol with syntax.scala.PP.Mul with PP_Base
    case object Div extends BinOpSymbol with syntax.scala.PP.Div with PP_Base

    sealed abstract class Expr extends syntax.scala.PP.Expr

    case class Const     (value: Double)                            extends Expr with syntax.scala.PP.Const with PP_Base
    case class Var       (s : String)                               extends Expr with syntax.scala.PP.Var with PP_Base
    case class Neg       (x: Expr)                                  extends Expr with syntax.scala.PP.Neg with PP_Base
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)   extends Expr with syntax.scala.PP.BinOp with PP_Base
    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr)   extends Expr with syntax.scala.PP.IfThenElse with PP_Base
    case class FunCall   (name : QualifiedName, args : List[Expr])  extends Expr with syntax.scala.PP.FunCall with PP_Base

    sealed abstract class CondSymbol

    case object Less           extends CondSymbol with syntax.scala.PP.Less with PP_Base
    case object LessEqual      extends CondSymbol with syntax.scala.PP.LessEqual with PP_Base
    case object Greater        extends CondSymbol with syntax.scala.PP.Greater with PP_Base
    case object GreaterEqual   extends CondSymbol with syntax.scala.PP.GreaterEqual with PP_Base
    case object Equal          extends CondSymbol with syntax.scala.PP.Equal with PP_Base
    case object NotEqual       extends CondSymbol with syntax.scala.PP.NotEqual with PP_Base

    sealed abstract class BooleanExpr

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends BooleanExpr with syntax.scala.PP.Condition with PP_Base
    case class Or       (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with syntax.scala.PP.Or with PP_Base
    case class And      (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with syntax.scala.PP.And with PP_Base
    case class Not      (x : BooleanExpr)                           extends BooleanExpr with syntax.scala.PP.Not with PP_Base
}

