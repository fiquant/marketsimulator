import syntax.scala.Printer.types

package object TypesUnbound
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}

    sealed abstract class Base
        extends sc.Base
        with    ScPrintable
    {
        def bind(m : ITypeMapper) : TypesBound.Base
    }

    trait ITypeMapper
    {
        def apply(t : Parameter) : TypesBound.Base
    }

    case class TypeMapper(decl : Typed.TypeDeclaration, genericArgs : List[TypesBound.Base]) extends ITypeMapper
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
            extends Base
    {
        override def toScala = name

        def bind(m : ITypeMapper) = m(this)
    }

    case object Unit
            extends Base
            with    sc.Unit
    {
        def bind(m : ITypeMapper) = TypesBound.Unit
    }

    case class Tuple(elems : List[Base])
            extends Base
            with    sc.Tuple
    {
        def bind(m : ITypeMapper) =
            TypesBound.Tuple(elems map { _ bind m })
    }

    case class Function(args : List[Base], ret : Base)
            extends Base
            with    sc.Function
    {
        def bind(m : ITypeMapper) =
            TypesBound.Function(
                args map { _ bind m },
                ret bind m)
    }

    sealed abstract class UserDefined
            extends Base
            with    sc.UsedDefined_Unbound
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Base]

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
    case class Interface(decl : Typed.InterfaceDecl, genericArgs : List[Base])
            extends UserDefined
    {
        def bind(m : ITypeMapper) = TypesBound.Interface(decl, genericArgs map { _ bind m })
    }

    case class Alias(decl : Typed.AliasDecl, genericArgs : List[Base])
            extends UserDefined
    {
        def bind(m : ITypeMapper) = TypesBound.Alias(decl, genericArgs map { _ bind m })
    }

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)

    val T = Parameter("T")
    val _T_ = T :: Nil

    val IFunction = Typed.AliasDecl("IFunction",
                                Typed.topLevel,
                                nullaryFunction(T),
                                _T_)

    Typed.topLevel insert IFunction

    val IObservable = Typed.InterfaceDecl("IObservable",
                                      Typed.topLevel,
                                      IFunction(_T_) :: Nil,
                                      _T_)

    Typed.topLevel insert IObservable

    def makeScalar(name : String, bases : Base*) = {
        val ty = Typed.InterfaceDecl(name, Typed.topLevel, bases.toList, Nil)
        Typed.topLevel insert ty
        ty.apply(Nil)
    }

    def functionOf(t : Base) = IFunction(t :: Nil)
    def observableOf(t : Base) = IObservable(t :: Nil)

}
