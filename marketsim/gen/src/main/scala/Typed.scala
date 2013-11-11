package object Typed
{
    abstract class Expr {
        def ty : Types.Base
    }

    case class Parameter(name : String, ty : Types.Base, initializer : Option[Expr])

    case class Function(name : String, params : List[Parameter], ty : Types.Base)
}