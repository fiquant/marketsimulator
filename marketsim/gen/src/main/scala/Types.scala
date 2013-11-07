package object Types
{
    sealed abstract class Base {
        override def toString : String = PrettyPrinter.instance(this)
    }
    case class `Float`() extends Base
    case class Unit() extends Base
    case class Tuple(elems : List[Base]) extends Base
    case class Function(args : Base, ret : Base) extends Base

    def fromAST(t : AST.Type) : Base = t match {
        case AST.SimpleType("Float") => `Float`()
        case AST.SimpleType(name) => throw new Exception(s"Unknown type $name")
        case AST.UnitType() => Unit()
        case AST.TupleType(types) => Tuple(types map fromAST)
        case AST.FunctionType(arg_type, ret_type) => Function(fromAST(arg_type), fromAST(ret_type))
    }
}
