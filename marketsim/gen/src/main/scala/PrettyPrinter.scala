package object PrettyPrinter
{
    abstract class Base
    {
        def apply(x : Types.Type) : String
        def apply(x : AST.Expr) : String
        def apply(x : AST.BooleanExpr) : String
        def apply(x : AST.CondSymbol) : String
        def apply(x : AST.BinOpSymbol) : String
    }

    var instance : Base = null
}

