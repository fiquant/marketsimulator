package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => pp}

    abstract class Expr(val ty : Types.Base)

    abstract class ArithExpr(override val ty : Types.Base) extends Expr(ty) with pp.Expr

    case class Neg(t: Types.Base, x : ArithExpr) extends ArithExpr(t) with pp.Neg with AST.Printable
    case class BinOp(t : Types.Base, op : BinOpSymbol, x : ArithExpr, y : ArithExpr) extends ArithExpr(t) with pp.BinOp with AST.Printable
    case class IfThenElse(t : Types.Base, cond : BooleanExpr, x : ArithExpr, y : ArithExpr) extends ArithExpr(t) with pp.IfThenElse with AST.Printable
    case class FloatConst(x : Double) extends ArithExpr(Types.`Float`) with pp.FloatConst with AST.Printable
    case class ParamRef(p : Parameter) extends ArithExpr(p.ty) with pp.ParamRef with AST.Printable
    case class FunctionCall(target : Function, arguments : List[(Parameter, ArithExpr)]) extends ArithExpr(Types.nullaryFunction(target.ret_type)) with pp.FunCall with AST.Printable

    case class Annotation(target : AnnotationHandler, parameters : List[String]) extends pp.Annotation with AST.Printable

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr]) extends pp.Parameter with AST.Printable

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : Types.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation]) extends pp.Function with AST.Printable
    {
        parent.insert(this)
    }

    abstract class BooleanExpr extends Expr(Types.BooleanFunc)

    case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr with pp.Or with AST.Printable
    case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr with pp.And with AST.Printable
    case class Not(x : BooleanExpr) extends BooleanExpr with pp.Not with AST.Printable
    case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr with pp.Condition with AST.Printable

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