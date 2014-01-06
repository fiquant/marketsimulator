import TypesUnbound.TypeMapper

package object TypesBound
{
    import predef.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    sealed abstract class Base
            extends sc.Base
            with    py.Bound
            with    ScPyPrintable
    {
        final def canCastTo(other : Base) : Boolean = this == other || (other match {
            case a : Alias => canCastTo(a.target)
            case _ => false
        }) || canCastToImpl(other)

        protected def canCastToImpl(other : Base) = false

        def cannotCastTo(other : Base) = !canCastTo(other)

        def returnTypeIfFunction : Option[Base] = None
    }

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
        override def canCastToImpl(other : Base) = {
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
            extends Base
            with    sc.UsedDefined
            with    py.UsedDefined
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Base]

        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Type $decl is instantiated with wrong type parameters: $genericArgs" )
    }

    def allSubstitutions[T](lst : List[T], f : T => Iterable[T]) : Stream[List[T]] =
    {
        def elementSubstitution(head : List[T],
                                elem : T,
                                tail : List[T]) =

            f(elem) map { x => head ++ (x :: tail) }

        def partitions(head : List[T], tail : List[T]) : Stream[(List[T], T, List[T])] =
            tail match {
                case Nil => Stream.empty
                case x :: tl =>
                    (head, x, tl) +: partitions(head :+ x, tl)
            }
        partitions(Nil, lst) flatMap { case (head, x, tail) => elementSubstitution(head, x, tail) }
    }

    def directCasts(genericArgs : List[Base]) : Stream[List[Base]]=

        allSubstitutions[Base](genericArgs, directCasts)

    def directCasts(e : Base) : Stream[Base] = e match
    {
        case x : Alias      => Stream(x.target)
        case x : Interface  => x.bases.toStream
        case x if x == Unit => Stream.empty
        case x : Tuple      => directCasts(x.elems) map Tuple
        case x : Function   => directCasts(x.ret) map { Function(x.args, _)}
    }



    case class Interface(decl : Typed.InterfaceDecl, genericArgs : List[Base]) extends UserDefined
    {
        val bases = decl.bases map { _ bind TypeMapper(decl, genericArgs) }

        override def canCastToImpl(other : Base) =  (bases exists { _ canCastTo other }) ||
                (directCasts(genericArgs) map { g => copy(genericArgs = g) } exists { _ canCastTo other})

        override def returnTypeIfFunction =
            bases flatMap { _.returnTypeIfFunction } match {
                case Nil => None
                case x :: tl =>
                    if (tl exists { _ != x})
                        throw new Exception(s"Type $this casts to different functional types: " + (x :: tl))
                    Some(x)
            }
    }

    case class Alias(decl : Typed.AliasDecl, genericArgs : List[Base]) extends UserDefined
    {
        val target = decl.target bind TypeMapper(decl, genericArgs)

        override def canCastToImpl(other : Base) =  (target canCastTo other) ||
                    (directCasts(genericArgs) map { g => copy(genericArgs = g) } exists { _ canCastTo other})

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

}
