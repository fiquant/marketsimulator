package object PrettyPrinter
{
    abstract class Printable {
        override def toString = PrettyPrinter.instance(this)
    }

    abstract class Base
    {
        def apply(p : Typed.Expr) : String
        def apply(p : Typed.Parameter) : String
        def apply(p : Typed.Function) : String
        def apply(p : Typed.BooleanExpr) : String

        def apply(p : Typed.Annotation) : String

        def apply(p : Printable): String = p match {

            case x : Typed.BooleanExpr  => apply(x)
            case x : Typed.Expr         => apply(x)
            case x : Typed.Parameter    => apply(x)
            case x : Typed.Function     => apply(x)

            case x : Typed.Annotation   => apply(x)
        }
    }

    var instance : Base = null
}

