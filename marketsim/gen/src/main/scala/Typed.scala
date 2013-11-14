package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString}
    import PrettyPrinter.Printable

    abstract class Expr(val ty : Types.Base) extends Printable

    case class Neg(t: Types.Base, x : Expr) extends Expr(t)
    case class BinOp(t : Types.Base, op : BinOpSymbol, x : Expr, y : Expr) extends Expr(t)
    case class IfThenElse(t : Types.Base, cond : BooleanExpr, x : Expr, y : Expr) extends Expr(t)
    case class FloatConst(x : Double) extends Expr(Types.`Float`)
    case class ParamRef(p : Parameter) extends Expr(p.ty)
    case class FunctionCall(target : Function, arguments : List[(Parameter, Expr)]) extends Expr(Types.nullaryFunction(target.ret_type))

    case class Annotation(target : AnnotationHandler, parameters : List[String]) extends Printable

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr]) extends Printable

    case class Function(name        : String,
                        parameters  : List[Parameter],
                        ret_type    : Types.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation]) extends Printable

    class BooleanExpr extends Expr(Types.BooleanFunc)

    case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
    case class Not(x : BooleanExpr) extends BooleanExpr
    case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr

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