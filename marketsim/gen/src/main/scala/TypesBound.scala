import TypesUnbound.TypeMapper

package object TypesBound
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    sealed abstract class Bound
            extends sc.Base
            with    py.Bound
            with    ScPyPrintable
    {
        final def canCastTo(other : Bound) : Boolean = this == other || (other match {
            case a : Alias => canCastTo(a.target)
            case _ => false
        }) || canCastToImpl(other)

        protected def canCastToImpl(other : Bound) = false

        def cannotCastTo(other : Bound) = !canCastTo(other)

        def returnTypeIfFunction : Option[Bound] = None
    }

    case object Unit
            extends Bound
            with    sc.Unit
            with    py.Unit

    case class Tuple(elems : List[Bound])
            extends Bound
            with    sc.Tuple
            with    py.Tuple

    case class Function(args : List[Bound], ret : Bound)
            extends Bound
            with    sc.Function
            with    py.Function
    {
        override def canCastToImpl(other : Bound) = {
            other match {
                case f: Function =>
                    (f.args.length == args.length) &&
                    (ret canCastTo f.ret) &&
                    (args zip f.args).forall({
                        case (mine, others) => others canCastTo mine
                    })
                case _ => false
            }
        }

        override def returnTypeIfFunction = Some(ret)
    }

    sealed abstract class UserDefined
            extends Bound
            with    sc.UsedDefined
            with    py.UsedDefined
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Bound]

        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Type $decl is instantiated with wrong type parameters: $genericArgs" )
    }

    case class Interface(decl : Typed.Interface, genericArgs : List[Bound]) extends UserDefined
    {
        val bases = decl.bases map { _ bind TypeMapper(decl, genericArgs) }

        override def canCastToImpl(other : Bound) =  bases exists { _ canCastTo other }

        override def returnTypeIfFunction =
            bases flatMap { _.returnTypeIfFunction } match {
                case Nil => None
                case x :: tl =>
                    if (tl exists { _ != x})
                        throw new Exception(s"Type $this casts to different functional types: " + (x :: tl))
                    Some(x)
            }
    }

    case class Alias(decl : Typed.Alias, genericArgs : List[Bound]) extends UserDefined
    {
        val target = decl.target bind TypeMapper(decl, genericArgs)

        override def canCastToImpl(other : Bound) =  target canCastTo other

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

}
