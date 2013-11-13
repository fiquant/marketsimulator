package object PrettyPrinter
{
    abstract class Printable {
        override def toString = PrettyPrinter.instance(this)
    }

    abstract class Base
    {
        def apply(x : Types.Base) : String
        def apply(x : AST.Type) : String
        def apply(x : AST.Expr) : String
        def apply(x : AST.BooleanExpr) : String
        def apply(x : AST.CondSymbol) : String
        def apply(x : AST.BinOpSymbol) : String

        def apply(p : AST.Parameter) : String
        def apply(p : AST.QualifiedName) : String
        def apply(p : AST.Annotation) : String
        def apply(p : AST.DocString) : String
        def apply(p : AST.FunDef) : String
        def apply(p : AST.Definitions) : String

        def apply(p : Typed.Expr) : String
        def apply(p : Typed.Parameter) : String
        def apply(p : Typed.Function) : String
        def apply(p : Typed.BooleanExpr) : String

        def apply(p : Typed.Annotation) : String

        def apply(p : Printable): String = p match {
            case x : Types.Base     => apply(x)
            case x : AST.Type       => apply(x)
            case x : AST.Expr       => apply(x)
            case x : AST.BooleanExpr=> apply(x)
            case x : AST.CondSymbol => apply(x)
            case x : AST.BinOpSymbol=> apply(x)

            case x : AST.Parameter      => apply(x)
            case x : AST.QualifiedName  => apply(x)
            case x : AST.Annotation     => apply(x)
            case x : AST.DocString      => apply(x)
            case x : AST.FunDef         => apply(x)
            case x : AST.Definitions    => apply(x)

            case x : Typed.BooleanExpr  => apply(x)
            case x : Typed.Expr         => apply(x)
            case x : Typed.Parameter    => apply(x)
            case x : Typed.Function     => apply(x)

            case x : Typed.Annotation   => apply(x)
        }
    }

    var instance : Base = null
}

