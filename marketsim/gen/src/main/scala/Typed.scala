package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => sc}
    import generator.python.{Printer => py}
    import AST.{ScPrintable, ScPyPrintable}

    abstract class Expr
            extends ScPyPrintable
            with    sc.Expr
            with    py.Expr
    {
        def ty : Types.Bound
    }

    case class Neg(x : Expr)
            extends Expr
            with    sc.Neg
            with    py.Neg
            with    TypeInference.Neg

    case class BinOp(symbol : BinOpSymbol,
                     x      : Expr,
                     y      : Expr)
            extends Expr
            with    sc.BinOp
            with    py.BinOp
            with    TypeInference.BinOp

    case class IfThenElse(cond  : Expr,
                          x     : Expr,
                          y     : Expr)
            extends Expr
            with    sc.IfThenElse
            with    py.IfThenElse
            with    TypeInference.IfThenElse

    case class StringLit(value : String)
            extends Expr
            with    sc.StringLit
            with    py.StringLit
            with    TypeInference.StringLit

    case class IntLit(value : Int)
            extends Expr
            with    sc.IntLit
            with    py.IntLit
            with    TypeInference.IntLit


    case class FloatLit(x : Double)
            extends Expr
            with    sc.FloatLit
            with    py.FloatLit
            with    TypeInference.FloatLit

    case class ParamRef(p : Parameter)
            extends Expr
            with    sc.ParamRef
            with    py.ParamRef
            with    TypeInference.ParamRef

    case class FunctionCall(target      : Function,
                            arguments   : List[(Parameter, Expr)])
            extends Expr
            with    sc.FunCall
            with    py.FunCall
            with    TypeInference.FunctionCall

    case class Annotation(target    : AnnotationHandler,
                          parameters: List[String])
            extends sc.Annotation
            with    ScPrintable

    case class Attributes(items : Map[String, String])
            extends sc.Attributes
            with    ScPrintable

    case class Parameter(name        : String,
                         ty          : Types.Bound,
                         initializer : Option[Expr],
                         comment     : List[String])
            extends sc.Parameter
            with    ScPrintable

    case class Or(x : Expr,
                  y : Expr)
            extends Expr
            with    sc.Or
            with    py.Or
            with    TypeInference.BinaryBoolean

    case class And(x : Expr,
                   y : Expr)
            extends Expr
            with    sc.And
            with    py.And
            with    TypeInference.BinaryBoolean

    case class Not(x : Expr)
            extends Expr
            with    sc.Not
            with    py.Not
            with    TypeInference.UnaryBoolean

    case class Condition(symbol : CondSymbol,
                         x      : Expr,
                         y      : Expr)
            extends Expr
            with    sc.Condition
            with    py.Condition
            with    TypeInference.Condition

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : Types.Bound,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation],
                        attributes  : Attributes)
            extends sc.Function
            with    ScPrintable
    {
        def decorators = attributes :: annotations

        def getAttribute(name : String) = attributes.items get name match {
            case Some(v) => v
            case None =>    try {
                parent getAttribute name
            } catch {
                case e : Exception => throw new Exception(s"Cannot find attribute '$name' for function $this")
            }
        }

        override def equals(o : Any) = o match {
            case that : Function =>
                parent.qualifiedName == that.parent.qualifiedName &&
                name                 == that.name &&
                parameters           == that.parameters &&
                ret_type             == that.ret_type &&
                body                 == that.body &&
                docstring            == that.docstring &&
                attributes           == that.attributes &&
                annotations          == that.annotations
            case _ => false
        }

    }


    abstract class TypeDeclaration
    {
        val name        : String
        val scope       : Typed.Package
        val generics    : List[Types.Parameter]

        def apply(genericArgs : List[Types.Bound] = Nil) : Types.Declaration

        override def equals(o : Any) = o match {
            case that : TypeDeclaration => name == that.name && scope.qualifiedName == that.scope.qualifiedName
            case _ => false
        }

        def label = scope qualifyName name

        def matchTypeParameter(genericArgs : List[Types.Bound], t : Types.Parameter) =
            generics zip genericArgs find { _._1 == t } match {
                case Some(p) => p._2
                case None    => throw new Exception(s"Cannot find type parameter $t at $this")
            }

    }

    case class Alias(name       : String,
                     scope      : Typed.Package,
                     target     : Types.Unbound,
                     generics   : List[Types.Parameter] = Nil)
            extends TypeDeclaration
            with sc.AliasDecl
            with ScPrintable
    {
        private val impl = predef.Memoize1({
            genericArgs : List[Types.Bound] => Types.Alias(this, genericArgs)
        })
        def apply(genericArgs : List[Types.Bound]) = impl(genericArgs)
    }

    case class Interface(name       : String,
                         scope      : Typed.Package,
                         bases      : List[Types.Unbound],
                         generics   : List[Types.Parameter] = Nil)
            extends TypeDeclaration
            with    sc.InterfaceDecl
            with    ScPrintable
    {
        private val impl = predef.Memoize1({
            genericArgs : List[Types.Bound] => Types.Interface(this, genericArgs)
        })
        def apply(genericArgs : List[Types.Bound]) = impl(genericArgs)
    }



    class Package extends sc.TopLevelPackage with ScPrintable
    {
        var functions = Map[String, Function]()
        var packages = Map[String, SubPackage]()
        var anonymous = List[AnonymousPackage]()
        var types = Map[String, TypeDeclaration]()
        var annotations = List[Annotation]()
        val attributes = Attributes(Map.empty)

        def qualifiedName : List[String] = Nil

        def qualifyName(x : String) = x

        def getAttribute(name : String) : String =
            throw new Exception(s"Cannot find attribute named $name")

        def getName = ""

        def insert(f : Function)  = {
            functions = functions updated (f.name, f)
            f
        }

        def insert(t : TypeDeclaration) = {
            types = types updated (t.name, t)
            t
        }

        def createChild(n : String, a : Attributes) = {
            val p = new SubPackage(n, this, a)
            packages = packages.updated(p.name, p)
            p
        }

        def createChild(a : Attributes) = {
            val p = new AnonymousPackage(this, a)
            anonymous = p :: anonymous
            p
        }

        override def equals(o : Any) = o match {
            case that : Package =>
                (functions  equals that.functions) &&
                (packages   equals that.packages)  &&
                (anonymous  equals that.anonymous) &&
                (attributes equals that.attributes)
            case _ => false
        }

        def getOrElseUpdateFunction(name : String, default : => Typed.Function) =
            functions get name match {
                case Some(f) => f
                case None => insert(default)
            }

        // TODO: factor common implementation out

        def getOrElseUpdateType(name : String, default : => TypeDeclaration) =
            types get name match {
                case Some(t) => t
                case None => insert(default)
            }
    }

    val topLevel = new Package

    class AnonymousPackage(val parent : Package, override val attributes : Attributes)
            extends Package
            with    sc.AnonymousPackage
            with    ScPrintable
    {
        override def qualifiedName = parent.qualifiedName

        override def qualifyName(x : String) = parent qualifyName x

        override def getAttribute(name : String) = attributes.items get name match {
            case Some(v) => v
            case None    => parent getAttribute name
        }

    }

    class SubPackage(val name   : String,
                     parent     : Package,
                     attributes : Attributes)
            extends AnonymousPackage(parent, attributes)
            with    sc.SubPackage
            with    ScPrintable
    {
        override def qualifiedName = parent.qualifiedName :+ name

        override def qualifyName(x : String) = (qualifiedName mkString ".") + "." + x

        override def getName = name

        override def equals(o : Any) = o match {
            case that : SubPackage => super.equals(o) && name == that.name
            case _ => false
        }
    }

    trait AnnotationHandler
    {
        val name : String
    }

    object Annotations
    {
        var registry = Map[String, AnnotationHandler]()

        def register(handler : AnnotationHandler){
            registry = registry.updated(handler.name, handler)
        }

        def lookup(name : String) = registry.get(name) match {
            case Some(handler) => handler
            case None => throw new Exception(s"Cannot find annotation handler $name")
        }

        override def toString = registry.toString()
    }

}

