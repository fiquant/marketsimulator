package object Types
{
    import AST.Printable
    import syntax.scala.Printer.{types => pp}

    sealed abstract class Base extends pp.Base
    case object `Float` extends Base with pp.`Float` with Printable
    case object `Boolean` extends Base with pp.`Boolean` with Printable
    case object Unit extends Base with pp.Unit with Printable
    case class Tuple(elems : List[Base]) extends Base with pp.Tuple with Printable
    case class Function(args : List[Base], ret : Base) extends Base with pp.Function with Printable

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)
    val FloatFunc = nullaryFunction(`Float`)
    val BooleanFunc = nullaryFunction(`Boolean`)

    def fromAST(t : AST.Type) : Base = t match {
        case AST.SimpleType("Float") => `Float`
        case AST.SimpleType("Boolean") => `Boolean`
        case AST.SimpleType(name) => throw new Exception(s"Unknown type $name")
        case AST.UnitType => Unit
        case AST.TupleType(types) => Tuple(types map fromAST)
        case AST.FunctionType(arg_types, ret_type) => Function(arg_types map fromAST, fromAST(ret_type))
    }
}
