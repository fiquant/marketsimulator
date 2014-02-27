import scala.util.matching.Regex

package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => sc}
    import generator.python.{Printer => py}
    import predef.{ScPrintable, ScPyPrintable}

    abstract class Expr
            extends ScPyPrintable
            with    sc.Expr
            with    py.Expr
    {
        def ty : TypesBound.Base
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

    case class FunctionRef(f : Function)
            extends Expr
            with    sc.FunctionRef
            with    py.FunctionRef
            with    TypeInference.FunctionRef

    case class FunctionCall(target      : Expr,
                            arguments   : List[Expr])
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
                         ty          : TypesBound.Base,
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

    case class Cast(x   : Expr,
                    ty  : TypesBound.Base)
            extends Expr
            with    sc.Cast
            with    py.Cast
    {
        if (x.ty cannotCastTo ty)
            throw new Exception(s"Expression $x of type ${x.ty} cannot be casted to $ty")
    }

    case class List_(xs : List[Expr])
            extends Expr
            with    sc.List_
            with    py.List_
            with    TypeInference.List_

    trait FunctionDecl
    {
        val parent : Package
        val name   : String
        val target : Function
        def parameter_names : List[String] = target.parameters map { _.name }
    }

    case class FunctionAlias(parent : Package,
                             name   : String,
                             target : Function)
            extends sc.FunctionAlias
            with    ScPrintable
            with    FunctionDecl
    {
        override def equals(o : Any) = o match {
            case other : FunctionAlias => other.target == target
            case _ => false
        }
    }

    trait AttributeReplace
    {
        def getParent : Option[AttributeReplace]
        def attributes : Attributes

        def tryGetAttributeImpl(name : String) : Option[String] = attributes.items get name match {
            case Some(v) => Some(v)
            case None =>    getParent flatMap { _ tryGetAttributeImpl name }
        }

        def substNamesInAttribute(value : String, name : String) =
            (new Regex("\\{\\{(\\w+)\\}\\}", "x") 
                    replaceAllIn(value, m => tryGetAttribute(m group "x") match {
                        case Some(y) => y
                        case None    =>
                            throw new Exception(s"Cannot find attribute named ${m group "x"} when evaluating attribute $name")
                    }))

        def tryGetAttribute(name : String) : Option[String] =
            tryGetAttributeImpl(name) map { substNamesInAttribute(_, name) }
    }

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : TypesBound.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation],
                        attributes  : Attributes)
            extends sc.Function
            with    ScPrintable
            with    AttributeReplace
            with    AST.Positional
            with    FunctionDecl
    {
        val target = this

        def getParent = Some(parent.asInstanceOf[AttributeReplace])

        def decorators = attributes :: annotations

        def qualifiedName = parent qualifyName name

        val ty = TypesBound.Function(parameters map { _.ty }, ret_type)

        def getAttribute(name : String) = tryGetAttribute(name) match {
            case Some(v) => v
            case None =>    throw new Exception(s"Cannot find attribute '$name' for function $this")
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


    trait TypeDeclaration
    {
        val name        : String
        val parent      : Package
        val generics    : List[TypesUnbound.Parameter]

        def resolveGenerics(genericArgs : List[TypesUnbound.Base]) : TypesUnbound.Base

        override def equals(o : Any) = o match {
            case that : TypeDeclaration => name == that.name && parent.qualifiedName == that.parent.qualifiedName
            case _ => false
        }

        def label = (parent qualifyName name) + (if (generics.isEmpty) "" else generics mkString ("[", ",", "]"))
    }

    case class AliasDecl(name       : String,
                         parent      : Typed.Package,
                         target     : TypesUnbound.Base,
                         generics   : List[TypesUnbound.Parameter],
                         annotations : List[Annotation],
                         attributes  : Attributes)
            extends TypeDeclaration
            with    sc.AliasDecl
            with    ScPrintable
    {
        def decorators = attributes :: annotations

        private val unbound = predef.Memoize1({
            genericArgs : List[TypesUnbound.Base] =>
                TypesUnbound.Alias(this, genericArgs)
        })
        def resolveGenerics(genericArgs : List[TypesUnbound.Base]) = unbound(genericArgs)

        var instances = Set.empty[TypesBound.Base]

        def addInstance(x : TypesBound.Base) {
            instances = instances + x
        }

        def getInstances = (instances map { _.unOptionalize }).toList sortBy { _.asScala.length }

    }

    case class InterfaceDecl(name       : String,
                             parent      : Typed.Package,
                             bases      : List[TypesUnbound.Base],
                             generics   : List[TypesUnbound.Parameter],
                             annotations : List[Annotation],
                             attributes  : Attributes)
            extends TypeDeclaration
            with    sc.InterfaceDecl
            with    ScPrintable
    {
        def decorators = attributes :: annotations

        private val unbound = predef.Memoize1({
            genericArgs : List[TypesUnbound.Base] =>
                TypesUnbound.Interface(this, genericArgs)
        })
        def resolveGenerics(genericArgs : List[TypesUnbound.Base]) = unbound(genericArgs)

        var instances = Set.empty[TypesBound.Interface]

        def addInstance(x : TypesBound.Interface) {
            instances = instances + x
        }

        def getInstances = instances map { _.unOptionalize }
    }



    abstract class Package
    {
        var functions = Map[String, List[FunctionDecl]]()
        var packages = Map[String, SubPackage]()
        var types = Map[String, TypeDeclaration]()
        var annotations = List[Annotation]()
        val attributes = Attributes(Map.empty)

        def qualifiedName : AST.QualifiedName
        def qualifyName(x : String) : AST.QualifiedName = qualifiedName :+ x
        def tryGetAttribute(name : String) : Option[String]
        def tryGetAttributeImpl(name : String) : Option[String]
        def getName : String

        def insert(fs : List[FunctionDecl]) = {

            if (functions contains fs.head.name)
                assert(fs == functions(fs.head.name))
            else
                functions = functions updated (fs.head.name, fs)
        }

        def insert(t : TypeDeclaration) = {
            types = types updated (t.name, t)
            t
        }

        def createChild(n : String, a : Attributes) = {
            val p = new SubPackage(n, this, a)
            packages = packages updated (p.name, p)
            p
        }

        override def equals(o : Any) = o match {
            case that : Package =>
                (functions       equals that.functions) &&
                (packages        equals that.packages)  &&
                (attributes      equals that.attributes)
            case _ => false
        }

        protected def getFunctionImpl(name : String) =
            (functions getOrElse (name, Nil)) map { _.target }

        def getFunction(name : String) = getFunctionImpl(name)

        def getOrElseUpdateType(name : String, default : => TypeDeclaration) =
            types get name match {
                case Some(t) => t
                case None => insert(default)
            }
    }

    def getMethodName(f : Function) =
        f tryGetAttribute "method" getOrElse f.name

    def getMethodName(scope : NameTable.Scope, f : AST.FunDef) =
        scope tryGetAttributeFor (f, "method") getOrElse f.name


    class TopLevelPackage
            extends Package
            with    sc.TopLevelPackage
            with    ScPrintable
            with    AttributeReplace
    {
        private var used_types = Set.empty[TypesBound.Base]

        def addTypeUsage(t : TypesBound.Base) {
            used_types = used_types + t.unOptionalize
        }

        private var methods_by_name = Map.empty[String, Map[TypesBound.Base, Set[AST.QualifiedName]]]
        private var methods_by_type = Map.empty[TypesBound.Base, Map[String, Set[NameTable.Scope]]]
        private var untyped = Option.empty[NameTable.Scope]

        def getParent = None

        def setMethods(source : NameTable.Scope, ms : Stream[(TypesBound.Base, NameTable.Scope, AST.FunDef)])
        {
            untyped = Some(source)

            methods_by_name =
                    (ms groupBy { e => getMethodName(e._2, e._3) }
                        filterKeys { _ != "N/A"}
                        mapValues {
                        (_ groupBy   { _._1 }
                           mapValues { p =>
                                (p map { x => x._2 qualifyName x._3.name }).toSet[AST.QualifiedName]
                        })
                    })

            methods_by_type =
                    (ms groupBy { _._1 }
                        mapValues {
                        (_ groupBy   { _._3.name  }
                           mapValues { p =>
                                (p map { _._2 }).toSet[NameTable.Scope]
                        })
                    })

//            methods_by_name foreach { case (name, xs) =>
//                println(name)
//                xs foreach { case (ty, names) =>
//                    println("\t" + ty.asScala + ":" + (names mkString "," ))
//                }
//            }
        }
        
        def lookupMethod(name : String, ty : TypesBound.Base) =

            methods_by_name get name match {
                case None       => Nil
                case Some(m)    =>
                    (m.toList   filter  { ty canCastTo _._1 }
                                flatMap {
                                    _._2.toList flatMap { p =>
                                        Typer.Processor(untyped.get) lookupFunction p
                    }})
            }

        def getMethods(t : TypesBound.Base) = {

            def checkFunctionsCompatible(p : (String, List[Function])) = {
                if (p._2 exists { _.qualifiedName != p._2.head.qualifiedName })
                    println("Functions from different scopes trying to bind to method name " + p._1
                            + (p._2 map { predef.crlf + _.qualifiedName } mkString "") )
                p
            }

            ((methods_by_type getOrElse  (t, Map.empty)).toList
                flatMap { case (name, scopes) =>
                    scopes flatMap { scope =>
                        ((scope.typed.get.functions get name).get
                                collect { case f : Function => f }
                                map     { f => (getMethodName(f), f) }
                                filter  { _._1 != "N/A" }
                                groupBy { _._1 }
                                map     { p => (p._1, p._2 map { _._2 })}
                                map     { checkFunctionsCompatible })
                    }
                }).toMap
        }


        def argumentDependentLookup(name : String, ty : TypesBound.Base) =

            methods_by_name getOrElse (name, Nil) filter { ty canCastTo _._1 } flatMap { _._2 }

        def qualifiedName = "" :: Nil

        def getName = ""

        def getScalar(name : String) =
            (types get name).get resolveGenerics Nil

        def getScalarBound(name : String) =
            getScalar(name) bind EmptyTypeMapper

        lazy val IFunction = (types get "IFunction").get.asInstanceOf[AliasDecl]

        def unboundFunctionOf(t : TypesUnbound.Base) =
            IFunction resolveGenerics  t :: Nil

        lazy val IObservable = (types get "IObservable").get.asInstanceOf[InterfaceDecl]
        lazy val Observable = (types get "Observable").get.asInstanceOf[InterfaceDecl]

        def unboundObservableOf(t : TypesUnbound.Base) =
            IObservable resolveGenerics  t :: Nil

        val EmptyTypeMapper = TypesUnbound.EmptyTypeMapper_Bound

        def genType(name : String) = {
            val scalar  = getScalar(name)
            val func    = unboundFunctionOf(scalar)
            val obs     = unboundObservableOf(scalar)
            val m = EmptyTypeMapper
            (scalar, scalar bind m, func bind m, obs bind m)
        }

        lazy val (unbound_float,     float_, floatFunc, floatObservable) = genType("Float")
        lazy val (unbound_string,    string_, stringFunc, stringObservable) = genType("String")
        lazy val (unbound_int,       int_, intFunc, intObservable) = genType("Int")
        lazy val (unbound_boolean,   boolean_, booleanFunc, booleanObservable) = genType("Boolean")
        lazy val (unbound_side,      side_, sideFunc, sideObservable) = genType("Side")

        lazy val IOrderGenerator = getScalarBound("IOrderGenerator")
        lazy val ISingleAssetStrategy = getScalarBound("ISingleAssetStrategy")
        lazy val Side = getScalarBound("Side")
        lazy val IEvent = getScalarBound("IEvent")

        def observableOf(t : TypesBound.Base) =
            TypesBound.Interface(IObservable, t :: Nil)

        def observableImplOf(t : TypesBound.Base) =
            TypesBound.Interface(Observable, t :: Nil)

        
    }

    private var topLevelInstance : Option[TopLevelPackage] = None

    def topLevel = topLevelInstance.get

    def withNewTopLevel[T](f : => T) : T ={
        val old = topLevelInstance
        topLevelInstance = Some(new TopLevelPackage)
        val ret = f
        topLevelInstance = old
        ret
    }

    class SubPackage(val name   : String,
                     val parent : Package,
                     override val attributes : Attributes)
            extends Package
            with    sc.SubPackage
            with    ScPrintable
            with    AttributeReplace
    {
        override def getFunction(name : String) =
            getFunctionImpl(name) match {
                case Nil    => parent getFunction name
                case f      => f
            }

        def getParent = Some(parent.asInstanceOf[AttributeReplace])

        override def qualifiedName = parent.qualifiedName :+ name

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

    trait BeforeTyping extends Typed.AnnotationHandler
    {
        def beforeTyping(/** arguments of the annotation     */ args  : List[String])
                        (/** function to process             */ f     : AST.FunDef,
                         /** scope where function is defined */ scope : NameTable.Scope)
    }

    object BeforeTyping
    {
        def apply(scope : NameTable.Scope)
        {
            scope.packages.values foreach { apply }

            scope.functions.values flatMap { _ collect { case f : AST.FunDef =>
                Typer.annotationsOf(f) collect { case Typed.Annotation(g : BeforeTyping, args) => g.beforeTyping(args)(f, scope) }
            } }
        }
    }

    trait AfterTyping extends AnnotationHandler
    {
        def afterTyping(/** arguments of the annotation */ args  : List[String])
                       (/** function to process         */ f     : Typed.Function)
    }

    object AfterTyping
    {
        def apply(pkg : Package = topLevel)
        {
            pkg.packages.values foreach { apply(_) }

            pkg.functions.values foreach { _ foreach {
                case f : Typed.Function =>
                    f.annotations collect { case Typed.Annotation(g : AfterTyping, args) => g.afterTyping(args)(f) }
                case f : Typed.FunctionAlias =>
            } }
        }
    }
}

