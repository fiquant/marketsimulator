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
        var functions   = Map.empty[String, List[AST.FunctionDeclaration]]
        var types       = Map.empty[String, AST.TypeDeclaration]
        var attributes  = Typed.Attributes(Map.empty)
        var parent      = Option.empty[Scope]
        var typed       = Option.empty[Typed.Package]
        var bases       = List.empty[AST.QualifiedName]

        val isRoot = name == "_root_"
        val isAnonymous = name startsWith "$"
        val nonAbstract = !`abstract`

        override def equals(o : Any) = o match {
            case other : Scope =>
                name == other.name &&
                parameters == other.parameters &&
                `abstract` == other.`abstract` &&
                packages == other.packages &&
                attributes == other.attributes &&
                types == other.types &&
                bases == other.bases &&
                functions == other.functions
            case _ => false
        }

        def add(m : AST.FunctionDeclaration) {
            functions get m.name match {
                case None =>
                    functions = functions updated (m.name, m :: Nil)
                case Some(overloads) =>
                    if (!(overloads contains m))
                        functions = functions updated (m.name, m :: overloads)
            }
        }

        def add(t : AST.TypeDeclaration) {
            types get t.name match {
                case None =>
                    check_name_is_unique(t.name, t)
                    types = types updated (t.name, t)
                case Some(x) =>
                    if (x != t)
                        throw new Exception(s"Trying to replace type member $x\r\n by $t\r\n at $qualifiedNameAnon" )
            }
        }

        def qualifyName(x : String) : AST.QualifiedName = qualifiedName :+ x

        private def getQualifiedName(show_anonymous : Boolean = false) : AST.QualifiedName =
                if (isRoot)
                    (if (show_anonymous) name else "") :: Nil
                else
                    if (isAnonymous && !show_anonymous)
                        parent.get getQualifiedName show_anonymous
                    else
                        (parent.get getQualifiedName show_anonymous) :+ name

        lazy val qualifiedName     = getQualifiedName(show_anonymous = false)
        lazy val qualifiedNameAnon = getQualifiedName(show_anonymous = true)

        private def check_name_is_unique(name : String, e : Any) {
            if ((functions contains name) && functions(name) != e)
                throw new Exception(s"Duplicate definition for $name:\r\n" + functions(name) + "\r\n" + e)
            if ((types contains name) && types(name) != e)
                throw new Exception(s"Duplicate definition for $name:\r\n" + types(name) + "\r\n" + e)
            if (packages contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + packages(name) + "\r\n" + e)
        }

        def getAttribute(name : String) : Option[String] =

            attributes.items get name match {
                case None    =>
                    parent flatMap { _.getAttribute(name) }
                case x => x
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
            packages get child.name match {
                case Some(existing) =>
                    if (existing.`abstract` != child.`abstract`)
                        throw new Exception(s"Trying to merge packages with different `abstract` annotations:" + existing + child)
                    if (existing.parameters != child.parameters)
                        throw new Exception(s"Trying to merge packages with different parameters:" + existing + child)
                    child.functions.values foreach { _ foreach existing.add }
                    child.types.values foreach existing.add
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
            val target = addImpl(p, if (p.name.isEmpty) Nil else p.name.get)
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
                    pkg.functions.values foreach { _ foreach { m =>
                        add(m match {
                            case f : AST.FunDef =>
                                f.copy(decorators =
                                        (pkg.attributes.items map { p => AST.Attribute(p._1, p._2) }).toList
                                                ++ f.decorators)
                            case x => x
                        })
                    } }
                    pkg.types.values foreach { add }
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

        private def injectBasesImpl()
        {
            bases foreach { base =>
                 lookupPackage(base) match {
                     case Some(b) =>
                         b.injectBasesImpl()
                         b.functions.values filterNot { functions contains _.head.name } foreach { _ foreach { add  } }
                         b.types.values filterNot { types contains _.name } foreach { add }
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

        def lookupInnerScopes(hasName : (Scope, String) => Boolean, qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in inner scopes of $qualifiedNameAnon ")
            qn match {
                case x :: Nil =>
                    if (hasName(this, x)) Some(this) else None
                case x :: tl =>
                    packages get x map { _.lookupInnerScopes(hasName, tl) } match {
                        case Some(y)  => y
                        case None     => None
                    }
            }
        }


        def lookupScope(hasName : (Scope, String) => Boolean, qn : List[String]) : Option[Scope] =
        {
            //println(s"looking for $qn in $qualifiedNameAnon")
            if (isAnonymous)
                parent.get lookupScope (hasName, qn)
            else
                qn match {
                    case Nil => throw new Exception("Qualified name cannot be empty")
                    case "" :: tl =>
                        parent match {
                            case Some(p) => p lookupScope (hasName, qn)
                            case None    => lookupScope(hasName, tl)
                        }
                    case _ =>
                        lookupInnerScopes(hasName, qn) match {
                            case None    => parent match {
                                case None => None
                                case Some(p) => p lookupScope (hasName, qn)
                            }
                            case x => x
                        }
                }
        }

        def hasFunction(name : String) = functions contains name
        def hasPackage(name : String) = packages contains name
        def hasType(name : String) = types contains name

        def lookupType(qn : List[String]) : Option[(Scope, AST.TypeDeclaration)] =
            lookupScope(_ hasType _, qn) map { scope => (scope, scope.types(qn.last) )}

        def lookupPackage(qn : List[String]) : Option[Scope] =
            lookupScope(_ hasPackage _, qn) map { _.packages(qn.last) }


        def lookupFunction(qn : List[String]) : List[(Scope, AST.FunDef)] =

            lookupScope(_ hasFunction _, qn) match {
                case None => Nil
                case Some(scope) =>
                    scope.functions(qn.last) flatMap {
                        case f : AST.FunDef  => (scope, f) :: Nil
                        case a : AST.FunAlias => scope lookupFunction a.target
                    }
            }

        def fullyQualifyType(n : AST.QualifiedName) =
            lookupType(n) match {
                case Some((scope, m)) => scope qualifyName m.name
                case None => throw new Exception(s"Cannot lookup $n from scope $name")
            }

        def fullyQualifyType(t : AST.Type) : AST.Type = t match {
            case AST.SimpleType(n, generics) =>
                AST.SimpleType(fullyQualifyType(n), generics map fullyQualifyType)
            case AST.TupleType(elems) => AST.TupleType(elems map fullyQualifyType)
            case AST.FunctionType(args, ret) => AST.FunctionType(args map fullyQualifyType, fullyQualifyType(ret))
            case AST.UnitType => AST.UnitType
        }


        def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name, p.attributes))
            }
            target
        }

        def fullyQualifyName(n : AST.QualifiedName) =
            lookupScope(_ hasFunction _, n) match {
                case None => throw new Exception(s"Cannot lookup $n from scope $name")
                case Some(scope) => scope qualifyName n.last
            }

        def fullyQualify(isLocal : String => Boolean) =
        {
            def qualify(e : AST.Expr) : AST.Expr = e match {
                case AST.FunCall(n, params) =>
                    val (qualified, extra_params) =
                        n.names match {
                            case x :: Nil if isLocal(x) => (n, Nil)
                            case _ =>
                                lookupScope(_ hasFunction _, n) match {
                                    case Some(scope) =>
                                        (scope qualifyName n.last, scope.collectParameters.toList)
                                    case None =>
                                        throw new Exception(s"Cannot lookup $n from scope $name")
                                }
                        }
                    val extra = extra_params map { p => AST.Var(p.name) }
                    //println(context.last._2)
                    AST.FunCall(qualified, extra ++ (params map  qualify) )

                case AST.Cast(x, ty) =>
                    AST.Cast(qualify(x), fullyQualifyType(ty))
                case x : AST.StringLit => x
                case x : AST.FloatLit => x
                case x : AST.IntLit => x
                case x : AST.Var =>
                    if (isLocal(x.s))
                        x
                    else
                        throw new Exception(s"Cannot lookup variable ${x.s} while qualifying $e")

                case AST.List_(xs) => AST.List_(xs map qualify)
                case AST.BinOp(s, x, y) => AST.BinOp(s, qualify(x), qualify(y))
                case AST.Neg(x) => AST.Neg(qualify(x))
                case AST.IfThenElse(cond, x, y) => AST.IfThenElse(qualify(cond), qualify(x), qualify(y))
                case AST.And(x, y) => AST.And(qualify(x), qualify(y))
                case AST.Or(x, y) => AST.Or(qualify(x), qualify(y))
                case AST.Not(x) => AST.Not(qualify(x))
                case AST.Condition(c, x, y) => AST.Condition(c, qualify(x), qualify(y))
            }
            qualify(_)
        }

        def fullyQualified(f : AST.FunDef) = {
            def isLocal(n : String) =
                (f.parameters find { _.name == n }).nonEmpty || getParameter(n).nonEmpty

            f.copy(
                parameters = (collectParameters.toList ++ f.parameters) map { p =>
                    p.copy(
                        ty = p.ty map fullyQualifyType,
                        initializer = p.initializer map fullyQualify(isLocal(_))
                    )
                },
                ty = f.ty map fullyQualifyType,
                body = f.body map fullyQualify(isLocal(_))
            )
        }

        def getParameter(name : String) : Option[AST.Parameter] =

            parameters find { _.name == name } match {
                case None => parent flatMap { _ getParameter name }
                case x    => x
            }

        def collectParameters : Stream[AST.Parameter] =
            (parent match {
                case None    => Stream.empty
                case Some(p) => p.collectParameters
            }) ++ parameters.toStream

        def qualifyNames() {
            packages.values foreach { _.qualifyNames() }

            functions = functions mapValues { _ map {
                case f : AST.FunDef => fullyQualified(f)
                case a : AST.FunAlias => a.copy(target = fullyQualifyName(a.target))
                case x => x
            } }
        }
    }

    private def create(p : AST.Definitions, a : Iterable[AST.Attribute], impl : Scope) {
        p.definitions foreach {
            case t : AST.TypeDeclaration        => impl add t
            case m : AST.FunctionDeclaration    => impl add m
            case package_def : AST.PackageDef   => impl add package_def
        }
        a foreach { impl.add }
    }


    def create(p : List[AST.Definitions]) : Option[Scope] =
    {
        val impl : Scope = new Scope

        try {
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
            impl.qualifyNames()

            Some(impl)
        } catch {
            case e : Exception =>
                if (config.catch_errors) {
                    println("An error occured during building name tables:")
                    println(e.getMessage)
                    None
                }
                else throw e
        }

    }

}
