import syntax.scala.Printer.types

package object TypesUnbound
{
    import predef.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}

    sealed abstract class Base
        extends sc.Base
        with    ScPrintable
    {
        def bind(m : ITypeMapper[TypesBound.Base]) : TypesBound.Base
        def substitute(m : ITypeMapper[TypesUnbound.Base]) : TypesUnbound.Base
    }

    trait ITypeMapper[T]
    {
        def apply(t : Parameter) : T
    }

    case class TypeMapper[T](decl : Typed.TypeDeclaration, genericArgs : List[T]) extends ITypeMapper[T]
    {
        def apply(t : Parameter) =
            decl.generics zip genericArgs find { _._1 == t } match {
                case Some(p) => p._2
                case None    => throw new Exception(s"Cannot find type parameter $t at $decl")
            }
    }

    object EmptyTypeMapper_Bound extends ITypeMapper[TypesBound.Base]
    {
        def apply(t : Parameter) =
            throw new Exception("Cannot do any type mapping")
    }

    object EmptyTypeMapper_Unbound extends ITypeMapper[TypesUnbound.Base]
    {
        def apply(t : Parameter) =
            throw new Exception("Cannot do any type mapping")
    }

    case class Parameter(name : String)
            extends Base
    {
        override def toScala = name

        def bind(m : ITypeMapper[TypesBound.Base]) = m(this)
        def substitute(m : ITypeMapper[TypesUnbound.Base]) = m(this)
    }

    case object Unit
            extends Base
            with    sc.Unit
    {
        def bind(m : ITypeMapper[TypesBound.Base]) = TypesBound.Unit
        def substitute(m : ITypeMapper[TypesUnbound.Base]) = TypesUnbound.Unit
    }

    case class Tuple(elems : List[Base])
            extends Base
            with    sc.Tuple
    {
        def bind(m : ITypeMapper[TypesBound.Base]) =
            TypesBound.Tuple(elems map { _ bind m })

        def substitute(m : ITypeMapper[TypesUnbound.Base]) =
            TypesUnbound.Tuple(elems map { _ substitute m })
    }

    case class Function(args : List[Base], ret : Base)
            extends Base
            with    sc.Function
    {
        def bind(m : ITypeMapper[TypesBound.Base]) =
            TypesBound.Function(
                args map { _ bind m },
                ret bind m,
                args.length)

        def substitute(m : ITypeMapper[TypesUnbound.Base]) =
            TypesUnbound.Function(
                args map { _ substitute m },
                ret substitute m)
    }

    sealed abstract class UserDefined
            extends Base
            with    sc.UsedDefined_Unbound
    {
        val decl        : Typed.TypeDeclaration
        val genericArgs : List[Base]

        if (decl.generics.length != genericArgs.length)
            throw new Exception(s"Type $decl is instantiated with wrong type parameters: $genericArgs" )

        def substitute(m : ITypeMapper[TypesUnbound.Base]) : UserDefined
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
        def bind(m : ITypeMapper[TypesBound.Base]) =
            if (decl.name == "Optional") {
                if (genericArgs.length != 1)
                    throw new Exception("Option[T] must have exactly one generic parameter")
                TypesBound.Optional(genericArgs(0) bind m)
            }
            else
                TypesBound.Interface(decl, genericArgs map { _ bind m })

        def substitute(m : ITypeMapper[TypesUnbound.Base]) = TypesUnbound.Interface(decl, genericArgs map { _ substitute m })
    }

    case class Alias(decl : Typed.AliasDecl, genericArgs : List[Base])
            extends UserDefined
    {
        def bind(m : ITypeMapper[TypesBound.Base]) = TypesBound.Alias(decl, genericArgs map { _ bind m })

        def substitute(m : ITypeMapper[TypesUnbound.Base]) = TypesUnbound.Alias(decl, genericArgs map { _ substitute m })
    }

    def nullaryFunction(ret_type : Base) = Function(List(), ret_type)

}
