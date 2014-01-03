import syntax.scala.Printer.{typed => pp}
import AST.ScPrintable
import shapeless.syntax.typeable._
import scala.collection.immutable._
import Typed.AfterTyping

object NameTable {

    class Scope(val name : String = "_root_") extends pp.NamesScope with ScPrintable {

        var packages = Map[String, Scope]()
        var anonymous = List[Scope]()
        var members = Map[String, AST.Member]()
        var attributes = Typed.Attributes(Map.empty)
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        def add(m : AST.Member) {
            check_name_is_unique(m.name, m)
            members = members updated (m.name, m)
        }

        def qualifyName(x : String) = typed.get qualifyName x

        def qualifiedName = parent match {
            case Some(p) => p.qualifyName(name)
            case None    => name
        }

        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if (members contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + members(name) + "\r\n" + e)
            if (packages contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + packages(name) + "\r\n" + e)
            anonymous foreach { _.check_name_is_unique(name, e) }
        }

        def add(a : AST.Attribute) {
            attributes.items get a.name match {
                case None => attributes = Typed.Attributes(attributes.items updated (a.name, a.value))
                case Some(v) =>
                    throw new Exception(s"Duplicate definition for package attribute ${qualifyName(a.name)}: $v => ${a.value}" )
            }
        }

        def add(p : AST.PackageDef) {
            def populate(src: Scope, child: Scope) = {
                if (members contains child.name)
                    throw new Exception(s"Duplicate definition for ${child.name}:\r\n" + members(child.name) + "\r\n" + child)
                if (!(packages contains child.name)) {
                    src.packages = src.packages updated(child.name, child)
                    child.parent = Some(src)
                }
                src.packages(child.name)
            }
            val target = p.name match {
                case Some(qn) =>
                    (qn.names map (new Scope(_))).foldLeft(this) { populate }
                case None =>
                    val fresh = new Scope("$" + anonymous.length)
                    anonymous = fresh :: anonymous
                    fresh.parent = Some(this)
                    fresh
            }
            create(p.members, p.attributes, target)
        }

        def lookup[T <: AST.Member](qn : List[String], visited : HashSet[Scope] = HashSet.empty)(implicit t : Manifest[T]) : Option[(Scope, T)] = {
            if (visited contains this)
                None
            else {
                val v = visited + this
                anonymous map { _ lookup (qn, v) } find { _.nonEmpty } match {
                    case Some(Some((scope, x))) => Some((scope, x.asInstanceOf[T]))
                    case Some(None) => throw new Exception("cannot occur")
                    case None =>
                        qn match {
                            case Nil => throw new Exception("Qualified name cannot be empty")
                            case x :: Nil =>
                                members get x match {
                                    case Some(f) if f.cast[T].nonEmpty => Some((this, f.asInstanceOf[T]))
                                    case _ => parent flatMap { _ lookup (qn, v) }
                                }
                            case x :: tl =>
                                packages get x map { _ lookup tl } match {
                                    case None => parent flatMap { _ lookup (qn, v) }
                                    case y => y.get
                                }
                        }
                }
            }
        }

        def lookupFunction(name : List[String]) : Option[(Scope, AST.FunDef)] = lookup[AST.FunDef](name)
        def lookupType(name : List[String]) : Option[(Scope, AST.TypeDeclaration)] = lookup[AST.TypeDeclaration](name)

        def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name, p.attributes))
            }
            anonymous foreach {
                p => p.toTyped(target.createChild(p.attributes))
            }
            target
        }
    }

    private def create(p : AST.Definitions, a : Iterable[AST.Attribute], impl : Scope) {
        p.definitions foreach {
            case m : AST.Member => impl.add(m)
            case package_def : AST.PackageDef => impl.add(package_def)
        }
        a foreach { impl.add }
    }

    trait BeforeTyping extends Typed.AnnotationHandler
    {
        def beforeTyping(/** arguments of the annotation     */ args  : List[String])
                        (/** function to process             */ f     : AST.FunDef, 
                         /** scope where function is defined */ scope : Scope)
    }

    object BeforeTyping
    {
        def apply(scope : Scope)
        {
            scope.packages.values foreach { apply }
            scope.anonymous       foreach { apply }

            scope.members.values collect { case f : AST.FunDef =>
                Typer.annotationsOf(f) collect { case Typed.Annotation(g : BeforeTyping, args) => g.beforeTyping(args)(f, scope) }
            }
        }
    }


    def apply(p : List[AST.Definitions]) : Scope =
    {
        val impl : Scope = new Scope

        p foreach { create(_, Nil, impl) }

        BeforeTyping(impl)

        impl
    }

}
