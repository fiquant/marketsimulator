import syntax.scala.TypedPP     // TODO: break somehow this dependency

package object Types
{
    sealed abstract class Type
    case class `Float`() extends Type
    case class Unit() extends Type
    case class Tuple(elems : List[Type]) extends Type
    case class Function(args : Type, ret : Type) extends Type

    def fromAST(t : AST.Type) : Type = t match {
        case AST.SimpleType("Float") => new `Float`() with TypedPP.`Float`
        case AST.SimpleType(name) => throw new Exception(s"Unknown type $name")
        case AST.UnitType() => new Unit() with TypedPP.Unit
        case AST.TupleType(types) => new Tuple(types map fromAST) with TypedPP.Tuple
        case AST.FunctionType(arg_type, ret_type) => new Function(fromAST(arg_type), fromAST(ret_type)) with TypedPP.Function
    }
}
