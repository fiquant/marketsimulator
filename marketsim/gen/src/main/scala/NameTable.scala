import syntax.scala.Printer.{typed => pp}
import predef.ScPrintable
import shapeless.syntax.typeable._
import scala.collection.immutable._
import Typed.AfterTyping

package object NameTable {

    case class Scope(name       : String = "_root_",
                     parameters : List[AST.Parameter] = Nil,
                     `abstract` : Boolean = false)
            extends pp.NamesScope
            with    ScPrintable
    {
        var packages    = Map.empty[String, Scope]
        var members     = Map.empty[String, AST.Member]
        var attributes  = Typed.Attributes(Map.empty)
        var parent      = Option.empty[Scope]
        var typed       = Option.empty[Typed.Package]
        var bases       = List.empty[AST.QualifiedName]

        val isRoot = name == "_root_"
        val isAnonymous = name startsWith "$"
        val nonAbstract = !`abstract`

        def add(m : AST.Member) {
            members get m.name match {
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
        }

        def add(a : AST.Attribute) = addAttribute(a.name, a.value)

        def addAttribute(key : String, value : String) {
            attributes.items get key match {
                case None => attributes = Typed.Attributes(attributes.items updated (key, value))
                case Some(v) =>
                    if (v != value)
                        throw new Exception(s"Duplicate definition for package attribute ${qualifyName(key)}: $v => $value at $this" )
            }
        }

        private def populate(child: Scope) : Scope = {
            if (members contains child.name)
                throw new Exception(s"Duplicate definition for ${child.name}:\r\n" + members(child.name) + "\r\n" + child)
            packages get child.name match {
                case Some(existing) =>
                    if (existing.`abstract` != child.`abstract`)
                        throw new Exception(s"Trying to merge packages with different `abstract` annotations:" + existing + child)
                    if (existing.parameters != child.parameters)
                        throw new Exception(s"Trying to merge packages with different parameters:" + existing + child)
                    child.members.values foreach existing.add
                    child.packages.values foreach existing.populate
                    child.attributes.items foreach { p => existing.addAttribute(p._1, p._2) }
                case None =>
                    packages = packages updated(child.name, child)
                    child.parent = Some(this)
            }
            packages(child.name)
        }

        private var anon_idx = 0

        private def addImpl(p : AST.PackageDef, qn : List[String]) : Scope = qn match {
            case Nil =>
                anon_idx += 1
                addImpl(p, "$" + anon_idx :: Nil)
            case x :: Nil =>
                populate(Scope(x, p.parameters, p.`abstract`))
            case x :: tl =>
                getPackageOrCreate(x) addImpl (p, tl)
        }

        def add(p : AST.PackageDef) {
            val target = addImpl(p, if (p.name.isEmpty) Nil else p.name.get.names)
            target.bases = target.bases ++ p.bases
            create(p.members, p.attributes, target)
        }

        def removeAbstract()
        {
            packages = packages filter { _._2.nonAbstract }

            packages.values foreach { _.removeAbstract() }
        }

        def removeAnonymous()
        {
            packages.values foreach { _.removeAnonymous() }

            val (anonymous, normal) =  packages partition { _._2.isAnonymous }

            packages = normal

            anonymous.values foreach {
                pkg =>
                    pkg.packages.values foreach { inner =>
                        inner.attributes = Typed.Attributes(pkg.attributes.items ++ inner.attributes.items)
                        populate(inner)
                    }
                    pkg.members.values foreach { m =>
                        add(m match {
                            case f : AST.FunDef =>
                                f.copy(decorators =
                                        (pkg.attributes.items map { p => AST.Attribute(p._1, p._2) }).toList
                                                ++ f.decorators)
                            case x => x
                        })
                    }
            }
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

        private def lookupPackageInnerScopes(qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            qn match {
                case x :: Nil => packages get x
                case x :: tl =>
                    packages get x map { _ lookupPackageInnerScopes tl } match {
                        case Some(y)  => y
                        case None     => None
                    }
            }
        }

        def lookupPackage(qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookupPackage qn
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookupPackage qn
                            case None    => lookupPackage(tl)
                        }
                    case _ =>
                        lookupPackageInnerScopes(qn) match {
                            case Some(x) => Some(x)
                            case None    =>
                                parent flatMap { _ lookupPackage  qn }
                        }
                }
        }



        private def injectBasesImpl()
        {
            bases foreach { base =>
                 lookupPackage(base.names) match {
                     case Some(b) =>
                         b.injectBasesImpl()
                         b.members.values filterNot { members contains _.name } foreach { add }
                         b.packages.values foreach { populate }
                         b.attributes.items foreach { p => addAttribute(p._1, p._2) }
                     case None =>
                         throw new Exception(s"Cannot find base package $base for $this")
                 }
            }
            bases = Nil
        }

        def injectBases()
        {
            injectBasesImpl()
            packages.values foreach { _.injectBases() }
        }

        private def lookupInnerScopes[T <: AST.Member](qn : List[String])(implicit t : Manifest[T]) : Option[(Scope, T)] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
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

        def lookupFunction      (name : List[String]) : Option[(Scope, AST.FunDef)]         = lookup[AST.FunDef](name)
        def lookupFunctionAlias (name : List[String]) : Option[(Scope, AST.FunAlias)]       = lookup[AST.FunAlias](name)
        def lookupType          (name : List[String]) : Option[(Scope, AST.TypeDeclaration)]= lookup[AST.TypeDeclaration](name)

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

        def fullyQualify(n : AST.QualifiedName) =
            lookup[AST.Member](n.names) match {
                case Some((scope, m)) => scope qualifyName m.name
                case None => throw new Exception(s"Cannot lookup $n from scope $name")
            }

        def fullyQualify(t : AST.Type) : AST.Type = t match {
            case AST.SimpleType(n, generics) =>
                AST.SimpleType(fullyQualify(n), generics map fullyQualify)
            case AST.TupleType(elems) => AST.TupleType(elems map fullyQualify)
            case AST.FunctionType(args, ret) => AST.FunctionType(args map fullyQualify, fullyQualify(ret))
            case AST.UnitType => AST.UnitType
        }

        def fullyQualify(isLocal : String => Boolean)(e : AST.Expr) : AST.Expr = e match {
            case AST.FunCall(n, params) =>
                AST.FunCall(
                    n.names match {
                        case x :: Nil if isLocal(x) => n
                        case _ => fullyQualify(n)
                    },
                    params map { _ map fullyQualify(isLocal) })

            case AST.Cast(x, ty) =>
                AST.Cast(fullyQualify(isLocal)(x), fullyQualify(ty))
            case x : AST.StringLit => x
            case x : AST.FloatLit => x
            case x : AST.IntLit => x
            case x : AST.Var =>
                if (isLocal(x.s))
                    x
                else
                    throw new Exception(s"Cannot lookup variable ${x.s} while qualifying $e")

            case AST.List_(xs) => AST.List_(xs map fullyQualify(isLocal))
            case AST.BinOp(s, x, y) => AST.BinOp(s, fullyQualify(isLocal)(x), fullyQualify(isLocal)(y))
            case AST.Neg(x) => AST.Neg(fullyQualify(isLocal)(x))
            case AST.IfThenElse(cond, x, y) => AST.IfThenElse(fullyQualify(isLocal)(cond), fullyQualify(isLocal)(x), fullyQualify(isLocal)(y))
            case AST.And(x, y) => AST.And(fullyQualify(isLocal)(x), fullyQualify(isLocal)(y))
            case AST.Or(x, y) => AST.Or(fullyQualify(isLocal)(x), fullyQualify(isLocal)(y))
            case AST.Not(x) => AST.Not(fullyQualify(isLocal)(x))
            case AST.Condition(c, x, y) => AST.Condition(c, fullyQualify(isLocal)(x), fullyQualify(isLocal)(y))
        }

        def fullyQualified(f : AST.FunDef, packageArgs : List[AST.Parameter] = Nil) = {
            def isLocal(n : String) = (packageArgs ++ f.parameters find { _.name == n }).nonEmpty
            f.copy(
                parameters = packageArgs ++ (f.parameters map { p =>
                    p.copy(
                        ty = p.ty map fullyQualify,
                        initializer = p.initializer map fullyQualify(isLocal(_))
                    )
                }),
                ty = f.ty map fullyQualify,
                body = f.body map fullyQualify(isLocal(_))
            )
        }

        def qualifyNames(packageArgs : List[AST.Parameter]) {
            packages.values foreach { p => p.qualifyNames(packageArgs ++ p.parameters) }

            members = members mapValues {
                case f : AST.FunDef => fullyQualified(f, packageArgs)
                case a : AST.FunAlias => a.copy(target = fullyQualify(a.target))
                case x => x
            }
        }

        def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name, p.attributes))
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

        println("\r\n\tremoving anonymous packages")
        impl.removeAnonymous()

        println("\tinjecting base packages")
        impl.injectBases()

        println("\tremoving abstract packages")
        impl.removeAbstract()

        println("\tapplying before typing annotations")
        Typed.BeforeTyping(impl)

        println("\tqualifying names")
        impl.qualifyNames(Nil)

        impl
    }

}
