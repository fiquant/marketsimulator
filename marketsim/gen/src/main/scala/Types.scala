import syntax.scala.Printer.typed

package object Types
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    // TODO:
    //  Generics        type G[T] : F[T]

    sealed abstract class Unbound
        extends sc.Base
        with    ScPrintable
    {
        def bind(m : ITypeMapper) : Bound
    }

    trait ITypeMapper
    {
        def apply(t : Parameter) : Bound
    }

    case class TypeMapper(decl : Typed.TypeDeclaration, genericArgs : List[Bound]) extends ITypeMapper
    {
        def apply(t : Parameter) =
            decl.generics zip genericArgs find { _._1 == t } match {
                case Some(p) => p._2
                case None    => throw new Exception(s"Cannot find type parameter $t at $decl")
            }
    }

    object EmptyTypeMapper extends ITypeMapper
    {
        def apply(t : Parameter) =
            throw new Exception("Cannot do any type mapping")
    }


    case class Parameter(name : String)
            extends Unbound
    {
        override def toScala = name

        def bind(m : ITypeMapper) = m(this)
    }

    case object Unit_Unbound
            extends Unbound
            with    sc.Unit
    {
        def bind(m : ITypeMapper) = Unit
    }

    case class Tuple_Unbound(elems : List[Unbound])
            extends Unbound
            with    sc.Tuple
    {
        def bind(m : ITypeMapper) =
            Tuple(elems map { _ bind m })
    }

    case class Function_Unbound(args : List[Unbound], ret : Unbound)
            extends Unbound
            with    sc.Function
    {
        def bind(m : ITypeMapper) =
            Function(
                args map { _ bind m },
                ret bind m)
    }

    sealed abstract class UserDefined_Unbound
            extends Unbound
            with    sc.UsedDefined
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Types.Unbound]

        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Type $decl is instantiated with wrong type parameters: $genericArgs" )
    }

    /**
     * This class represents a call to a (possibly) unbound interface like InterfaceA[ConcreteTypeA, (T, U)]
     * @param decl -- a reference to the interface declaration: InterfaceA
     * @param genericArgs -- list of arguments passed to the generic: List(ConcreteTypeA, (T, U))
     *
     * When a generic interface is instantiated with concrete type (when a function is defined)
     * we need to bind it against concrete arguments;
     * if the generic inherits from another generic interface we need to substitute its unbound arguments with bound arguments
     * */
    case class Interface_Unbound(decl : Typed.Interface, genericArgs : List[Types.Unbound])
            extends UserDefined_Unbound
    {
        def bind(m : ITypeMapper) = Interface(decl, genericArgs map { _ bind m })
    }

    case class Alias_Unbound(decl : Typed.Alias, genericArgs : List[Types.Unbound])
            extends UserDefined_Unbound
    {
        def bind(m : ITypeMapper) = Alias(decl, genericArgs map { _ bind m })
    }


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
        val genericArgs : List[Types.Bound]

        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Type $decl is instantiated with wrong type parameters: $genericArgs" )
    }

    case class Interface(decl : Typed.Interface, genericArgs : List[Types.Bound]) extends UserDefined
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

    case class Alias(decl : Typed.Alias, genericArgs : List[Types.Bound]) extends UserDefined
    {
        val target = decl.target bind TypeMapper(decl, genericArgs)

        override def canCastToImpl(other : Bound) =  target canCastTo other

        override def returnTypeIfFunction = target.returnTypeIfFunction
    }

    def nullaryFunction(ret_type : Unbound) = Function_Unbound(List(), ret_type)

    private def getLabel(t : Unbound) = t match {
        case x : UserDefined_Unbound => x.decl.name
    }

    def makeScalar(name : String, bases : Unbound*) = {
        val ty = Typed.Interface(name, Typed.topLevel, bases.toList)
        Typed.topLevel insert ty
        ty.apply(Nil)
    }

    def functionOf_(t : Unbound) = {
        val name = "IFunction_" + getLabel(t)
        val ty = Typed.Alias(name, Typed.topLevel, nullaryFunction(t))
        Typed.topLevel insert ty
        ty.apply(Nil)
    }


    def observableOf_(t : Unbound) = {
        val name = "IObservable_" + getLabel(t)
        val ty = Typed.Interface(name, Typed.topLevel, functionOf(t) :: Nil)
        Typed.topLevel insert ty
        ty.apply(Nil)
    }

    def functionOf = predef.Memoize1(functionOf_)
    def observableOf = predef.Memoize1(observableOf_)

    def genType(name : String, bases : Unbound*) = {
        val scalar  = makeScalar(name, bases : _*)
        val func    = functionOf(scalar)
        val obs     = observableOf(scalar)
        val m = Types.EmptyTypeMapper
        (scalar, scalar bind m, func bind m, obs bind m)
    }

    //val IFunction = Typed.Alias("IFunction", Typed.topLevel, null)


    val (unbound_float,     float_, floatFunc, floatObservable) = genType("Float")
    val (unbound_string,    string_, stringFunc, stringObservable) = genType("String")
    val (unbound_int,       int_, intFunc, intObservable) = genType("Int", unbound_float)
    val (unbound_boolean,   boolean_, booleanFunc, booleanObservable) = genType("Boolean")
}
