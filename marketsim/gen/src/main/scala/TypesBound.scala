import TypesUnbound.TypeMapper

package object TypesBound
{
    import predef.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    sealed abstract class Base
            extends sc.Base
            with    py.Printable
            with    ScPyPrintable
    {
        final def canCastTo(other : Base) : Boolean = this == other || (other match {
            case a : Alias      => canCastTo(a.target)
            case Optional(x)    => canCastTo(x)
            case Any_           => true
            case _              => false
        }) || canCastToImpl(other)

        protected def canCastToImpl(other : Base) = false

        def cannotCastTo(other : Base) = !canCastTo(other)

        def returnTypeIfFunction : Option[Base] = None
        def paramTypesIfFunction : Option[List[Base]] = None
    }

    case object Unit
            extends Base
            with    sc.Unit
            with    py.Unit

    case object Nothing
            extends Base
            with    sc.Nothing
            with    py.Nothing
    {
        override def canCastToImpl(other : Base) = true
    }

    case object Any_
            extends Base
            with    sc.Any_
            with    py.Any_

    case class Optional(x : Base)
            extends Base
            with    sc.Optional
            with    py.Optional
    {
        override def canCastToImpl(other : Base) = other match {
            case Optional(y) => x canCastTo y
            case _           => false
        }
    }

    def unOptionalize(t : Base) : Base =  t match {
        case Optional(x) => unOptionalize(x)
        case x => x
    }

    case class List_(x : Base)
            extends Base
            with    sc.List_
            with    py.List_
    {
        override def canCastToImpl(other : Base) = {
            other match {
                case List_(y) => x canCastTo y
                case _ => false
            }
        }
    }
    case class Tuple(elems : List[Base])
            extends Base
            with    sc.Tuple
            with    py.Tuple

    case class Function(args : List[Base], ret : Base)
            extends Base
            with    sc.Function
            with    py.Function
    {
        Typed.topLevel.IFunction addInstance this

        override def canCastToImpl(other : Base) = {
            other match {
                case f: Function =>
                    (f betterThan this) && (ret canCastTo f.ret)
                case _ => false
            }
        }

        def betterThan(other : Function) =
            (args.length == other.args.length) &&
            (args zip other.args forall { case (mine, others) => mine canCastTo others })

        override def returnTypeIfFunction = Some(ret)
        override def paramTypesIfFunction = Some(args)

        val mandatory_arg_count = args lastIndexWhere { !_.isInstanceOf[Optional] } match {
            case -1  => 0
            case idx => idx
        }
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

    def directCasts(e : Base) : Stream[Base] =
        if (e == Any_)
            Stream.empty
        else
            Any_ #:: (e match {
                case x : ImplementationClass => Stream.empty
                case x : Alias      => Stream(x.target)
                case x : Interface  => x.bases.toStream
                case Unit           => Stream.empty
                case Any_           => throw new Exception("cannot happen")
                case List_(x)       => directCasts(x) map List_
                case Nothing        => throw new Exception("don't know how to implement")
                case Optional(x)    => directCasts(x) map Optional
                case x : Tuple      => directCasts(x.elems) map Tuple
                case x : Function   => directCasts(x.ret) map { Function(x.args, _)}
            })



    case class Interface(decl : Typed.InterfaceDecl, genericArgs : List[Base]) extends UserDefined
    {
        decl addInstance this

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

        override def paramTypesIfFunction =
            bases flatMap { _.paramTypesIfFunction } match {
                case Nil => None
                case x :: tl =>
                    if (tl exists { _ != x})
                        throw new Exception(s"Type $this casts to different functional types: " + (x :: tl))
                    Some(x)
            }
    }

    case class ImplementationClass(name : String, module : String) extends Base with py.ImplementationClass
    {
        def toScala = "NA"
    }

    def isObservable(t : Base) = t match {
        case Interface(Typed.InterfaceDecl("IObservable", _, _, _,_,_), _) => true
        case _ => false
    }

    def isStrategy(t : Base) = t match {
        case Interface(Typed.InterfaceDecl("ISingleAssetStrategy",_,_,_,_,_), _) => true
        case _ => false
    }

    case class Alias(decl : Typed.AliasDecl, genericArgs : List[Base]) extends UserDefined
    {
        val target = decl.target bind TypeMapper(decl, genericArgs)

        override def canCastToImpl(other : Base) =  (target canCastTo other) ||
                    (directCasts(genericArgs) map { g => copy(genericArgs = g) } exists { _ canCastTo other})

        override def returnTypeIfFunction = target.returnTypeIfFunction
        override def paramTypesIfFunction = target.paramTypesIfFunction
    }

}
