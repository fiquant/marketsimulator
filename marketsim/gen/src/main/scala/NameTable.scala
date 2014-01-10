import syntax.scala.Printer.{typed => pp}
import predef.ScPrintable
import shapeless.syntax.typeable._
import scala.collection.immutable._
import Typed.AfterTyping

package object NameTable {

    class Scope(val name : String = "_root_") extends pp.NamesScope with ScPrintable {

        var packages = Map[String, Scope]()
        var anonymous = List[Scope]()
        var members = Map[String, AST.Member]()
        var attributes = Typed.Attributes(Map.empty)
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        val isRoot = name == "_root_"
        val isAnonymous = name startsWith "$"

        def add(m : AST.Member) {
            members get m.name match {  // TODO: lookup at anon spaces too
                case None =>
                    check_name_is_unique(m.name, m)
                    members = members updated (m.name, m)
                case Some(x) =>
                    if (x != m)
                        throw new Exception(s"Trying to replace member $x\r\n by $m\r\n at $qualifiedNameAnon" )
            }
        }

        def qualifyName(x : String) : AST.QualifiedName =
            AST.QualifiedName(qualifiedName.names :+ x)

        private def getQualifiedName(show_anonymous : Boolean = false) : AST.QualifiedName =
            AST.QualifiedName(
                if (isRoot)
                    (if (show_anonymous) name else "") :: Nil
                else
                    if (isAnonymous && !show_anonymous)
                        (parent.get getQualifiedName show_anonymous).names
                    else
                        (parent.get getQualifiedName show_anonymous).names :+ name
            )

        lazy val qualifiedName     = getQualifiedName(show_anonymous = false)
        lazy val qualifiedNameAnon = getQualifiedName(show_anonymous = true)

        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if ((members contains name) && members(name) != e)
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

        def getPackageOrCreate(name : String) =
            packages get name match {
                case Some(p) => p
                case None    =>
                    val p = new Scope(name)
                    p.parent = Some(this)
                    packages = packages updated (name, p)
                    p
            }

        private def lookupInnerScopes[T <: AST.Member](qn : List[String])(implicit t : Manifest[T]) : Option[(Scope, T)] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            anonymous map { _ lookupInnerScopes qn } find { _.nonEmpty } match {
                case Some(x)
                    => x
                case None =>
                    qn match {
                        case x :: Nil =>
                            members get x match {
                                case Some(f) if f.cast[T].nonEmpty
                                    => Some((this, f.asInstanceOf[T]))
                                case _
                                    => None
                            }
                        case x :: tl =>
                            packages get x map { _ lookupInnerScopes tl } match {
                                case Some(y)  => y
                                case None     => None
                            }
                    }
            }
        }


        def lookup[T <: AST.Member](qn : List[String])(implicit t : Manifest[T]) : Option[(Scope, T)] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookup qn
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookup qn
                            case None    => lookup(tl)
                        }
                    case _ =>
                        lookupInnerScopes(qn) match {
                            case Some(x) => Some(x)
                            case None    =>
                                parent flatMap { _ lookup qn }
                        }
                }
        }

        def lookupFunction(name : List[String]) : Option[(Scope, AST.FunDef)] = lookup[AST.FunDef](name)
        def lookupFunctionAlias(name : List[String]) : Option[(Scope, AST.FunAlias)] = lookup[AST.FunAlias](name)
        def lookupType(name : List[String]) : Option[(Scope, AST.TypeDeclaration)] = lookup[AST.TypeDeclaration](name)

        def resolveFunction(name : AST.QualifiedName) : Option[(Scope, AST.FunDef)] =
            lookupFunction(name.names) match {
                case r : Some[_] => r
                case None =>
                    println("resolve alias for " + name)
                    lookupFunctionAlias(name.names) match {
                        case Some((scope, alias)) =>
                            scope resolveFunction alias.target
                        case None =>
                            None
                    }
            }

        def fullyQualifyB(e : AST.BooleanExpr) : AST.BooleanExpr = e match {
            case AST.And(x, y) => AST.And(fullyQualifyB(x), fullyQualifyB(y))
            case AST.Or(x, y) => AST.Or(fullyQualifyB(x), fullyQualifyB(y))
            case AST.Not(x) => AST.Not(fullyQualifyB(x))
            case AST.Condition(c, x, y) => AST.Condition(c, fullyQualify(x), fullyQualify(y))
        }

        def fullyQualify(n : AST.QualifiedName) =
            lookup[AST.Member](n.names) match {
                case Some((scope, m)) => scope qualifyName m.name
                case None => throw new Exception(s"Cannot lookup $n from scope $this")
            }

        def fullyQualify(t : AST.Type) : AST.Type = t match {
            case AST.SimpleType(n, generics) => AST.SimpleType(fullyQualify(n), generics map fullyQualify)
            case AST.TupleType(elems) => AST.TupleType(elems map fullyQualify)
            case AST.FunctionType(args, ret) => AST.FunctionType(args map fullyQualify, fullyQualify(ret))
            case AST.UnitType => AST.UnitType
        }

        def fullyQualify(e : AST.Expr) : AST.Expr = e match {
            case AST.FunCall(n, params) =>
                AST.FunCall(fullyQualify(n), params map { _ map fullyQualify})
            case AST.Cast(x, ty) =>
                AST.Cast(fullyQualify(x), fullyQualify(ty))
            case x : AST.StringLit => x
            case x : AST.FloatLit => x
            case x : AST.IntLit => x
            case x : AST.Var => x
            case AST.BinOp(s, x, y) => AST.BinOp(s, fullyQualify(x), fullyQualify(y))
            case AST.Neg(x) => AST.Neg(fullyQualify(x))
            case AST.IfThenElse(cond, x, y) => AST.IfThenElse(fullyQualifyB(cond), fullyQualify(x), fullyQualify(y))
        }

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



    def apply(p : List[AST.Definitions]) : Scope =
    {
        val impl : Scope = new Scope

        p foreach { create(_, Nil, impl) }

        Typed.BeforeTyping(impl)

        impl
    }

}
