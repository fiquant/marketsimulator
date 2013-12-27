import syntax.scala.Printer.types

package object TypesUnbound
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}

    sealed abstract class Unbound
        extends sc.Base
        with    ScPrintable
    {
        def bind(m : ITypeMapper) : Types.Bound
    }

    trait ITypeMapper
    {
        def apply(t : Parameter) : Types.Bound
    }

    case class TypeMapper(decl : Typed.TypeDeclaration, genericArgs : List[Types.Bound]) extends ITypeMapper
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

    case object Unit
            extends Unbound
            with    sc.Unit
    {
        def bind(m : ITypeMapper) = Types.Unit
    }

    case class Tuple(elems : List[Unbound])
            extends Unbound
            with    sc.Tuple
    {
        def bind(m : ITypeMapper) =
            Types.Tuple(elems map { _ bind m })
    }

    case class Function(args : List[Unbound], ret : Unbound)
            extends Unbound
            with    sc.Function
    {
        def bind(m : ITypeMapper) =
            Types.Function(
                args map { _ bind m },
                ret bind m)
    }

    sealed abstract class UserDefined
            extends Unbound
            with    sc.UsedDefined_Unbound
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Unbound]

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
    case class Interface(decl : Typed.Interface, genericArgs : List[Unbound])
            extends UserDefined
    {
        def bind(m : ITypeMapper) = Types.Interface(decl, genericArgs map { _ bind m })
    }

    case class Alias(decl : Typed.Alias, genericArgs : List[Unbound])
            extends UserDefined
    {
        def bind(m : ITypeMapper) = Types.Alias(decl, genericArgs map { _ bind m })
    }

    def nullaryFunction(ret_type : Unbound) = Function(List(), ret_type)

    val T = Parameter("T")
    val _T_ = T :: Nil

    val IFunction = Typed.Alias("IFunction",
                                Typed.topLevel,
                                nullaryFunction(T),
                                _T_)

    Typed.topLevel insert IFunction

    val IObservable = Typed.Interface("IObservable",
                                      Typed.topLevel,
                                      IFunction(_T_) :: Nil,
                                      _T_)

    Typed.topLevel insert IObservable

    def makeScalar(name : String, bases : Unbound*) = {
        val ty = Typed.Interface(name, Typed.topLevel, bases.toList, Nil)
        Typed.topLevel insert ty
        ty.apply(Nil)
    }

    def functionOf(t : Unbound) = IFunction(t :: Nil)
    def observableOf(t : Unbound) = IObservable(t :: Nil)

}
