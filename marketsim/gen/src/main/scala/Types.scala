package object Types
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    // TODO:
    //  Generics        type G[T] : F[T]

    sealed abstract class Unbound

    case class Parameter(name : String)
            extends Unbound
            with    ScPrintable
    {
         override def toScala = name
    }

    sealed abstract class Bound
            extends Unbound
            with    sc.Bound
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

    sealed abstract class Declaration
            extends Bound
            with    sc.TypeDeclaration
            with    py.TypeDeclaration
    {
        val decl : Typed.TypeDeclaration
        val name = decl.name
        val scope = decl.scope
        val generics = decl.generics
    }

    case class Interface(decl : Typed.Interface, genericArgs : List[Types.Bound]) extends Declaration
    {
        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Interface $decl is instantiated with wrong type parameters: $genericArgs" )

        val bases = decl.bases map {
            case x : Bound => x
            case x : Parameter => decl matchTypeParameter (genericArgs, x)
        }

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

    case class Alias(decl : Typed.Alias, genericArgs : List[Types.Bound]) extends Declaration
    {
        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Alias $decl is instantiated with wrong type parameters: $genericArgs" )

        val target = decl.target match {
            case x : Bound => x
            case x : Parameter => decl matchTypeParameter (genericArgs, x)
        }

        override def canCastToImpl(other : Bound) =  target canCastTo other

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

    def nullaryFunction(ret_type : Bound) = Function(List(), ret_type)

    private def getLabel(t : Bound) = t match {
        case x : Declaration => x.name
    }

    def makeScalar(name : String, bases : Bound*) = {
        val ty = Typed.Interface(name, Typed.topLevel, bases.toList)
        Typed.topLevel insert ty
        ty.apply()
    }

    def functionOf_(t : Bound) = {
        val name = "IFunction_" + getLabel(t)
        val ty = Typed.Alias(name, Typed.topLevel, nullaryFunction(t))
        Typed.topLevel insert ty
        ty.apply()
    }


    def observableOf_(t : Bound) = {
        val name = "IObservable_" + getLabel(t)
        val ty = Typed.Interface(name, Typed.topLevel, functionOf(t) :: Nil)
        Typed.topLevel insert ty
        ty.apply()
    }

    def functionOf = predef.Memoize1(functionOf_)
    def observableOf = predef.Memoize1(observableOf_)

    def genType(name : String, bases : Bound*) = {
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
