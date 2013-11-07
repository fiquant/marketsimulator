package object Types
{
    sealed abstract class Type {
        override def toString : String = PrettyPrinter.instance(this)
    }
    case class `Float`() extends Type
    case class Unit() extends Type
    case class Tuple(elems : List[Type]) extends Type
    case class Function(args : Type, ret : Type) extends Type

    def fromAST(t : AST.Type) : Type = t match {
        case AST.SimpleType("Float") => `Float`()
        case AST.SimpleType(name) => throw new Exception(s"Unknown type $name")
        case AST.UnitType() => Unit()
        case AST.TupleType(types) => Tuple(types map fromAST)
        case AST.FunctionType(arg_type, ret_type) => Function(fromAST(arg_type), fromAST(ret_type))
    }
}
