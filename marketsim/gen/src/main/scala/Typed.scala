package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => pp}
    import AST.Printable

    abstract class Expr {
        def ty : Types.Base
    }

    abstract class ArithExpr
            extends Expr
            with    pp.Expr

    case class Neg(x : ArithExpr)
            extends ArithExpr
            with    pp.Neg
            with    Printable
            with    TypeInference.Neg

    case class BinOp(symbol : BinOpSymbol,
                     x      : ArithExpr,
                     y      : ArithExpr)
            extends ArithExpr
            with    pp.BinOp
            with    Printable
            with    TypeInference.BinOp

    case class IfThenElse(cond  : BooleanExpr,
                          x     : ArithExpr,
                          y     : ArithExpr)
            extends ArithExpr
            with    pp.IfThenElse
            with    Printable
            with    TypeInference.IfThenElse

    case class FloatConst(x : Double)
            extends ArithExpr
            with    pp.FloatConst
            with    Printable
            with    TypeInference.FloatConst

    case class ParamRef(p : Parameter)
            extends ArithExpr
            with    pp.ParamRef
            with    Printable
            with    TypeInference.ParamRef

    case class FunctionCall(target      : Function,
                            arguments   : List[(Parameter, ArithExpr)])
            extends ArithExpr
            with    pp.FunCall
            with    Printable
            with    TypeInference.FunctionCall

    case class Annotation(target    : AnnotationHandler,
                          parameters: List[String])
            extends pp.Annotation
            with    Printable

    case class Parameter(name        : String,
                         ty          : Types.Base,
                         initializer : Option[Expr])
            extends pp.Parameter
            with    Printable

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : Types.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation])
            extends pp.Function
            with    Printable
    {
        parent.insert(this)
    }

    abstract class BooleanExpr
            extends Expr
            with    pp.BooleanExpr
            with    TypeInference.BooleanExpr

    case class Or(x : BooleanExpr,
                  y : BooleanExpr)
            extends BooleanExpr
            with    pp.Or
            with    Printable

    case class And(x : BooleanExpr,
                   y : BooleanExpr)
            extends BooleanExpr
            with    pp.And
            with    Printable

    case class Not(x : BooleanExpr)
            extends BooleanExpr
            with    pp.Not
            with    Printable

    case class Condition(symbol : CondSymbol,
                         x      : ArithExpr,
                         y      : ArithExpr)
            extends BooleanExpr
            with    pp.Condition
            with    Printable
            with    TypeInference.Condition

    class Package(val name : String)
    {
        var functions = Map[String, Function]()
        var packages = Map[String, SubPackage]()

        def qualifiedName : QualifiedName = QualifiedName(name :: Nil)

        def insert(f : Function) {
            functions = functions.updated(f.name, f)
        }

        def createChild(n : String) = {
            val p = new SubPackage(n, this)
            packages = packages.updated(p.name, p)
            p
        }
    }

    class SubPackage(n : String, parent : Package) extends Package(n)
    {
        override def qualifiedName = parent.qualifiedName ++ n
    }

    val globals = new Package("_root_")

    trait AnnotationHandler
    {
        def apply(f : Function) : (String, String, List[String])
        val name : String
    }

    object Annotations
    {
        var registry = Map[String, AnnotationHandler]()

        def register(handler : AnnotationHandler){
            registry = registry.updated(handler.name, handler)
        }

        def lookup(name : String) = registry.get(name) match {
            case Some(handler) => handler
            case None => throw new Exception(s"Cannot find annotation handler $name")
        }

        override def toString = registry.toString
    }

}

