import predef.ScPrintable
import scala.util.parsing.input.{Position}

package object AST {

    import syntax.scala.Printer.{ast => pp}

    trait Positional extends scala.util.parsing.input.Positional
    {
        var filename : String = "<undefined filename>"

        def setPos(pos : Position, _filename : String) : this.type = {
            filename = _filename
            super.setPos(pos)
            this
        }

        def copyPositionFrom(other : Positional) : this.type = setPos(other.pos, other.filename)
    }

    sealed abstract class Type extends pp.TypeBase

    case class SimpleType(name : QualifiedName, genericArgs : List[Type] = Nil)
            extends Type
            with    pp.SimpleType
            with    ScPrintable

    case object UnitType
            extends Type
            with    pp.UnitType
            with    ScPrintable

    case class FunctionType (args : List[Type], ret : Type)
            extends Type
            with    pp.FunctionType
            with    ScPrintable

    case class TupleType(elems : List[Type])
            extends Type
            with    pp.TupleType
            with    ScPrintable
    {
        assert(elems.length > 1) // SimpleType or UnitType should be used in this case
    }

    case class Parameter(name        : String,
                         ty          : Option[Type],
                         initializer : Option[Expr],
                         comment     : List[String]) extends pp.Parameter with ScPrintable

    case class QualifiedName(names   : List[String]) extends pp.QualifiedName with ScPrintable

    implicit def toQualifiedName(name : List[String])  = AST.QualifiedName(name)
    implicit def fromQualifiedName(name : QualifiedName)  = name.names

    val side_t = SimpleType(""::"Side"::Nil, Nil)
    val float_t = SimpleType(""::"Float"::Nil, Nil)

    def functionOf(t : Type) = FunctionType(Nil, t)

    val side_function_t = functionOf(side_t)
    val float_function_t = functionOf(float_t)

    abstract class Decorator extends pp.Decorator

    case class Annotation(name       : QualifiedName,
                          parameters : List[String])
            extends Decorator
            with    pp.Annotation
            with    ScPrintable

    case class Attribute(name : String, value : String)
            extends Decorator
            with    pp.Attribute
            with    ScPrintable

    case class DocString(brief : String, detailed : List[String]) extends pp.DocString with ScPrintable

    abstract sealed class Definition extends pp.Definition

    abstract sealed class FunctionDeclaration extends Definition
    {
        val name : String
    }

    case class PackageDef(name      : Option[QualifiedName],
                          parameters: List[Parameter],
                          members   : Definitions,
                          attributes: List[Attribute],
                          bases     : List[QualifiedName],
                          `abstract`: Boolean) extends Definition with pp.Package with ScPrintable
    {
        def getName = if (name.nonEmpty) name.get.toString else ""
    }

    case class Generics(elems : List[String])
            extends pp.Generics
            with    ScPrintable

    case class FunDef(name           : String,
                      parameters     : List[Parameter],
                      body           : Option[Expr],
                      ty             : Option[Type],
                      docstring      : Option[DocString],
                      decorators     : List[Decorator])
            extends FunctionDeclaration
            with    pp.Function
            with    ScPrintable
            with    Positional

    case class FunAlias(name    : String,
                        target  : QualifiedName)
            extends FunctionDeclaration
            with    pp.FunctionAlias
            with    ScPrintable

    sealed abstract class TypeDeclaration extends Definition
    {
        val name : String
    }

    case class Interface(name       : String,
                         generics   : Generics,
                         bases      : List[Type])
            extends TypeDeclaration
            with    pp.TypeDeclaration
            with    ScPrintable

    case class Alias(name       : String,
                     generics   : Generics,
                     target     : Type)
            extends TypeDeclaration
            with    pp.TypeAlias
            with    ScPrintable

    case class Definitions(definitions : List[Definition]) extends pp.Definitions with ScPrintable

    sealed abstract class BinOpSymbol extends pp.BinOpSymbol
    case object Add extends BinOpSymbol with pp.Add with ScPrintable
    case object Sub extends BinOpSymbol with pp.Sub with ScPrintable
    case object Mul extends BinOpSymbol with pp.Mul with ScPrintable
    case object Div extends BinOpSymbol with pp.Div with ScPrintable

    sealed abstract class Expr extends pp.Expr

    case class FloatLit  (value: Double)                                  extends Expr with pp.FloatLit with ScPrintable
    case class StringLit (value: String)                                  extends Expr with pp.StringLit with ScPrintable
    case class IntLit    (value: Int)                                     extends Expr with pp.IntLit with ScPrintable
    case class Var       (s : String)                                     extends Expr with pp.Var with ScPrintable
    case class Neg       (x: Expr)                                        extends Expr with pp.Neg with ScPrintable
    case class BinOp     (symbol : BinOpSymbol, x: Expr, y: Expr)         extends Expr with pp.BinOp with ScPrintable
    case class IfThenElse(cond : Expr, x : Expr, y : Expr)                extends Expr with pp.IfThenElse with ScPrintable
    case class FunCall   (name : QualifiedName, args : List[Expr])        extends Expr with pp.FunCall with ScPrintable
    case class Cast      (x : Expr, ty : Type)                            extends Expr with pp.Cast with ScPrintable
    case class List_     (xs : List[Expr])                                extends Expr with pp.List_ with ScPrintable

    sealed abstract class CondSymbol extends pp.CondSymbol

    case object Less           extends CondSymbol with pp.Less with ScPrintable
    case object LessEqual      extends CondSymbol with pp.LessEqual with ScPrintable
    case object Greater        extends CondSymbol with pp.Greater with ScPrintable
    case object GreaterEqual   extends CondSymbol with pp.GreaterEqual with ScPrintable
    case object Equal          extends CondSymbol with pp.Equal with ScPrintable
    case object NotEqual       extends CondSymbol with pp.NotEqual with ScPrintable

    case class Condition(symbol : CondSymbol, x : Expr, y : Expr)   extends Expr with pp.Condition with ScPrintable
    case class Or       (x : Expr, y : Expr)                        extends Expr with pp.Or with ScPrintable
    case class And      (x : Expr, y : Expr)                        extends Expr with pp.And with ScPrintable
    case class Not      (x : Expr)                                  extends Expr with pp.Not with ScPrintable
}

