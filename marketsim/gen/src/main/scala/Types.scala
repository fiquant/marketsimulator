package object Types
{
    import AST.ScPyPrintable
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    // TODO:
    //  Typedef         type A = B
    //  Generics        type G[T] : F[T]

    sealed abstract class Base
            extends sc.Base
            with    py.Base
            with    ScPyPrintable
    {
        def canCastTo(other : Base) = this == other
        def cannotCastTo(other : Base) = !canCastTo(other)
    }

    case object `Float`
            extends Base
            with    sc.`Float`
            with    py.`Float`

    case object `Boolean`
            extends Base
            with    sc.`Boolean`
            with    py.`Boolean`

    case object Unit
            extends Base
            with    sc.Unit
            with    py.Unit

    case class Tuple(elems : List[Base])
            extends Base
            with    sc.Tuple
            with    py.Tuple

    case class Function(args : List[Base], ret : Base)
            extends Base
            with    sc.Function
            with    py.Function
    {
        override def canCastTo(other : Base) = {
            super.canCastTo(other) || (other match {
                case f : Function =>
                    (f.args.length == args.length) &&
                    (ret canCastTo f.ret) &&
                    (args zip f.args).forall({
                        case (mine, others) => others canCastTo mine
                    })
                case _ => false
            })
        }
    }

    abstract class UserDefined
            extends Base
            with    sc.UserDefined
            with    py.UserDefined
    {
        val name : String
        val scope : Typed.Package
    }

    case class Interface(name : String, scope : Typed.Package, bases : List[Base]) extends UserDefined
    {
        override def canCastTo(other : Base) = {
            super.canCastTo(other) || (bases exists { _ canCastTo other })
        }
    }

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)
    val FloatFunc = nullaryFunction(`Float`)
    val BooleanFunc = nullaryFunction(`Boolean`)

}
