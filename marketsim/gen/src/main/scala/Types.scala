package object Types
{
    import AST.ScPyPrintable
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    // TODO:
    //  Generics        type G[T] : F[T]

    abstract class BaseUnbound

    sealed abstract class Base
            extends BaseUnbound
            with    sc.Base
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

    sealed abstract class Declaration
            extends Base
            with    sc.TypeDeclaration
            with    py.TypeDeclaration
    {
        val decl : Typed.TypeDeclaration
        val name = decl.name
        val scope = decl.scope
    }

    case class Interface(decl : Typed.Interface, genericArgs : List[Types.Base]) extends Declaration
    {
        val bases = decl.bases map {
            case x : Base => x
        }

        override def canCastToImpl(other : Base) =  bases exists { _ canCastTo other }

        override def returnTypeIfFunction =
            bases flatMap { _.returnTypeIfFunction } match {
                case Nil => None
                case x :: tl =>
                    if (tl exists { _ != x})
                        throw new Exception(s"Type $this casts to different functional types: " + (x :: tl))
                    Some(x)
            }
    }

    case class Alias(decl : Typed.Alias, genericArgs : List[Types.Base]) extends Declaration
    {
        val target = decl.target match {
            case x : Base => x
        }

        override def canCastToImpl(other : Base) =  target canCastTo other

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)

    private def getLabel(t : Base) = t match {
        case x : Declaration => x.name
    }

    def makeScalar(name : String, bases : Base*) = {
        val ty = Typed.Interface(name, Typed.topLevel, bases.toList)
        Typed.topLevel insert ty
        ty.apply()
    }

    def functionOf_(t : Base) = {
        val name = "IFunction_" + getLabel(t)
        val ty = Typed.Alias(name, Typed.topLevel, nullaryFunction(t))
        Typed.topLevel insert ty
        ty.apply()
    }


    def observableOf_(t : Base) = {
        val name = "IObservable_" + getLabel(t)
        val ty = Typed.Interface(name, Typed.topLevel, functionOf(t) :: Nil)
        Typed.topLevel insert ty
        ty.apply()
    }

    def functionOf = predef.Memoize1(functionOf_)
    def observableOf = predef.Memoize1(observableOf_)

    def genType(name : String, bases : Base*) = {
        val scalar  = makeScalar(name, bases : _*)
        val func    = functionOf(scalar)
        val obs     = observableOf(scalar)
        (scalar, func, obs)
    }



    val (float_, floatFunc, floatObservable) = genType("Float")
    val (string_, stringFunc, stringObservable) = genType("String")
    val (int_, intFunc, intObservable) = genType("Int", float_)
    val (boolean_, booleanFunc, booleanObservable) = genType("Boolean")
}
