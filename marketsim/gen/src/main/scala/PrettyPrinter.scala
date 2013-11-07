package object PrettyPrinter
{
    abstract class Base
    {
        def apply(x : Types.Type) : String
        def apply(x : AST.BooleanExpr) : String
    }

    var instance : Base = null
}

