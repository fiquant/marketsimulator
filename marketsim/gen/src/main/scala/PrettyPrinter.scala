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

        def apply(p : AST.Parameter) : String
        def apply(p : AST.QualifiedName) : String
        def apply(p : AST.Annotation) : String
        def apply(p : AST.DocString) : String
        def apply(p : AST.FunDef) : String
        def apply(p : AST.Definitions) : String
    }

    var instance : Base = null
}

