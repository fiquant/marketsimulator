package object PrettyPrinter
{
    abstract class Base
    {
        def apply(x : Types.Base) : String
        def apply(x : AST.Type) : String
        def apply(x : AST.Expr) : String
        def apply(x : AST.BooleanExpr) : String
        def apply(x : AST.CondSymbol) : String
        def apply(x : AST.BinOpSymbol) : String
    }

    var instance : Base = null
}

