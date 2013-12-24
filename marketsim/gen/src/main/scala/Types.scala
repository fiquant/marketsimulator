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
            with    sc.UserDefined
            with    py.UserDefined
    {
        val name : String
        val scope : Typed.Package

        override def equals(o : Any) = o match {
            case that : UserDefined => name == that.name && scope.qualifiedName == that.scope.qualifiedName
            case _ => false
        }
    }

    case class Interface(name : String, scope : Typed.Package, bases : List[Base]) extends UserDefined
    {
        override def canCastToImpl(other : Base) =  bases exists { _ canCastTo other }

        override def equals(o : Any) = super.equals(o) && (o match {
            case that : Interface => bases == that.bases
            case _ => false
        })

        override def returnTypeIfFunction =
            bases flatMap { _.returnTypeIfFunction } match {
                case Nil => None
                case x :: tl =>
                    if (tl exists { _ != x})
                        throw new Exception(s"Type $this casts to different functional types: " + (x :: tl))
                    Some(x)
            }
    }

    case class Alias(name : String, scope : Typed.Package, target : Base) extends UserDefined
    {
        override def canCastToImpl(other : Base) =  target canCastTo other

        override def equals(o: Any) = super.equals(o) && (o match {
            case that: Alias => target == that.target
            case _ => false
        })

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)

    val String_ = Typed.TypeDeclaration(Interface("String", Typed.topLevel, Nil)).ty

    val Float_ = Typed.TypeDeclaration(Interface("Float", Typed.topLevel, Nil)).ty
    val FloatFunc = Typed.TypeDeclaration(Alias("IFunction", Typed.topLevel, nullaryFunction(Float_))).ty
    val FloatObservable = Typed.TypeDeclaration(Interface("IObservable", Typed.topLevel, FloatFunc :: Nil)).ty

    val Int_ = Typed.TypeDeclaration(Interface("Int", Typed.topLevel, Float_ :: Nil)).ty

    val Boolean_ = Typed.TypeDeclaration(Interface("Boolean", Typed.topLevel, Nil)).ty
    val BooleanFunc = Typed.TypeDeclaration(Alias("IFunction_Boolean", Typed.topLevel, nullaryFunction(Boolean_))).ty

    val CandleStick = Typed.TypeDeclaration(Interface("CandleStick", Typed.topLevel, Nil)).ty
    val CandleStickFunc = Typed.TypeDeclaration(Alias("IFunction_CandleStick", Typed.topLevel, nullaryFunction(CandleStick))).ty
    val CandleStickObservable = Typed.TypeDeclaration(Interface("IObservable_CandleStick", Typed.topLevel, CandleStickFunc :: Nil)).ty

    val VolumeLevels = Typed.TypeDeclaration(Interface("VolumeLevels", Typed.topLevel, Nil)).ty
    val VolumeLevelsFunc = Typed.TypeDeclaration(Alias("IFunction_VolumeLevels", Typed.topLevel, nullaryFunction(VolumeLevels))).ty

    val Order = Typed.TypeDeclaration(Interface("Order", Typed.topLevel, Nil)).ty
    val OrderFunc = Typed.TypeDeclaration(Alias("IFunction_Order", Typed.topLevel, nullaryFunction(Order))).ty
    val OrderObservable = Typed.TypeDeclaration(Interface("IObservable_Order", Typed.topLevel, OrderFunc :: Nil)).ty

}
