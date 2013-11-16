package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => pp}
    import AST.Printable

    private def floatRank(e: Expr) = e.ty match {
        case Types.`Float` => 0
        case Types.FloatFunc => 1
        case t => throw new Exception(s"has wrong type $t")
    }

    private def unifyFloat(xs : Expr*) =
        if ((xs map floatRank).sum > 0) Types.FloatFunc else Types.`Float`

    abstract class Expr {
        def ty : Types.Base
    }

    abstract class ArithExpr extends Expr with pp.Expr

    case class Neg(x : ArithExpr) extends ArithExpr with pp.Neg with Printable
    {
        def ty = unifyFloat(x)
    }

    case class BinOp(symbol : BinOpSymbol, x : ArithExpr, y : ArithExpr) extends ArithExpr with pp.BinOp with Printable
    {
        def ty = unifyFloat(x,y)
    }

    case class IfThenElse(cond : BooleanExpr, x : ArithExpr, y : ArithExpr) extends ArithExpr with pp.IfThenElse with Printable
    {
        def ty = unifyFloat(x,y)
    }

    case class FloatConst(x : Double) extends ArithExpr with pp.FloatConst with Printable {
        val ty = Types.`Float`
    }

    case class ParamRef(p : Parameter) extends ArithExpr with pp.ParamRef with Printable {
        def ty = p.ty
    }

    case class FunctionCall(target : Function, arguments : List[(Parameter, ArithExpr)]) extends ArithExpr with pp.FunCall with Printable {
        def ty = Types.nullaryFunction(target.ret_type)
    }

    case class Annotation(target : AnnotationHandler, parameters : List[String]) extends pp.Annotation with Printable

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr]) extends pp.Parameter with Printable

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : Types.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation]) extends pp.Function with Printable
    {
        parent.insert(this)
    }

    abstract class BooleanExpr extends Expr with pp.BooleanExpr {
        val ty = Types.BooleanFunc
    }

    case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr with pp.Or with Printable
    case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr with pp.And with Printable
    case class Not(x : BooleanExpr) extends BooleanExpr with pp.Not with Printable

    case class Condition(symbol : CondSymbol, x : ArithExpr, y : ArithExpr) extends BooleanExpr with pp.Condition with Printable
    {
        override val ty = {
            if (unifyFloat(x,y) != Types.FloatFunc)
                throw new Exception(s"Arguments of boolean expression must be casted to () => Float")
            Types.BooleanFunc
        }
    }

    class Package(val name : String, parent : Option[Package] = None)
    {
        var functions = Map[String, Function]()
        var packages = Map[String, Package]()

        if (parent.nonEmpty)
            parent.get.insert(this)

        val qualifiedName : QualifiedName =
            if (parent.isEmpty) QualifiedName(Nil) else parent.get.qualifiedName ++ name

        def insert(f : Function) {
            functions = functions.updated(f.name, f)
        }

        def insert(p : Package) {
            packages = packages.updated(p.name, p)
        }
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