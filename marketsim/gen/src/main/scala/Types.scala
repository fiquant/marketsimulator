package object Types
{
    sealed abstract class Base {
        override def toString : String = PrettyPrinter.instance(this)
    }
    case object `Float` extends Base
    case object Unit extends Base
    case class Tuple(elems : List[Base]) extends Base
    case class Function(args : List[Base], ret : Base) extends Base

    val FloatFunc = Function(Nil, `Float`)

    def fromAST(t : AST.Type) : Base = t match {
        case AST.SimpleType("Float") => `Float`
        case AST.SimpleType(name) => throw new Exception(s"Unknown type $name")
        case AST.UnitType => Unit
        case AST.TupleType(types) => Tuple(types map fromAST)
        case AST.FunctionType(arg_types, ret_type) => Function(arg_types map fromAST, fromAST(ret_type))
    }
}
