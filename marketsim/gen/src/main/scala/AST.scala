package object AST {

    trait Printable
    {
        self : syntax.scala.Printer.Printable =>

        override def toString = toScala
    }
    
    import syntax.scala.Printer.{ast => pp}

    sealed abstract class Type extends pp.TypeBase

    case class SimpleType   (name : String)                          extends Type with pp.SimpleType with Printable
    case object UnitType                                             extends Type with pp.UnitType with Printable
    case class FunctionType (args : List[Type], ret : Type) extends Type with pp.FunctionType with Printable
    case class TupleType    (elems : List[Type])                     extends Type with pp.TupleType with Printable
    {
        assert(elems.length > 1) // SimpleType or UnitType should be used in this case
    }


    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         comment     : List[String]) extends pp.Parameter with Printable

    case class QualifiedName(names   : List[String]) extends pp.QualifiedName with Printable
    {
        def ++(s : String) = QualifiedName(names :+ s)
        def head = names.head
        def tail = QualifiedName(names.tail)
        def simple = names.length == 1
    }

    case class Annotation(name       : QualifiedName,
                          parameters : List[String]) extends pp.Annotation with Printable

    case class DocString(brief : String, detailed : String) extends pp.DocString with Printable

    abstract sealed class Definition extends pp.Definition

    case class PackageDef(name      : QualifiedName,
                          members   : Definitions) extends Definition with pp.Package with Printable

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation]) extends Definition with pp.Function with Printable

    case class Definitions(definitions : List[Definition]) extends pp.Definitions with Printable

    sealed abstract class BinOpSymbol extends pp.BinOpSymbol
    case object Add extends BinOpSymbol with pp.Add with Printable
    case object Sub extends BinOpSymbol with pp.Sub with Printable
    case object Mul extends BinOpSymbol with pp.Mul with Printable
    case object Div extends BinOpSymbol with pp.Div with Printable

    sealed abstract class Expr extends pp.Expr

    case class Const     (value: Double)                            extends Expr with pp.Const with Printable
    case class Var       (s : String)                               extends Expr with pp.Var with Printable
    case class Neg       (x: Expr)                                  extends Expr with pp.Neg with Printable
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)   extends Expr with pp.BinOp with Printable
    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr)   extends Expr with pp.IfThenElse with Printable
    case class FunCall   (name : QualifiedName, args : List[Expr])  extends Expr with pp.FunCall with Printable

    sealed abstract class CondSymbol extends pp.CondSymbol

    case object Less           extends CondSymbol with pp.Less with Printable
    case object LessEqual      extends CondSymbol with pp.LessEqual with Printable
    case object Greater        extends CondSymbol with pp.Greater with Printable
    case object GreaterEqual   extends CondSymbol with pp.GreaterEqual with Printable
    case object Equal          extends CondSymbol with pp.Equal with Printable
    case object NotEqual       extends CondSymbol with pp.NotEqual with Printable

    sealed abstract class BooleanExpr extends pp.BooleanExpr

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends BooleanExpr with pp.Condition with Printable
    case class Or       (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with pp.Or with Printable
    case class And      (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with pp.And with Printable
    case class Not      (x : BooleanExpr)                           extends BooleanExpr with pp.Not with Printable
}

