package object AST {

    trait ScPrintable
    {
        def toScala : String
        override def toString = toScala
    }

    trait PyPrintable
    {
        def toPython : String
        override def toString = toPython
    }

    sealed abstract class PrintMode

    case object ScalaMode extends PrintMode
    case object PythonMode extends PrintMode

    object ScPyPrintable
    {
        var printMode : PrintMode = ScalaMode
    }

    trait ScPyPrintable extends ScPrintable with PyPrintable
    {
        override def toString = ScPyPrintable.printMode match {
            case ScalaMode => toScala
            case PythonMode => toPython
        }
        
        def as(m : PrintMode) = {
            val old_mode = ScPyPrintable.printMode
            ScPyPrintable.printMode = m
            val ret = toString
            ScPyPrintable.printMode = old_mode
            ret
        }

        def asScala = as(ScalaMode)
        def asPython = as(PythonMode)
    }


    
    import syntax.scala.Printer.{ast => pp}

    sealed abstract class Type extends pp.TypeBase

    case class SimpleType   (name : String)                          extends Type with pp.SimpleType with ScPrintable
    case object UnitType                                             extends Type with pp.UnitType with ScPrintable
    case class FunctionType (args : List[Type], ret : Type) extends Type with pp.FunctionType with ScPrintable
    case class TupleType    (elems : List[Type])                     extends Type with pp.TupleType with ScPrintable
    {
        assert(elems.length > 1) // SimpleType or UnitType should be used in this case
    }


    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         comment     : List[String]) extends pp.Parameter with ScPrintable

    case class QualifiedName(names   : List[String]) extends pp.QualifiedName with ScPrintable
    {
        def ++(s : String) = QualifiedName(names :+ s)
        def head = names.head
        def tail = QualifiedName(names.tail)
        def simple = names.length == 1
    }

    case class Annotation(name       : QualifiedName,
                          parameters : List[String]) extends pp.Annotation with ScPrintable

    case class DocString(brief : String, detailed : List[String]) extends pp.DocString with ScPrintable

    abstract sealed class Definition extends pp.Definition

    case class PackageDef(name      : QualifiedName,
                          members   : Definitions) extends Definition with pp.Package with ScPrintable

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ret_type       : Option[Type],
                      docstring      : Option[DocString],
                      annotations    : List[Annotation]) extends Definition with pp.Function with ScPrintable

    case class Definitions(definitions : List[Definition]) extends pp.Definitions with ScPrintable

    sealed abstract class BinOpSymbol extends pp.BinOpSymbol
    case object Add extends BinOpSymbol with pp.Add with ScPrintable
    case object Sub extends BinOpSymbol with pp.Sub with ScPrintable
    case object Mul extends BinOpSymbol with pp.Mul with ScPrintable
    case object Div extends BinOpSymbol with pp.Div with ScPrintable

    sealed abstract class Expr extends pp.Expr

    case class Const     (value: Double)                            extends Expr with pp.Const with ScPrintable
    case class Var       (s : String)                               extends Expr with pp.Var with ScPrintable
    case class Neg       (x: Expr)                                  extends Expr with pp.Neg with ScPrintable
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)   extends Expr with pp.BinOp with ScPrintable
    case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr)   extends Expr with pp.IfThenElse with ScPrintable
    case class FunCall   (name : QualifiedName, args : List[Expr])  extends Expr with pp.FunCall with ScPrintable

    sealed abstract class CondSymbol extends pp.CondSymbol

    case object Less           extends CondSymbol with pp.Less with ScPrintable
    case object LessEqual      extends CondSymbol with pp.LessEqual with ScPrintable
    case object Greater        extends CondSymbol with pp.Greater with ScPrintable
    case object GreaterEqual   extends CondSymbol with pp.GreaterEqual with ScPrintable
    case object Equal          extends CondSymbol with pp.Equal with ScPrintable
    case object NotEqual       extends CondSymbol with pp.NotEqual with ScPrintable

    sealed abstract class BooleanExpr extends pp.BooleanExpr

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends BooleanExpr with pp.Condition with ScPrintable
    case class Or       (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with pp.Or with ScPrintable
    case class And      (x : BooleanExpr, y : BooleanExpr)          extends BooleanExpr with pp.And with ScPrintable
    case class Not      (x : BooleanExpr)                           extends BooleanExpr with pp.Not with ScPrintable
}

